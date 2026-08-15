# Mini Course: Build a Medicine RAG App

## Course Overview

This mini course shows how a Retrieval Augmented Generation app works using medicine documents. A normal chat model answers from its trained knowledge. A RAG app first searches your own documents, then sends the most relevant passages to the model with the user's question. This makes the answer more grounded in your course material.

## Learning Goals

By the end of this mini course, you should be able to:

- explain what RAG means;
- describe the steps in a retrieval pipeline;
- understand why chunking and embeddings matter;
- understand why Chroma DB is used in this project;
- trace how a question becomes an answer with sources;
- connect the RAG app to Docker once the app works locally.

## Lesson 1: What RAG Means

RAG means Retrieval Augmented Generation. The app does not rely only on the model's memory. It first finds relevant text in your documents, then gives that text to the model so the answer is tied to the course content.

## Lesson 2: The RAG Pipeline

1. Put documents in `docs/`.
2. Split documents into chunks.
3. Convert chunks into embeddings with Mistral.
4. Convert the user's question into an embedding.
5. Store the chunk embeddings in Chroma DB.
6. Compare the question embedding with the stored chunk embeddings in Chroma DB.
7. Send the best chunks to the chat model.
8. Return an answer plus source filenames.

## Lesson 3: Why Chunking Matters

Documents are often too large to send completely. Chunking creates smaller pieces that can be searched more precisely. In this project, each text file is split by word count. A production app may use smarter chunking by headings, paragraphs, overlap, and metadata.

## Lesson 4: Why Embeddings Matter

Embeddings turn text into vectors. Similar meanings produce vectors that are close together. This lets the app retrieve a document about hypertension even if the user asks about "high blood pressure."

## Lesson 5: What The Backend Does

The backend:

- reads the medicine documents;
- chunks the text;
- creates embeddings for the chunks and stores them in Chroma DB;
- searches the Chroma DB for the user's question;
- sends the best matches to the chat model;
- returns an answer and source files.

The local vector database lives in `backend/chroma_db/` and is built by the indexing script before Dockerizing the app.

## Lesson 6: What The Frontend Does

The frontend:

- shows a question box;
- sends the question to the backend;
- displays the answer;
- displays the top matching sources.

## Beginner Exercises

### Exercise 1: Follow The Flow

- Open one file in `docs/`.
- Identify one likely chunk boundary.
- Explain why that text is useful for retrieval.

### Exercise 2: Test Retrieval

- Ask about a known topic like hypertension.
- Check whether the source file matches the question.
- Compare the answer with the source text.

### Exercise 3: Test Another Topic

- Ask about a different document, such as asthma or diabetes.
- Confirm the returned sources change with the topic.

## What To Improve Next

- Cache embeddings instead of rebuilding them on every question.
- Add document upload.
- Store vectors in a managed database.
- Add authentication.
- Add citations with exact passages.
- Dockerize backend and frontend using `task.md` after building the Chroma DB.

## Beginner Checklist

- Understand the difference between retrieval and generation.
- Verify that the app works before adding Docker.
- Keep source filenames visible in answers.
- Test with multiple questions, not just one.

