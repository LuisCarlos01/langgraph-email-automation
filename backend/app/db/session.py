from .database import get_async_engine, get_async_session, get_db

# Create a single engine instance for the application
engine = get_async_engine()

# Factory for creating async sessions
AsyncSessionLocal = get_async_session()

__all__ = ["engine", "AsyncSessionLocal", "get_db"]
