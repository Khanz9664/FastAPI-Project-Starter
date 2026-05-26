from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRole(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "jane.doe@example.com", "password": "SuperSecretPassword123!", "full_name": "Jane Doe"}
        }
    )


class WelcomeEmailPayload(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None


class User(BaseModel):
    id: UUID
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
