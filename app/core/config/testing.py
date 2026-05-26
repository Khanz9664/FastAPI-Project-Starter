from .base import BaseConfig


class TestingConfig(BaseConfig):
    ENVIRONMENT: str = "testing"
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"  # Use SQLite for quick tests, or test PostgreSQL
    SECRET_KEY: str = "test-secret-key"
