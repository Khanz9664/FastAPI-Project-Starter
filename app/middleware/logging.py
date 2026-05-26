import json
import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(message)s"))
if not logger.handlers:
    logger.addHandler(handler)


class StructuredLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        duration = f"{process_time * 1000:.2f}ms"

        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration": duration,
        }

        logger.info(json.dumps(log_data))
        return response
