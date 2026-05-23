from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.db.session import get_db
from app.repositories.items import item_repo
from app.schemas.items import Item as ItemSchema
from app.schemas.common import PaginatedResponse, PaginatedData
from app.api.deps.pagination import PaginationParams

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=PaginatedResponse[ItemSchema])
async def list_items(
    pagination: PaginationParams = Depends(),
    search: Optional[str] = Query(None, description="Search items by title"),
    db: AsyncSession = Depends(get_db)
):
    """Return a paginated list of items"""
    items, total = await item_repo.get_multi(
        db, 
        skip=pagination.skip, 
        limit=pagination.limit,
        search_field="title",
        search_query=search
    )
    
    return PaginatedResponse(
        success=True,
        message="Items retrieved successfully",
        data=PaginatedData(
            items=[ItemSchema.model_validate(item) for item in items],
            total=total,
            skip=pagination.skip,
            limit=pagination.limit
        )
    ) 