# Task: Dockerize the Mini RAG Course App

## Project Goal

Dockerize this beginner-friendly RAG app so it can be built and run consistently on any machine with Docker. The app has a FastAPI backend, a simple frontend, and a local medicine document corpus.

## What You Will Build

- A Docker image for the backend.
- A Docker image for the frontend.
- A Docker Compose setup that runs both services together.
- A local setup that beginners can understand and reproduce.
- A local Chroma DB that stores the chunked medicine documents.

## Folder Layout

- `dockerize/backend`: FastAPI backend code.
- `dockerize/frontend`: Static frontend files.
- `dockerize/docs`: Medicine source documents.
- `dockerize/.env`: Secrets and local configuration.

## Step 1: Task - Build The Chroma DB

This is the first thing to do before Dockerizing anything.

### Goal

Build the local vector database from the medicine documents so the backend can search it later.

### What To Do

Create and run the indexing script:

```bash
cd dockerize/backend
python build_chroma_db.py
```

### What The Script Does

- reads every `.txt` file in `docs/`;
- splits each file into chunks;
- converts each chunk into embeddings with Mistral;
- stores the chunks and embeddings in Chroma DB at `backend/chroma_db/`.

### Why This Comes First

- the backend search endpoint now reads from Chroma DB instead of rebuilding embeddings on every request;
- beginners can separate indexing from serving;
- it makes the RAG flow easier to understand.

### Check Your Work

- Confirm the `backend/chroma_db/` folder exists.
- Run one search question after the DB is built.
- Make sure the backend can use the stored chunks instead of rebuilding them each time.

## Step 2: Prepare Python With uv

Install `uv` using pip:

```bash
pip install uv
```

Create and activate the backend virtual environment:

```bash
cd dockerize/backend
uv venv
.venv\Scripts\activate
```

Install backend dependencies:

```bash
uv pip install -e .
```

## Step 3: Configure Environment

The `.env` file must stay inside the `dockerize/` folder.

Required variable:

```env
MISTRAL_API_KEY=your_key_here
```

The backend reads this key to call Mistral embeddings and chat models.

## Step 4: Run Locally Before Docker

Start the backend:

```bash
cd dockerize/backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open the frontend by serving the folder:

```bash
cd dockerize/frontend
python -m http.server 5173
```

Then visit:

```text
http://localhost:5173
```

## Step 5: Dockerize The Backend

Create `backend/Dockerfile`.

Requirements:

- Use `python:3.12-slim`.
- Install `uv` with `pip install uv`.
- Copy `pyproject.toml` first.
- Install dependencies with `uv pip install --system -e .`.
- Copy backend code.
- Expose port `8000`.
- Start FastAPI with `uvicorn`.
- Keep the Chroma DB outside the image and rebuild it locally when the documents change.

Beginner note:

- Copying dependency files before source code helps Docker reuse layers when only the app code changes.

## Step 6: Dockerize The Frontend

Create `frontend/Dockerfile`.

Requirements:

- Use a lightweight web server image such as `nginx:alpine`, or use Python's built-in server for learning.
- Copy `index.html`, `styles.css`, and `app.js`.
- Expose port `80` if using nginx.

Beginner note:

- The frontend here is static, so it only needs a simple server to deliver files to the browser.

## Step 7: Add docker-compose.yml

Create `docker-compose.yml` inside `dockerize/`.

Requirements:

- Service `backend` builds from `./backend`.
- Service `frontend` builds from `./frontend`.
- `backend` uses `env_file: .env`.
- Backend maps `8000:8000`.
- Frontend maps `5173:80` if using nginx.
- The frontend must call the backend at `http://localhost:8000`.
- The backend should be able to search the local Chroma DB.

Beginner note:

- Compose is the easiest way to run a multi-service project without typing multiple long Docker commands.

## Step 8: Verify The App

Run:

```bash
docker compose up --build
```

Check:

- Backend health endpoint: `http://localhost:8000/health`
- Frontend page: `http://localhost:5173`
- Ask a medicine question such as `What is hypertension?`
- Confirm the response includes sources from the medicine documents.

## Step 9: Explain What Happened

After testing, make sure you can explain:

- what the backend container runs;
- what the frontend container serves;
- where the API key lives;
- why ports are mapped;
- why Docker Compose is useful.
- why the Chroma DB is built before Docker.

## Beginner Tasks

### Task A: Build The Chroma DB

- Run the indexing script.
- Confirm the `backend/chroma_db/` folder is created.
- Ask why indexing and serving are separate steps.

### Task B: Build One Image

- Build only the backend image.
- Run it.
- Open `/health` in a browser.

### Task C: Run Both Services

- Start the full Compose setup.
- Open the frontend.
- Ask one question and check the answer.

### Task D: Read The Dockerfile

- Explain each Dockerfile instruction in plain language.
- Identify where dependencies are installed.
- Identify where the app starts.

### Task E: Improve The Project

- Add a `.dockerignore` file.
- Keep secrets out of the image.
- Reduce image size where possible.
- Rebuild the Chroma DB when the documents change.

## Common Beginner Mistakes

- Forgetting to create the `.env` file.
- Hardcoding the API key in source code.
- Running Docker before the local app works.
- Mixing up host ports and container ports.
- Forgetting to rebuild after changing dependencies.
- Forgetting to rebuild the Chroma DB after changing source documents.

## Success Criteria

You are done when:

- the backend starts inside Docker;
- the frontend starts inside Docker;
- the frontend can call the backend;
- the RAG answer returns the correct source documents;
- you can explain the setup to another beginner.
- you can explain why the Chroma DB is built before Dockerizing.

