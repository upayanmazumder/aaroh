# next-api-ai-template

A full-stack AI-powered starter template with **Next.js frontend**, **Express backend**, and a **Python AI module**.
Structured into `app/`, `api/`, and `ai/` for clean development, rapid prototyping, and seamless integration.

---

## Tech Stack

- **Frontend:** Next.js (TypeScript, pnpm)
- **Backend:** Express.js (Node.js, pnpm)
- **AI Service:** Python (Flask)
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions (ready for build + push caching)

---

## Folder Structure

```
.
├── app/         # Next.js frontend
│   └── Dockerfile
├── api/         # Express backend
│   └── Dockerfile
├── ai/          # Python Flask microservice
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── pnpm-workspace.yaml
```

---

## Getting Started

### Clone the repo

```bash
git clone https://github.com/upayanmazumder/next-api-ai-template.git
cd next-api-ai-template
```

### Run with Docker

Build and start all services:

```bash
docker compose up --build
```

Then open:

- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **API:** [http://localhost:4000](http://localhost:4000)
- **AI:** [http://localhost:5000](http://localhost:5000)

---

## How It Works

- **Next.js (`app/`)** → Handles UI + user interactions.
- **Express (`api/`)** → Acts as middleware and routes frontend requests to AI service.
- **Flask (`ai/`)** → Processes AI logic or ML inference and returns responses to the API.

Each layer is isolated, containerized, and easily swappable.

---

## Example Flow

1. Frontend sends text → `/api/analyze`
2. Express forwards it to Flask at `/predict`
3. Flask responds with mock or real AI prediction
4. Response bubbles back to UI instantly

---

## Docker Compose Overview

| Service | Port | Description      |
| ------- | ---- | ---------------- |
| `app`   | 3000 | Next.js frontend |
| `api`   | 4000 | Express backend  |
| `ai`    | 5000 | Flask AI service |

Each service includes caching, health checks, and restart policies.
You can deploy them independently or as a full stack.

---

## Development Notes

- Uses `pnpm` for efficient dependency management.
- Python virtual env not needed — handled via Docker.
- Ready for GitHub Actions auto-build (with GHA cache).

---

## Commands

```bash
# Run locally (no docker)
cd app && pnpm dev
cd api && pnpm run dev
cd ai && python main.py

# Run all with docker
docker compose up
```

---

## Future Ideas

- Add real model inference (OpenAI / Ollama / HuggingFace)
- Add shared types via `common/`
- Integrate PostgreSQL or Redis service
- Deploy to Fly.io, Railway, or Render

---

## License

Licensed under the [MIT License](LICENSE).
