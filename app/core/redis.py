import json
from typing import Any, Optional

from redis.asyncio import Redis


class RedisClient:
    def __init__(self):
        self.redis: Optional[Redis] = None

    async def connect(self, url: str):
        self.redis = Redis.from_url(url, decode_responses=True)

    async def disconnect(self):
        if self.redis:
            await self.redis.close()

    async def set_cache(self, key: str, value: Any, expire: int = 3600):
        if self.redis:
            await self.redis.set(key, json.dumps(value), ex=expire)

    async def get_cache(self, key: str) -> Optional[Any]:
        if self.redis:
            val = await self.redis.get(key)
            if val:
                return json.loads(val)
        return None

    async def delete_cache(self, key: str):
        if self.redis:
            await self.redis.delete(key)


redis_client = RedisClient()
