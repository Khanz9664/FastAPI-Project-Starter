from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"
    SECRET_KEY: str = "dev-secret-key-do-not-use-in-production"
