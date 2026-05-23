from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    error_code: Optional[str] = None

class PaginatedData(BaseModel, Generic[T]):
    items: list[T]
    total: int
    skip: int
    limit: int

class PaginatedResponse(APIResponse[PaginatedData[T]]):
    pass
