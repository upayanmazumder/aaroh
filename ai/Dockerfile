# Stage 1 — dependencies
FROM python:3.11-slim AS base
WORKDIR /ai

# caching pip packages separately
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2 — final
FROM python:3.11-slim AS runner
WORKDIR /ai

COPY --from=base /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=base /usr/local/bin /usr/local/bin
COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["python", "main.py"]
