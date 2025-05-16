# Reusable dependencies across routes
from .security import (
    get_current_user,
    oauth2_scheme,
    validate_admin_role
)

__all__ = ["get_current_user", "oauth2_scheme", "validate_admin_role"]
