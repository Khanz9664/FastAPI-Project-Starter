from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    error_code: Optional[str] = None


class PaginationMeta(BaseModel):
    total: int
    skip: int
    limit: int
    has_next: bool


class PaginatedData(BaseModel, Generic[T]):
    items: list[T]
    pagination: PaginationMeta


class PaginatedResponse(APIResponse[PaginatedData[T]]):
    pass
