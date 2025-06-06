import asyncio
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import Generator, AsyncGenerator

from app.main import app
from app.db.base import Base
from app.core.config import settings
from app.db.session import get_db

# Usar banco de dados de teste
TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/test_ipass_email_db"

engine_test = create_async_engine(TEST_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    engine_test, 
    class_=AsyncSession, 
    expire_on_commit=False
)

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_db_setup():
    """Setup test database."""
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def db_session(test_db_setup) -> AsyncGenerator[AsyncSession, None]:
    """Get async database session for tests."""
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture
async def client(db_session) -> Generator:
    """Get test client with overridden dependencies."""
    async def override_get_db():
        try:
            yield db_session
        finally:
            await db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear() 