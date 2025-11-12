"""Lightweight developer runner for the server package.

This file is intentionally small: use the `server.create_app()` factory for
production (gunicorn -> `server.wsgi:app`) and for tests. Running
`python app.py` will start the Flask dev server bound to 0.0.0.0.
"""

import os

from server import create_app


app = create_app()


def _run_dev():
    port = int(os.getenv("PORT", "5000"))
    debug = app.config.get("DEBUG", True)
    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    _run_dev()
