from .base import BaseConfig


class ProductionConfig(BaseConfig):
    ENVIRONMENT: str = "production"
    # Ensure these are provided by the actual production environment variables
    # Defaults here are merely placeholders to satisfy strict Pydantic checks if not provided during class definition
    DATABASE_URL: str = ""
    SECRET_KEY: str = ""
