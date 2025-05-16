# Export core components for easy access
__all__ = ["app", "settings", "database"]

# Optional: Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Import critical components (optional)
from .main import app
from .core.config import settings
from .database import engine, Base
