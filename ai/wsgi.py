"""WSGI entrypoint used by Gunicorn in production.

Expose the `app` variable which is the Flask application instance created by
the factory in `server.create_app()`.
"""

from server import create_app


app = create_app()
