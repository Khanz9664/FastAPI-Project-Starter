from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class Item(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    owner_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
