from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.rag_store import CHAT_MODEL, RetrievedChunk, client, search_chroma

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


@app.get("/health")
def health() -> dict[str, str | int]:
    return {"status": "ok", "collection": "medicine_documents"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    mistral = client()
    retrieved_chunks = search_chroma(payload.question, payload.top_k)

    ranked = [
        Source(file=chunk.file, score=chunk.score, text=chunk.text)
        for chunk in retrieved_chunks
    ]

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
