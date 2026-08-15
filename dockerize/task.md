# Task: Dockerize the Mini RAG Course App

Your goal is to Dockerize this beginner-friendly RAG app. The app has a FastAPI backend, a simple frontend, and a local medicine document corpus.

## 1. Prepare Python With uv

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

## 2. Configure Environment

The `.env` file must stay inside the `dockerize/` folder.

Required variable:

```env
MISTRAL_API_KEY=your_key_here
```

The backend reads this key to call Mistral embeddings and chat models.

## 3. Run Locally Before Docker

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

## 4. Dockerize the Backend

Create `backend/Dockerfile`.

Requirements:

- Use `python:3.12-slim`.
- Install `uv` with `pip install uv`.
- Copy `pyproject.toml`.
- Install dependencies with `uv pip install --system -e .`.
- Copy backend code.
- Expose port `8000`.
- Start FastAPI with `uvicorn`.

## 5. Dockerize the Frontend

Create `frontend/Dockerfile`.

Requirements:

- Use a lightweight web server image such as `nginx:alpine`, or use Python's built-in server for learning.
- Copy `index.html`, `styles.css`, and `app.js`.
- Expose port `80` if using nginx.

## 6. Add docker-compose.yml

Create `docker-compose.yml` inside `dockerize/`.

Requirements:

- Service `backend` builds from `./backend`.
- Service `frontend` builds from `./frontend`.
- `backend` uses `env_file: .env`.
- Backend maps `8000:8000`.
- Frontend maps `5173:80` if using nginx.
- The frontend must call the backend at `http://localhost:8000`.

## 7. Verify

Run:

```bash
docker compose up --build
```

Check:

- Backend health endpoint: `http://localhost:8000/health`
- Frontend page: `http://localhost:5173`
- Ask a medicine question such as: `What is hypertension?`
- Confirm the response includes sources from the medicine documents.

