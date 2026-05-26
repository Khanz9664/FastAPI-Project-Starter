from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps.security import RoleChecker, get_current_user
from app.core.config import settings
from app.core.limiter import limiter
from app.db.session import get_db
from app.models.base import User
from app.schemas.common import APIResponse
from app.schemas.users import Token
from app.schemas.users import User as UserSchema
from app.schemas.users import UserCreate, UserRole, WelcomeEmailPayload
from app.utils.password import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=APIResponse[UserSchema])
@limiter.limit(settings.AUTH_RATE_LIMIT)
async def create_user(request: Request, user: UserCreate, db: AsyncSession = Depends(get_db)):
    """Create new user"""
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, full_name=user.full_name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    # Enqueue background task (e.g., welcome email)
    if hasattr(request.app.state, "arq_pool"):
        payload = WelcomeEmailPayload(email=db_user.email, full_name=db_user.full_name)
        await request.app.state.arq_pool.enqueue_job("send_welcome_email_task", payload)

    return APIResponse(
        success=True,
        message="User created successfully",
        data=UserSchema.model_validate(db_user),
    )


@router.get("/me", response_model=APIResponse[UserSchema])
async def read_user_me(current_user: User = Depends(get_current_user)):
    """Get current user"""
    return APIResponse(
        success=True,
        message="Current user retrieved successfully",
        data=UserSchema.model_validate(current_user),
    )


@router.get("/admin", response_model=APIResponse[dict])
async def admin_only_route(current_user: User = Depends(RoleChecker([UserRole.ADMIN]))):
    """Test endpoint for RBAC admin access"""
    return APIResponse(success=True, message="Admin access granted", data={"user": current_user.email})
