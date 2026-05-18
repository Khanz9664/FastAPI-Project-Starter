from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.api.v1 import users, items, auth
from app.core.config import settings
from app.db.session import Base, engine, connect, disconnect
from app.middleware.logging import StructuredLoggingMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan manager to handle startup and shutdown events."""
    # We will remove create_all in Phase 2 when setting up Alembic.
    # For Phase 1, we still ensure the DB connects.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await connect()
    yield
    await disconnect()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    lifespan=lifespan
)

# Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": str(exc), "error_code": "INTERNAL_SERVER_ERROR"}
    )


# Middlewares
app.add_middleware(StructuredLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(users.router, prefix=settings.API_PREFIX)
app.include_router(items.router, prefix=settings.API_PREFIX)

@app.get(f"{settings.API_PREFIX}/")
async def read_main():
    return {"success": True, "message": "Hello World"}

