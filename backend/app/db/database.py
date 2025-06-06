from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# URL síncrona para o Alembic
SYNC_DATABASE_URL = settings.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://")

# Engine síncrono para o Alembic
sync_engine = create_engine(
    SYNC_DATABASE_URL,
    echo=settings.DB_ECHO,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW
)

# Base para os modelos
Base = declarative_base()

# Função para criar o engine assíncrono
def get_async_engine():
    return create_async_engine(
        settings.DATABASE_URL,
        echo=settings.DB_ECHO,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW
    )

# Função para criar a sessão assíncrona
def get_async_session():
    engine = get_async_engine()
    return sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

# Dependency para injeção da sessão do banco
async def get_db():
    async_session = get_async_session()
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close() 