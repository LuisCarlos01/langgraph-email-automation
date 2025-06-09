import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dotenv import load_dotenv
from .models import Base

load_dotenv()

POSTGRES_URL = os.getenv("DATABASE_URL")

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(bind=engine)
