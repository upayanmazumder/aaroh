# Aaroh — AI backend

This folder contains the Flask-based backend for Project Aaroh. It exposes a /simplify endpoint that accepts JSON {"text": "..."} and returns a simplified explanation plus a short quiz.

Key points

- Runs on port 5000 by default (env PORT)
- CORS is enabled and configurable via AAROH_ALLOWED_ORIGINS (comma-separated list). Defaults: http://localhost:3000,https://aaroh.upayan.dev
- Production server uses gunicorn with `gunicorn_conf.py` for worker sizing and timeouts

Local development

1. Create a virtualenv and install deps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the app in dev mode:

```powershell
#$env:PORT = "5000"
#(optional) set allowed origins
#$env:AAROH_ALLOWED_ORIGINS = "http://localhost:3000,https://aaroh.upayan.dev"
python app.py
```

Docker / Production

Build the image from the `ai` directory (the Dockerfile installs requirements):

```powershell
docker build -t aaroh-ai:latest .
docker run -p 5000:5000 -e AAROH_ALLOWED_ORIGINS="http://localhost:3000,https://aaroh.upayan.dev" aaroh-ai:latest
```

Notes

- For orchestration in production, use your orchestrator (docker-compose, k8s, ECS) and attach a load balancer.
- The gunicorn config uses (2\*CPU + 1) workers and a 120s timeout to tolerate slower LLM calls.
- Health endpoint: GET /health returns {"status":"ok"} for probes.

Environment variables

- PORT: port to bind (default 5000)
- AAROH_ALLOWED_ORIGINS: comma-separated list of allowed CORS origins
- FLASK_DEBUG: set to 1 to enable Flask debug server when running `python app.py`

If you want, I can also add a small docker-compose service or Kubernetes manifest next.
