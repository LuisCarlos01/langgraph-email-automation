from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models import Email, EmailStatus
import numpy as np

def salvar_email(db: Session, email: Email):
    db.add(email)
    db.commit()
    db.refresh(email)
    return email

def buscar_pendentes(db: Session):
    return db.query(Email).filter(Email.status == EmailStatus.PENDENTE).all()

def atualizar_status(db: Session, email_id: str, novo_status: EmailStatus):
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        email.status = novo_status
        db.commit()
        db.refresh(email)
    return email

def salvar_resposta_editada(db: Session, email_id: str, resposta: str):
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        email.resposta_editada = resposta
        email.status = EmailStatus.ENVIADO
        db.commit()
        db.refresh(email)
    return email

def salvar_embedding(db: Session, email_id: str, embedding: list):
    """
    Salva o embedding de um e-mail no banco de dados.
    """
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        email.embedding = embedding
        db.commit()
        db.refresh(email)
    return email

def buscar_similares(db: Session, query_embedding: list, limit: int = 3):
    """
    Busca os e-mails mais similares baseado no embedding da consulta.
    Usa o produto escalar (dot product) para calcular a similaridade.
    """
    # Converte o embedding da consulta para um array numpy
    query_embedding = np.array(query_embedding)
    
    # Busca todos os e-mails com embedding
    emails = db.query(Email).filter(
        Email.status == EmailStatus.ENVIADO,
        Email.embedding.isnot(None)
    ).all()
    
    # Calcula a similaridade usando produto escalar
    similarities = []
    for email in emails:
        if email.embedding:
            similarity = np.dot(query_embedding, email.embedding)
            similarities.append((email, similarity))
    
    # Ordena por similaridade e retorna os top N
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [email for email, _ in similarities[:limit]]
