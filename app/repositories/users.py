from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import User

from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    async def get_by_email(self, db: AsyncSession, email: str) -> Optional[User]:
        query = select(User).where(User.email == email, User.deleted_at.is_(None))
        result = await db.execute(query)
        return result.scalar_one_or_none()


user_repo = UserRepository()
