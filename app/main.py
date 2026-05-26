from contextlib import asynccontextmanager

from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
from slowapi.errors import RateLimitExceeded
from sqlalchemy import text
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1 import auth, items, users
from app.core.config import settings
from app.core.limiter import limiter
from app.core.redis import redis_client
from app.db.session import Base, connect, disconnect, engine
from app.middleware.logging import StructuredLoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan manager to handle startup and shutdown events."""
    await connect()
    await redis_client.connect(settings.REDIS_URL)
    app.state.arq_pool = await create_pool(RedisSettings.from_dsn(settings.REDIS_URL))
    yield
    await redis_client.disconnect()
    await app.state.arq_pool.close()
    await disconnect()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="""
    A production-ready FastAPI boilerplate featuring:
    * **Async PostgreSQL** database operations
    * **Redis** caching and **ARQ** background workers
    * **JWT Authentication** and **RBAC**
    * **Pagination** and generic repositories
    """,
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    contact={
        "name": "Shahid Ul Islam",
        "url": "https://khanz9664.github.io/portfolio/",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {"name": "auth", "description": "Authentication and JWT issuance operations."},
        {"name": "users", "description": "User management and Role-Based Access Control (RBAC)."},
        {"name": "items", "description": "Generic items management demonstrating pagination and search."},
    ],
    lifespan=lifespan,
)

app.state.limiter = limiter


# Exception Handlers
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "success": False,
            "message": "Too many requests",
            "error_code": "RATE_LIMIT_EXCEEDED",
        },
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": str(exc.detail),
            "error_code": f"HTTP_{exc.status_code}",
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "data": exc.errors(),
            "error_code": "VALIDATION_ERROR",
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "error_code": "INTERNAL_SERVER_ERROR",
        },
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

# Prometheus Metrics
Instrumentator().instrument(app).expose(app, include_in_schema=True, tags=["observability"])

# Include routers
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(users.router, prefix=settings.API_PREFIX)
app.include_router(items.router, prefix=settings.API_PREFIX)


@app.get(f"{settings.API_PREFIX}/")
@limiter.limit(settings.DEFAULT_RATE_LIMIT)
async def read_main(request: Request):
    return {"success": True, "message": "Hello World"}


@app.get("/health", tags=["observability"])
async def health_check():
    """Health check endpoint to verify infrastructure components."""
    status = {"status": "healthy", "services": {"database": "ok", "redis": "ok"}}

    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception:
        status["services"]["database"] = "failed"
        status["status"] = "unhealthy"

    try:
        if not redis_client.redis or not await redis_client.redis.ping():
            raise Exception("Redis not responding")
    except Exception:
        status["services"]["redis"] = "failed"
        status["status"] = "unhealthy"

    return JSONResponse(status_code=200 if status["status"] == "healthy" else 503, content=status)


@app.get("/live", tags=["observability"])
async def liveness_probe():
    """Kubernetes liveness probe. Indicates if the application is running."""
    return {"status": "alive"}


@app.get("/ready", tags=["observability"])
async def readiness_probe():
    """Kubernetes readiness probe. Same as /health but used by orchestration."""
    return await health_check()
