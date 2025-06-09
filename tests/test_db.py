import sys
import os
import pytest
from datetime import datetime, timezone
from uuid import uuid4

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import SessionLocal
from db.models import Email, EmailStatus
from db.crud import salvar_email, buscar_pendentes, atualizar_status, salvar_resposta_editada

@pytest.fixture
def db_session():
    """Fixture para fornecer uma sessão do banco de dados para os testes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(autouse=True)
def cleanup_database(db_session):
    """Fixture para limpar o banco de dados antes de cada teste."""
    db_session.query(Email).delete()
    db_session.commit()
    yield

def test_salvar_email(db_session):
    """Testa a função de salvar email no banco de dados."""
    # Cria um email de teste
    email = Email(
        id=str(uuid4()),
        remetente="teste@exemplo.com",
        assunto="Teste de Email",
        conteudo="Conteúdo do email de teste",
        resposta_gerada="Resposta gerada automaticamente",
        status=EmailStatus.PENDENTE,
        data_recebido=datetime.now(timezone.utc)
    )
    
    # Salva o email
    email_salvo = salvar_email(db_session, email)
    
    # Verifica se o email foi salvo corretamente
    assert email_salvo.id == email.id
    assert email_salvo.remetente == "teste@exemplo.com"
    assert email_salvo.status == EmailStatus.PENDENTE

def test_buscar_pendentes(db_session):
    """Testa a função de buscar emails pendentes."""
    # Cria alguns emails de teste com status diferentes
    emails = [
        Email(
            id=str(uuid4()),
            remetente=f"teste{i}@exemplo.com",
            assunto=f"Teste {i}",
            conteudo=f"Conteúdo {i}",
            resposta_gerada=f"Resposta {i}",
            status=EmailStatus.PENDENTE if i % 2 == 0 else EmailStatus.ENVIADO
        ) for i in range(4)
    ]
    
    # Salva os emails
    for email in emails:
        db_session.add(email)
    db_session.commit()
    
    # Busca emails pendentes
    pendentes = buscar_pendentes(db_session)
    
    # Verifica se apenas os emails pendentes foram retornados
    assert len(pendentes) == 2
    assert all(email.status == EmailStatus.PENDENTE for email in pendentes)

def test_atualizar_status(db_session):
    """Testa a função de atualizar o status de um email."""
    # Cria um email de teste
    email = Email(
        id=str(uuid4()),
        remetente="teste@exemplo.com",
        assunto="Teste de Atualização",
        conteudo="Conteúdo para atualização",
        resposta_gerada="Resposta inicial",
        status=EmailStatus.PENDENTE
    )
    
    # Salva o email
    db_session.add(email)
    db_session.commit()
    
    # Atualiza o status
    email_atualizado = atualizar_status(db_session, email.id, EmailStatus.ENVIADO)
    
    # Verifica se o status foi atualizado
    assert email_atualizado.status == EmailStatus.ENVIADO

def test_salvar_resposta_editada(db_session):
    """Testa a função de salvar uma resposta editada."""
    # Cria um email de teste
    email = Email(
        id=str(uuid4()),
        remetente="teste@exemplo.com",
        assunto="Teste de Resposta",
        conteudo="Conteúdo para resposta",
        resposta_gerada="Resposta inicial",
        status=EmailStatus.PENDENTE
    )
    
    # Salva o email
    db_session.add(email)
    db_session.commit()
    
    # Salva uma resposta editada
    nova_resposta = "Nova resposta editada"
    email_atualizado = salvar_resposta_editada(db_session, email.id, nova_resposta)
    
    # Verifica se a resposta foi atualizada e o status mudou
    assert email_atualizado.resposta_editada == nova_resposta
    assert email_atualizado.status == EmailStatus.ENVIADO

def test_email_nao_encontrado(db_session):
    """Testa o comportamento quando um email não é encontrado."""
    # Tenta atualizar um email que não existe
    email_id_inexistente = str(uuid4())
    
    # Verifica se as funções retornam None para IDs inexistentes
    assert atualizar_status(db_session, email_id_inexistente, EmailStatus.ENVIADO) is None
    assert salvar_resposta_editada(db_session, email_id_inexistente, "Teste") is None 