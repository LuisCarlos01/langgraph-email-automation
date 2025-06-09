"""
Ponto de entrada para a API FastAPI.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import routes
from db.database import engine
from db.models import Base

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="iPassResponder API",
    description="API para automação de respostas de email usando IA",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas da API
app.include_router(routes.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("run_api:app", host="0.0.0.0", port=8000, reload=True) 