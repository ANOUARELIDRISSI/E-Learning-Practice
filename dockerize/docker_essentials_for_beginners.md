# Docker Essentials for Beginners

Docker lets you package an application with the exact runtime, dependencies, and configuration it needs. Instead of telling someone to install Python, Node, system libraries, and environment variables manually, you describe the environment once and run it anywhere Docker is available.

## Core Ideas

- **Image**: a reusable blueprint for an application environment.
- **Container**: a running instance of an image.
- **Dockerfile**: instructions for building an image.
- **docker-compose.yml**: a file that runs multiple services together, such as a backend and frontend.
- **Volume**: storage that persists or mounts files into a container.
- **Port mapping**: exposes a container port on your machine, for example `8000:8000`.
- **Environment variable**: configuration passed to the app, such as `MISTRAL_API_KEY`.

## Common Commands

```bash
docker build -t my-app .
docker run --env-file .env -p 8000:8000 my-app
docker compose up --build
docker compose down
docker ps
docker logs <container_name>
```

## Dockerfile Basics

A backend Dockerfile usually:

1. Starts from a base image, such as `python:3.12-slim`.
2. Sets a working directory.
3. Copies dependency files.
4. Installs dependencies.
5. Copies source code.
6. Defines the command to start the app.

Example:

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN pip install uv && uv pip install --system -e .
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Compose Basics

Use Compose when an app has more than one service:

```yaml
services:
  backend:
    build: ./backend
    env_file: .env
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
```

## Beginner Checklist

- Keep secrets in `.env`, not in source code.
- Add `.env` to `.gitignore`.
- Use clear service names like `backend` and `frontend`.
- Expose only the ports users need.
- Rebuild after dependency changes.
- Read container logs when something fails.
- Keep images small by using slim base images.
- Verify that the app works locally before Dockerizing it.

