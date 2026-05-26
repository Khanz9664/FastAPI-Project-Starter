from typing import Optional

from fastapi import Query
from pydantic import BaseModel


class PaginationParams(BaseModel):
    skip: int = Query(0, ge=0, description="Number of records to skip")
    limit: int = Query(20, ge=1, le=100, description="Number of records to return (max 100)")
    sort_by: str = Query("created_at", description="Field to sort by")
    sort_order: str = Query("desc", pattern="^(asc|desc)$", description="Sort order (asc or desc)")
