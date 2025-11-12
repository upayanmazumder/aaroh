from flask_cors import CORS
import os

# Create the extension instance(s) here to avoid circular imports
cors = CORS()


def init_extensions(app):
    """Initializes Flask extensions and third-party integrations."""
    allowed = os.getenv(
        "AAROH_ALLOWED_ORIGINS", "http://localhost:3000,https://aaroh.upayan.dev"
    )
    origins = [o.strip() for o in allowed.split(",") if o.strip()]
    # Configure CORS with explicit origins to avoid open policies
    cors.init_app(app, origins=origins, supports_credentials=True)
