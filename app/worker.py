import asyncio
from typing import Any
from arq.connections import RedisSettings
from app.core.config import settings

async def dummy_background_task(ctx: dict, user_email: str) -> str:
    """
    Dummy background task to simulate sending an email or processing data.
    """
    print(f"Starting background processing for user: {user_email}")
    await asyncio.sleep(2)  # Simulate network or processing delay
    print(f"Finished processing for user: {user_email}")
    return f"Processed {user_email}"

async def startup(ctx: dict):
    print("Worker starting up...")

async def shutdown(ctx: dict):
    print("Worker shutting down...")

class WorkerSettings:
    functions = [dummy_background_task]
    redis_settings = RedisSettings.from_dsn(settings.REDIS_URL)
    on_startup = startup
    on_shutdown = shutdown
