from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, items
from app.core.config import settings
from fastapi import APIRouter
from app.database import Base, engine
import asyncio

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix=settings.API_PREFIX)
app.include_router(items.router, prefix=settings.API_PREFIX)

@app.get(f"{settings.API_PREFIX}/")
async def read_main():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_db():
    """Initialize database connection and create tables on startup"""
    # Create tables if they do not exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    """Close database connection on shutdown"""
    await database.disconnect()
