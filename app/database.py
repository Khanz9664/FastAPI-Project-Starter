from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Async SQLAlchemy setup
engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True  # Remove in production
)

AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    """Async database session dependency"""
    async with AsyncSessionLocal() as session:
        yield session
