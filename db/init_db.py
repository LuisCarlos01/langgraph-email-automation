"""
Script para inicializar o banco de dados com as tabelas necessárias.
"""
from dotenv import load_dotenv
from db.database import engine
from db.models import Base

# Carrega as variáveis de ambiente
load_dotenv()

def init_database():
    print("Criando/atualizando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas/atualizadas com sucesso!")

if __name__ == "__main__":
    init_database() 