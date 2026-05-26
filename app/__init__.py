# Export core components for easy access
__all__ = ["app", "settings", "database"]

# Optional: Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

from .core.config import settings
from .db.session import Base, engine

# Import critical components (optional)
from .main import app
