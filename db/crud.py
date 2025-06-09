from sqlalchemy.orm import Session
from .models import Email, EmailStatus

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
