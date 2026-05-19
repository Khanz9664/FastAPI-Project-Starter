from typing import Generic, TypeVar, Type, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_id(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == id)
        if hasattr(self.model, 'deleted_at'):
            query = query.where(self.model.deleted_at.is_(None))
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, obj_in: dict) -> ModelType:
        obj = self.model(**obj_in)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    async def delete(self, db: AsyncSession, id: Any) -> bool:
        obj = await self.get_by_id(db, id)
        if obj:
            if hasattr(self.model, 'deleted_at'):
                from app.models.mixins import utc_now
                obj.deleted_at = utc_now()
            else:
                await db.delete(obj)
            await db.commit()
            return True
        return False
