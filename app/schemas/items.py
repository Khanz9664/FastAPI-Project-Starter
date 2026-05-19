from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID

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