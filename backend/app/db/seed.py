"""Script para popular o banco de dados com dados de teste."""
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.models import Email, Response, Rule, EmailStatus

async def seed_database(db: AsyncSession) -> None:
    """Popula o banco de dados com dados de teste."""
    
    # Criando regras de exemplo
    rules = [
        Rule(
            palavra_chave="orçamento",
            resposta_customizada="Obrigado pelo seu interesse! Nossos preços começam a partir de R$ 1.000,00.",
            ativo=True
        ),
        Rule(
            palavra_chave="suporte",
            resposta_customizada="Nossa equipe de suporte está disponível 24/7. Como podemos ajudar?",
            ativo=True
        ),
        Rule(
            palavra_chave="reunião",
            resposta_customizada="Para agendar uma reunião, por favor acesse: calendly.com/ipass",
            ativo=True
        )
    ]
    
    for rule in rules:
        db.add(rule)
    
    # Criando emails de exemplo
    emails = [
        Email(
            subject="Solicitação de Orçamento",
            sender="cliente@empresa.com",
            recipient="contato@ipass.com.br",
            content="Gostaria de receber um orçamento dos serviços de automação.",
            status=EmailStatus.PENDING
        ),
        Email(
            subject="Problema Técnico",
            sender="usuario@startup.com",
            recipient="suporte@ipass.com.br",
            content="Estou com dificuldades para acessar o sistema.",
            status=EmailStatus.PROCESSING
        ),
        Email(
            subject="Agendamento de Reunião",
            sender="parceiro@tech.com",
            recipient="comercial@ipass.com.br",
            content="Podemos marcar uma reunião para discutir a parceria?",
            status=EmailStatus.COMPLETED
        )
    ]
    
    for email in emails:
        db.add(email)
    
    # Primeiro commit para obter os IDs
    await db.commit()
    
    # Criando respostas de exemplo
    responses = [
        Response(
            email_id=emails[0].id,
            content="Claro! Nossos preços variam de acordo com o volume. Vou preparar uma proposta detalhada.",
            generated_by_ai=True
        ),
        Response(
            email_id=emails[1].id,
            content="Por favor, tente limpar o cache do navegador e tentar novamente. Se o problema persistir, me avise.",
            generated_by_ai=True
        ),
        Response(
            email_id=emails[2].id,
            content="Ótimo! Podemos nos reunir amanhã às 14h? Vou enviar o link do Zoom.",
            generated_by_ai=False
        )
    ]
    
    for response in responses:
        db.add(response)
    
    # Commit final
    await db.commit() 