from typing import Generic, TypeVar, Type, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
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

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100, search_field: Optional[str] = None, search_query: Optional[str] = None
    ) -> tuple[list[ModelType], int]:
        query = select(self.model)
        if hasattr(self.model, 'deleted_at'):
            query = query.where(self.model.deleted_at.is_(None))
            
        if search_field and search_query and hasattr(self.model, search_field):
            column = getattr(self.model, search_field)
            query = query.where(column.ilike(f"%{search_query}%"))
            
        # Count total
        count_query = select(func.count()).select_from(query.subquery())
        total = await db.scalar(count_query)
        
        # Paginate
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        items = list(result.scalars().all())
        
        return items, total or 0

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
