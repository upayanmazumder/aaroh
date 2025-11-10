# Aaroh — The Ascent of Understanding

[![AI Build](https://img.shields.io/github/actions/workflow/status/upayanmazumder/aaroh/ai.yml?label=AI%20Service&style=for-the-badge&logo=python&logoColor=white)](https://github.com/upayanmazumder/aaroh/actions/workflows/ai.yml)
[![API Build](https://img.shields.io/github/actions/workflow/status/upayanmazumder/aaroh/api.yml?label=API%20Backend&style=for-the-badge&logo=node.js&logoColor=white)](https://github.com/upayanmazumder/aaroh/actions/workflows/api.yml)
[![App Build](https://img.shields.io/github/actions/workflow/status/upayanmazumder/aaroh/app.yml?label=Next.js%20App&style=for-the-badge&logo=next.js&logoColor=white)](https://github.com/upayanmazumder/aaroh/actions/workflows/app.yml)

[![License: MIT](https://img.shields.io/github/license/upayanmazumder/aaroh?style=for-the-badge&logo=mit&logoColor=white)](https://github.com/upayanmazumder/aaroh/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/upayanmazumder/aaroh?style=for-the-badge&logo=github&logoColor=white)](https://github.com/upayanmazumder/aaroh/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/upayanmazumder/aaroh?style=for-the-badge&logo=github&logoColor=white)](https://github.com/upayanmazumder/aaroh/network/members)
[![Issues](https://img.shields.io/github/issues/upayanmazumder/aaroh?style=for-the-badge&logo=github&logoColor=white)](https://github.com/upayanmazumder/aaroh/issues)
[![Contributors](https://img.shields.io/github/contributors/upayanmazumder/aaroh?style=for-the-badge&logo=github&logoColor=white)](https://github.com/upayanmazumder/aaroh/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/upayanmazumder/aaroh?style=for-the-badge&logo=github&logoColor=white)](https://github.com/upayanmazumder/aaroh/commits/main)

**Aaroh** is an AI-powered learning assistant that helps students move beyond rote memorization toward true comprehension.  
It breaks down complex academic text into **simplified explanations**, **relatable analogies**, and **auto-generated quizzes**, making learning engaging and accessible.

Built for the **Viksit Bharat Challenge** by **Team Runtime Terror**, Aaroh aims to democratize education by making complex knowledge simple and inclusive — for every learner, in every language.

---

## Overview

### The Problem

Students often struggle to grasp dense academic material, leading to surface-level understanding and dependence on memorization. Traditional educational resources are static and fail to adapt to individual learning needs.

### The Solution

Aaroh provides a dynamic, AI-driven solution that allows a student to paste any complex academic text and instantly receive:

- A simplified version of the content.
- A real-world analogy to make the concept intuitive.
- An auto-generated quiz to test comprehension.
- Multilingual support for inclusivity.

By transforming passive reading into active understanding, Aaroh fosters curiosity, confidence, and critical thinking.

---

## Tech Stack

- **Frontend:** Next.js (TypeScript, pnpm)
- **Backend:** Express.js (Node.js, pnpm)
- **AI Service:** Python (Flask + LLM integration)
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions (build and push caching)

---

## Folder Structure

```

.
├── app/         # Next.js frontend (UI for text input and quiz display)
│   └── Dockerfile
├── api/         # Express backend (routes + middleware)
│   └── Dockerfile
├── ai/          # Flask microservice (AI-powered text simplification, analogy, quiz generation)
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── pnpm-workspace.yaml

```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/upayanmazumder/aaroh.git
cd aaroh
```

### Run with Docker

Build and start all services:

```bash
docker compose up --build
```

Then open:

- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **API:** [http://localhost:4000](http://localhost:4000)
- **AI Service:** [http://localhost:5000](http://localhost:5000)

---

## How It Works

1. The **frontend** (Next.js) provides a simple interface for students to input text.
2. The **backend** (Express) receives the text and forwards it to the AI service.
3. The **AI service** (Flask) processes the input using language models to:
   - Simplify complex concepts.
   - Generate analogies for better recall.
   - Create short quizzes to test understanding.

4. The processed output is sent back through the backend and displayed in the UI.

---

## Example Flow

1. User submits text to `/api/learn`.
2. The Express backend routes it to the Flask endpoint `/process`.
3. Flask AI module generates a simplified explanation, analogy, and quiz.
4. The processed result is displayed on the web app.

---

## Docker Compose Overview

| Service | Port | Description           |
| ------- | ---- | --------------------- |
| `app`   | 3000 | Next.js frontend      |
| `api`   | 4000 | Express backend       |
| `ai`    | 5000 | Flask AI microservice |

Each container is modular, isolated, and deployable independently.

---

## Development Notes

- Uses `pnpm` for dependency management.
- Python virtual environments are handled through Docker.
- GitHub Actions workflow supports build caching for faster CI/CD.
- Easily extensible with additional services (databases, vector stores, etc.).

---

## Future Scope

- Integrate production-grade LLMs (OpenAI, HuggingFace, Ollama).
- Add multilingual voice input and output.
- Introduce user analytics and adaptive learning.
- Expand inclusivity through support for regional languages.
- Deploy to cloud providers (Fly.io, Railway, Render, etc.).

---

## Vision

To make learning **simple, personalized, and empowering** — cultivating thinkers, not memorizers.

---

## License

Licensed under the [MIT License](LICENSE).
