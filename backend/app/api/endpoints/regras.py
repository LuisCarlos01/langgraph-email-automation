from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List

from app.db.database import get_db
from app.db.models.models import Rule as Regra
from app.schemas.schemas import RuleCreate as RegraCreate, RuleResponse as RegraSchema
from app.schemas.filters import RuleFilter as RegraFilter

router = APIRouter()

@router.post("/regras/", response_model=RegraSchema, status_code=status.HTTP_201_CREATED)
def create_regra(regra: RegraCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova regra de resposta.
    """
    # Verifica se já existe uma regra com a mesma palavra-chave
    existing_regra = db.query(Regra).filter(Regra.palavra_chave == regra.palavra_chave).first()
    if existing_regra:
        raise HTTPException(
            status_code=400,
            detail="Já existe uma regra com esta palavra-chave"
        )

    db_regra = Regra(
        palavra_chave=regra.palavra_chave,
        resposta_customizada=regra.resposta_customizada,
        ativo=regra.ativo
    )
    db.add(db_regra)
    db.commit()
    db.refresh(db_regra)
    return db_regra

@router.get("/regras/", response_model=List[RegraSchema])
def list_regras(
    response: Response,
    filtros: RegraFilter = Depends(),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Lista todas as regras com filtros avançados e paginação.
    """
    query = db.query(Regra)

    # Aplicar filtros
    if filtros.palavra_chave:
        query = query.filter(Regra.palavra_chave.ilike(f"%{filtros.palavra_chave}%"))
    
    if filtros.ativo is not None:
        query = query.filter(Regra.ativo == filtros.ativo)
    
    # Ordenação
    ordem_func = desc if filtros.ordem == "desc" else asc
    if hasattr(Regra, filtros.ordenar_por):
        query = query.order_by(ordem_func(getattr(Regra, filtros.ordenar_por)))

    # Contagem total para paginação
    total = query.count()
    response.headers["X-Total-Count"] = str(total)
    
    # Aplicar paginação
    regras = query.offset(skip).limit(limit).all()
    return regras

@router.get("/regras/{regra_id}", response_model=RegraSchema)
def get_regra(regra_id: int, db: Session = Depends(get_db)):
    """
    Obtém uma regra específica pelo ID.
    """
    regra = db.query(Regra).filter(Regra.id == regra_id).first()
    if regra is None:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    return regra

@router.put("/regras/{regra_id}", response_model=RegraSchema)
def update_regra(regra_id: int, regra: RegraCreate, db: Session = Depends(get_db)):
    """
    Atualiza uma regra existente.
    """
    db_regra = db.query(Regra).filter(Regra.id == regra_id).first()
    if db_regra is None:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    
    # Verifica se a nova palavra-chave já existe em outra regra
    if regra.palavra_chave != db_regra.palavra_chave:
        existing_regra = db.query(Regra).filter(Regra.palavra_chave == regra.palavra_chave).first()
        if existing_regra:
            raise HTTPException(
                status_code=400,
                detail="Já existe uma regra com esta palavra-chave"
            )
    
    db_regra.palavra_chave = regra.palavra_chave
    db_regra.resposta_customizada = regra.resposta_customizada
    db_regra.ativo = regra.ativo
    
    db.commit()
    db.refresh(db_regra)
    return db_regra

@router.delete("/regras/{regra_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regra(regra_id: int, db: Session = Depends(get_db)):
    """
    Remove uma regra.
    """
    regra = db.query(Regra).filter(Regra.id == regra_id).first()
    if regra is None:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    
    db.delete(regra)
    db.commit()
    return None 