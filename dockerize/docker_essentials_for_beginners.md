# Docker Essentials for Beginners

## Course Overview

Docker packages an application with the runtime, dependencies, and configuration it needs. Instead of telling someone to install Python, Node, system libraries, and environment variables manually, you describe the environment once and run it anywhere Docker is available.

This course is written for beginners who want to understand Docker and learn how to dockerize a simple application.

## Learning Goals

By the end of this course, you should be able to:

- explain what an image, container, Dockerfile, and Compose file are;
- run a container and inspect it;
- build a custom image from a Dockerfile;
- expose ports and pass environment variables;
- use Docker Compose to run multiple services together;
- understand the basic steps needed to dockerize a backend and a frontend.

## Prerequisites

- Basic command-line knowledge.
- A working Docker installation.
- A sample app to practice on, such as the Mini RAG Course project.

## Key Concepts

### Image

An image is a reusable blueprint for an application environment. It contains the operating system layer, dependencies, and app files needed to start a container.

### Container

A container is a running instance of an image. You can start, stop, remove, and inspect containers.

### Dockerfile

A Dockerfile is a text file that describes how to build an image step by step.

### Docker Compose

Docker Compose runs multiple services together, such as a backend and a frontend, from one configuration file.

### Volume

A volume stores data outside the container so it can survive restarts and be shared with the host machine.

### Port Mapping

Port mapping exposes a container port on your machine, for example `8000:8000`.

### Environment Variables

Environment variables are configuration values passed to the app, such as `MISTRAL_API_KEY`.

## Common Commands

```bash
docker build -t my-app .
docker run --env-file .env -p 8000:8000 my-app
docker compose up --build
docker compose down
docker ps
docker logs <container_name>
docker exec -it <container_name> sh
```

## How A Dockerfile Works

A typical backend Dockerfile follows these steps:

1. Start from a base image, such as `python:3.12-slim`.
2. Set a working directory.
3. Copy dependency files first.
4. Install dependencies.
5. Copy the application code.
6. Define the command that starts the app.

Example:

```Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN pip install uv && uv pip install --system -e .

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## How Docker Compose Works

Use Compose when an app has more than one service.

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
      - "5173:80"
```

## Beginner Workflow

1. Run the app locally first.
2. Identify the backend entry point.
3. Identify required environment variables.
4. If the project uses retrieval, build the local vector store or Chroma DB first.
5. Create a Dockerfile for the backend.
6. Create a Dockerfile for the frontend.
7. Add Docker Compose.
8. Test the app again inside Docker.

## Beginner Tasks

### Task 1: Learn The Basics

- Define image, container, Dockerfile, volume, and Compose in your own words.
- Run `docker ps` and `docker logs` on a container.

### Task 2: Build A Single Container

- Build the backend image.
- Run the backend container.
- Open the health endpoint in a browser.

### Task 3: Connect Two Services

- Run backend and frontend together with Docker Compose.
- Confirm the frontend can call the backend API.

### Task 4: Explain The Setup

- Describe what each line of the Dockerfile does.
- Explain why `.env` should stay outside the image.
- Explain why port mapping is needed.

## Beginner Checklist

- Keep secrets in `.env`, not in source code.
- Add `.env` to `.gitignore`.
- Use clear service names like `backend` and `frontend`.
- Expose only the ports users need.
- Rebuild after dependency changes.
- Read container logs when something fails.
- Keep images small by using slim base images.
- Verify that the app works locally before Dockerizing it.

## Common Mistakes

- Copying too many files too early in the Dockerfile.
- Forgetting to expose or map the correct port.
- Baking secrets into the image.
- Testing Docker before the app works locally.
- Ignoring logs when the container exits immediately.

## What To Practice Next

- Add a `.dockerignore` file.
- Replace hardcoded values with environment variables.
- Separate development and production Docker setups.
- Learn how volumes help with persistent data.

