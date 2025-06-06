"""CLI para gerenciamento do banco de dados."""
import asyncio
import typer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_async_session
from app.db.seed import seed_database

app = typer.Typer()

async def get_db_session() -> AsyncSession:
    """Retorna uma sessão do banco de dados."""
    session_factory = get_async_session()
    async with session_factory() as session:
        yield session

@app.command()
def seed():
    """Popula o banco de dados com dados de teste."""
    typer.echo("Populando banco de dados...")
    
    async def run_seed():
        async for session in get_db_session():
            await seed_database(session)
    
    asyncio.run(run_seed())
    typer.echo("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    app() 