from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import UserCreate, User as UserSchema, Token
from app.schemas.common import APIResponse
from app.models.base import User
from app.db.session import get_db
from app.api.deps.security import get_current_user
from app.utils.password import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=APIResponse[UserSchema])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """Create new user"""
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, full_name=user.full_name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return APIResponse(
        success=True,
        message="User created successfully",
        data=UserSchema.model_validate(db_user)
    )

@router.get("/me", response_model=APIResponse[UserSchema])
async def read_user_me(current_user: User = Depends(get_current_user)):
    """Get current user"""
    return APIResponse(
        success=True,
        message="Current user retrieved successfully",
        data=UserSchema.model_validate(current_user)
    )
