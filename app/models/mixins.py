import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Uuid


def utc_now():
    return datetime.now(timezone.utc)


class AuditMixin:
    """Provides UUID primary key and standard audit fields for all models."""

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    deleted_at = Column(DateTime(timezone=True), nullable=True, index=True)

    # In a full RBAC system, these would be ForeignKeys, but Uuid is fine for tracking
    created_by = Column(Uuid(as_uuid=True), nullable=True)
    updated_by = Column(Uuid(as_uuid=True), nullable=True)
