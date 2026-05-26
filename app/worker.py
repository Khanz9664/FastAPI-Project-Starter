import asyncio
from typing import Any

from arq.connections import RedisSettings

from app.core.config import settings
from app.schemas.users import WelcomeEmailPayload


async def send_welcome_email_task(ctx: dict, payload: WelcomeEmailPayload) -> str:
    """
    Background task to simulate sending a welcome email.
    """
    print(f"Starting welcome email job for user: {payload.email}")
    await asyncio.sleep(2)  # Simulate network or processing delay
    print(f"Successfully sent welcome email to: {payload.email}")
    return f"Processed {payload.email}"


async def startup(ctx: dict):
    print("Worker starting up...")


async def shutdown(ctx: dict):
    print("Worker shutting down...")


class WorkerSettings:
    functions = [send_welcome_email_task]
    redis_settings = RedisSettings.from_dsn(settings.REDIS_URL)
    on_startup = startup
    on_shutdown = shutdown
    max_tries = 3
