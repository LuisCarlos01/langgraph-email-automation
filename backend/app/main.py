from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import emails, respostas, regras
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

# Inicializa o banco de dados
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

# Configuração avançada do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
    expose_headers=["X-Total-Count"],  # Expõe header para paginação
    max_age=3600,  # Cache preflight por 1 hora
)

# Inclusão dos routers
app.include_router(emails.router, prefix="/api/v1", tags=["emails"])
app.include_router(respostas.router, prefix="/api/v1", tags=["respostas"])
app.include_router(regras.router, prefix="/api/v1", tags=["regras"])

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return {"message": "iPass Email Automation API"} 