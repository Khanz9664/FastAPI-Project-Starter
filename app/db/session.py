from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# Async SQLAlchemy setup
engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)  # Remove in production

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    """Async database session dependency"""
    async with AsyncSessionLocal() as session:
        yield session


async def connect():
    """Establish a connection to the database (dummy for SQLAlchemy async)."""
    # SQLAlchemy async engine does not require explicit connect, but you can test connection here if needed
    async with engine.begin() as conn:
        pass


async def disconnect():
    """Dispose of the database engine."""
    await engine.dispose()
