from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application Configuration
    PROJECT_NAME: str = "FastAPI Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Full-Featured FastAPI Project"
    API_PREFIX: str = "/api"
    
    # Database Configuration
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"
    
    # Security Configuration
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    class Config:
        case_sensitive = True

settings = Settings()
