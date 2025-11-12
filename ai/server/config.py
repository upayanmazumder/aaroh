import os


class Config:
    """Simple configuration object reading from environment variables."""

    PORT = int(os.getenv("PORT", "5000"))
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    AAROH_ALLOWED_ORIGINS = os.getenv(
        "AAROH_ALLOWED_ORIGINS", "http://localhost:3000,https://aaroh.upayan.dev"
    )
