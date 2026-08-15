from __future__ import annotations

import math
import os
from dataclasses import dataclass
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from fastapi import HTTPException

try:
    from mistralai import Mistral
except ImportError:
    from mistralai.client import Mistral


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"
ENV_PATH = ROOT / ".env"
CHROMA_DIR = ROOT / "backend" / "chroma_db"
COLLECTION_NAME = "medicine_documents"
EMBED_MODEL = "mistral-embed"
CHAT_MODEL = "mistral-small-latest"

load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class ChunkRecord:
    chunk_id: str
    file: str
    text: str
    metadata: dict[str, str | int]


@dataclass(frozen=True)
class RetrievedChunk:
    file: str
    score: float
    text: str


def client() -> Mistral:
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key or api_key == "your_key_here":
        raise HTTPException(
            status_code=500,
            detail="Set MISTRAL_API_KEY in dockerize/.env before asking questions.",
        )
    return Mistral(api_key=api_key)


def chroma_client() -> chromadb.PersistentClient:
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


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


def build_chunks() -> list[ChunkRecord]:
    chunks: list[ChunkRecord] = []
    for path in sorted(DOCS_DIR.glob("*.txt")):
        for index, text in enumerate(chunk_text(path.read_text(encoding="utf-8"))):
            chunk_id = f"{path.name}:{index:04d}"
            chunks.append(
                ChunkRecord(
                    chunk_id=chunk_id,
                    file=path.name,
                    text=text,
                    metadata={"file": path.name, "chunk_index": index},
                )
            )
    return chunks


def get_collection() -> chromadb.Collection:
    return chroma_client().get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def rebuild_chroma_db() -> int:
    mistral = client()
    chunks = build_chunks()

    if not chunks:
        raise HTTPException(status_code=500, detail="No .txt documents found in docs/.")

    embeddings = embed_texts(mistral, [chunk.text for chunk in chunks])
    collection = get_collection()
    collection.upsert(
        ids=[chunk.chunk_id for chunk in chunks],
        documents=[chunk.text for chunk in chunks],
        metadatas=[chunk.metadata for chunk in chunks],
        embeddings=embeddings,
    )
    return collection.count()


def search_chroma(question: str, top_k: int) -> list[RetrievedChunk]:
    collection = get_collection()
    if collection.count() == 0:
        raise HTTPException(
            status_code=500,
            detail="Chroma DB is empty. Run backend/build_chroma_db.py first.",
        )

    mistral = client()
    question_embedding = embed_texts(mistral, [question])[0]
    result = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    documents = result.get("documents", [[]])[0]
    metadatas = result.get("metadatas", [[]])[0]
    distances = result.get("distances", [[]])[0]

    retrieved: list[RetrievedChunk] = []
    for document, metadata, distance in zip(documents, metadatas, distances):
        file_name = str(metadata.get("file", "unknown")) if metadata else "unknown"
        score = 1.0 - float(distance) if distance is not None else 0.0
        retrieved.append(RetrievedChunk(file=file_name, score=score, text=document))

    return retrieved