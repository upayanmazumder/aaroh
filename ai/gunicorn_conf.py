import multiprocessing

# Gunicorn config for scalable deployment
workers = (multiprocessing.cpu_count() or 1) * 2 + 1
bind = "0.0.0.0:5000"
# Increase timeout for slow LLM calls
timeout = 120
# Log to stdout/stderr so container logs capture them
accesslog = "-"
errorlog = "-"
loglevel = "info"
