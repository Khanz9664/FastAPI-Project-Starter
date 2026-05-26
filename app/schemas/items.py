from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Machine Learning Model Pipeline",
                "description": "A robust automated pipeline for training and deploying XGBoost models.",
            }
        }
    )


class ItemUpdate(ItemBase):
    title: Optional[str] = None

    model_config = ConfigDict(json_schema_extra={"example": {"title": "Updated ML Pipeline"}})
    description: Optional[str] = None


class Item(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    owner_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
