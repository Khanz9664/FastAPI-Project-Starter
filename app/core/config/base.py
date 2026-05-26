import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Full-Featured FastAPI Project"
    API_PREFIX: str = "/api/v1"

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # Rate Limiting
    AUTH_RATE_LIMIT: str = "5/minute"
    DEFAULT_RATE_LIMIT: str = "10/minute"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env", extra="ignore")
