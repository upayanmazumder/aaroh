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

# Use gunicorn in production for better concurrency and process management.
# The container will run gunicorn with the Python module `app:app` and the
# configuration in `gunicorn_conf.py`.
CMD ["gunicorn", "wsgi:app", "-c", "gunicorn_conf.py"]
