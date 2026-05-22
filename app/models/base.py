from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy import Uuid
from app.db.session import Base
from app.models.mixins import AuditMixin
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base, AuditMixin):
    __tablename__ = "users"
    
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(String, default=UserRole.USER.value, nullable=False)
    
    items = relationship("Item", back_populates="owner")

class Item(Base, AuditMixin):
    __tablename__ = "items"
    
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    owner_id = Column(Uuid(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    owner = relationship("User", back_populates="items")
