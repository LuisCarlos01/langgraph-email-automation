from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List

from backend.app.db.database import get_db
from backend.app.db.models.models import Resposta, Email
from backend.app.schemas.schemas import RespostaCreate, Resposta as RespostaSchema
from backend.app.schemas.filters import RespostaFilter

router = APIRouter()

@router.post("/respostas/", response_model=RespostaSchema, status_code=status.HTTP_201_CREATED)
def create_resposta(resposta: RespostaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova resposta para um email.
    """
    # Verifica se o email existe
    email = db.query(Email).filter(Email.id == resposta.email_id).first()
    if not email:
        raise HTTPException(status_code=404, detail="Email não encontrado")

    db_resposta = Resposta(
        email_id=resposta.email_id,
        corpo_resposta=resposta.corpo_resposta,
        gerada_por_ia=resposta.gerada_por_ia
    )
    db.add(db_resposta)
    
    # Marca o email como respondido
    email.respondido = True
    
    db.commit()
    db.refresh(db_resposta)
    return db_resposta

@router.get("/respostas/", response_model=List[RespostaSchema])
def list_respostas(
    response: Response,
    filtros: RespostaFilter = Depends(),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Lista todas as respostas com filtros avançados e paginação.
    """
    query = db.query(Resposta)

    # Aplicar filtros
    if filtros.email_id:
        query = query.filter(Resposta.email_id == filtros.email_id)
    
    if filtros.gerada_por_ia is not None:
        query = query.filter(Resposta.gerada_por_ia == filtros.gerada_por_ia)
    
    if filtros.data_inicio:
        query = query.filter(Resposta.data_envio >= filtros.data_inicio)
    
    if filtros.data_fim:
        query = query.filter(Resposta.data_envio <= filtros.data_fim)
    
    # Ordenação
    ordem_func = desc if filtros.ordem == "desc" else asc
    if hasattr(Resposta, filtros.ordenar_por):
        query = query.order_by(ordem_func(getattr(Resposta, filtros.ordenar_por)))

    # Contagem total para paginação
    total = query.count()
    response.headers["X-Total-Count"] = str(total)
    
    # Aplicar paginação
    respostas = query.offset(skip).limit(limit).all()
    return respostas

@router.get("/respostas/email/{email_id}", response_model=List[RespostaSchema])
def get_respostas_by_email(
    email_id: int,
    response: Response,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Obtém todas as respostas de um email específico com paginação.
    """
    query = db.query(Resposta).filter(Resposta.email_id == email_id)
    
    # Contagem total
    total = query.count()
    if total == 0:
        raise HTTPException(status_code=404, detail="Nenhuma resposta encontrada para este email")
    
    response.headers["X-Total-Count"] = str(total)
    respostas = query.offset(skip).limit(limit).all()
    return respostas

@router.get("/respostas/{resposta_id}", response_model=RespostaSchema)
def get_resposta(resposta_id: int, db: Session = Depends(get_db)):
    """
    Obtém uma resposta específica pelo ID.
    """
    resposta = db.query(Resposta).filter(Resposta.id == resposta_id).first()
    if resposta is None:
        raise HTTPException(status_code=404, detail="Resposta não encontrada")
    return resposta 