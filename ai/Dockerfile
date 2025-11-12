FROM python:3.11-slim

# Use a dedicated working directory
WORKDIR /app

# Prevent python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies first (keeps layer cache stable when code changes)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app sources
COPY . .

# Runtime port
ENV PORT=5000
EXPOSE 5000

# Use the actual entrypoint file in this folder
CMD ["python", "app.py"]
