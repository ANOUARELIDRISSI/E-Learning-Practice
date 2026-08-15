# Mini Course: Build a Medicine RAG App

## Lesson 1: What RAG Means

RAG means Retrieval Augmented Generation. A normal chat model answers from its trained knowledge. A RAG app first searches your own documents, then sends the most relevant passages to the model with the user's question. This makes the answer more grounded in your course material.

## Lesson 2: The Pipeline

1. Put documents in `docs/`.
2. Split documents into chunks.
3. Convert chunks into embeddings with Mistral.
4. Convert the user's question into an embedding.
5. Compare the question embedding with chunk embeddings.
6. Send the best chunks to the chat model.
7. Return an answer plus source filenames.

## Lesson 3: Why Chunking Matters

Documents are often too large to send completely. Chunking creates smaller pieces that can be searched more precisely. In this project, each text file is split by word count. A production app may use smarter chunking by headings, paragraphs, overlap, and metadata.

## Lesson 4: Why Embeddings Matter

Embeddings turn text into vectors. Similar meanings produce vectors that are close together. This lets the app retrieve a document about hypertension even if the user asks about "high blood pressure."

## Lesson 5: What To Improve Next

- Cache embeddings instead of rebuilding them on every question.
- Add document upload.
- Store vectors in a database.
- Add authentication.
- Add citations with exact passages.
- Dockerize backend and frontend using `task.md`.

