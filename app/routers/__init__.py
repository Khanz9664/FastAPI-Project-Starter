# Centralize router imports
from .users import router as users_router
from .items import router as items_router

# List of all routers (used in main.py)
routers = [users_router, items_router]

__all__ = ["routers", "users_router", "items_router"]
