from dotenv import load_dotenv
from flask import Flask
from .extensions import init_extensions
from .routes import bp as api_bp
from .config import Config
import logging


def create_app() -> Flask:
    """Application factory for the Aaroh AI backend.

    Returns a configured Flask app instance. Use this in production (wsgi/gunicorn)
    and in development (import and call run).
    """
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Structured logger for the package
    logging.basicConfig(level=logging.INFO)
    app.logger = logging.getLogger("aaroh.ai")

    # Initialize extensions (CORS etc.) and register blueprints
    init_extensions(app)
    app.register_blueprint(api_bp)

    return app
