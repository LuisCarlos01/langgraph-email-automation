"""
Script para inicializar o banco de dados com as tabelas necessárias.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models import Base

# Carrega as variáveis de ambiente
load_dotenv()

def init_database():
    # Obtém a URL do banco de dados
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL não encontrada nas variáveis de ambiente")

    print(f"Conectando ao banco de dados: {database_url}")
    engine = create_engine(database_url)
    
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_database() 