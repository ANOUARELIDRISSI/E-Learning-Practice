from __future__ import annotations

import math
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
try:
    from mistralai import Mistral
except ImportError:
    from mistralai.client import Mistral
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"
ENV_PATH = ROOT / ".env"
EMBED_MODEL = "mistral-embed"
CHAT_MODEL = "mistral-small-latest"

load_dotenv(ENV_PATH)

app = FastAPI(title="Mini RAG Course API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str = Field(min_length=3)
    top_k: int = Field(default=4, ge=1, le=8)


class Source(BaseModel):
    file: str
    score: float
    text: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


class Chunk(BaseModel):
    file: str
    text: str
    embedding: list[float]


def client() -> Mistral:
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key or api_key == "your_key_here":
        raise HTTPException(
            status_code=500,
            detail="Set MISTRAL_API_KEY in dockerize/.env before asking questions.",
        )
    return Mistral(api_key=api_key)


def chunk_text(text: str, max_words: int = 120) -> list[str]:
    words = text.split()
    return [" ".join(words[i : i + max_words]) for i in range(0, len(words), max_words)]


def embed_texts(mistral: Mistral, texts: list[str]) -> list[list[float]]:
    response = mistral.embeddings.create(model=EMBED_MODEL, inputs=texts)
    return [item.embedding for item in response.data]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def load_chunks() -> list[Chunk]:
    mistral = client()
    chunks: list[Chunk] = []
    for path in sorted(DOCS_DIR.glob("*.txt")):
        for text in chunk_text(path.read_text(encoding="utf-8")):
            chunks.append(Chunk(file=path.name, text=text, embedding=[]))

    if not chunks:
        raise HTTPException(status_code=500, detail="No .txt documents found in docs/.")

    embeddings = embed_texts(mistral, [chunk.text for chunk in chunks])
    return [
        Chunk(file=chunk.file, text=chunk.text, embedding=embedding)
        for chunk, embedding in zip(chunks, embeddings)
    ]


@app.get("/health")
def health() -> dict[str, str | int]:
    return {"status": "ok", "documents": len(list(DOCS_DIR.glob("*.txt")))}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    mistral = client()
    chunks = load_chunks()
    question_embedding = embed_texts(mistral, [payload.question])[0]

    ranked = sorted(
        (
            Source(
                file=chunk.file,
                score=cosine_similarity(question_embedding, chunk.embedding),
                text=chunk.text,
            )
            for chunk in chunks
        ),
        key=lambda source: source.score,
        reverse=True,
    )[: payload.top_k]

    context = "\n\n".join(
        f"Source: {source.file}\n{source.text}" for source in ranked
    )
    messages = [
        {
            "role": "system",
            "content": (
                "You are a careful medical education assistant. Use only the provided "
                "course context. Explain clearly, cite source filenames, and remind "
                "learners that this is not personal medical advice."
            ),
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {payload.question}",
        },
    ]
    response = mistral.chat.complete(model=CHAT_MODEL, messages=messages)
    answer = response.choices[0].message.content or "No answer generated."
    return AskResponse(answer=answer, sources=ranked)
