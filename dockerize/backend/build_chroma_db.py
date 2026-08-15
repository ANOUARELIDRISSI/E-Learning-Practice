from __future__ import annotations

from app.rag_store import rebuild_chroma_db


def main() -> None:
    total_chunks = rebuild_chroma_db()
    print(f"Chroma DB built successfully with {total_chunks} chunks.")


if __name__ == "__main__":
    main()