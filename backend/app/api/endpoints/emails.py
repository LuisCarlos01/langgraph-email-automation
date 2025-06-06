from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.db.database import get_db
from app.db.models.models import Email
from app.schemas.schemas import EmailCreate, EmailUpdate, EmailResponse
from app.schemas.filters import EmailFilter

router = APIRouter()

@router.post("/emails/", response_model=EmailResponse, status_code=status.HTTP_201_CREATED)
async def create_email(email: EmailCreate, db: AsyncSession = Depends(get_db)):
    """Criar um novo email."""
    db_email = Email(**email.model_dump())
    db.add(db_email)
    await db.commit()
    await db.refresh(db_email)
    return db_email

@router.get("/emails/", response_model=List[EmailResponse])
async def list_emails(
    filters: EmailFilter = Depends(),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: AsyncSession = Depends(get_db)
):
    """Listar emails com filtros opcionais."""
    query = select(Email)
    
    # Aplicar filtros
    if filters.subject:
        query = query.filter(Email.subject.ilike(f"%{filters.subject}%"))
    if filters.sender:
        query = query.filter(Email.sender.ilike(f"%{filters.sender}%"))
    if filters.status:
        query = query.filter(Email.status == filters.status)
    
    # Aplicar paginação
    query = query.offset(skip).limit(limit)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/emails/{email_id}", response_model=EmailResponse)
async def get_email(email_id: int, db: AsyncSession = Depends(get_db)):
    """Obter um email específico por ID."""
    result = await db.execute(select(Email).filter(Email.id == email_id))
    email = result.scalar_one_or_none()
    
    if email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    return email

@router.patch("/emails/{email_id}", response_model=EmailResponse)
async def update_email(email_id: int, email_update: EmailUpdate, db: AsyncSession = Depends(get_db)):
    """Atualizar um email existente."""
    # Verificar se o email existe
    result = await db.execute(select(Email).filter(Email.id == email_id))
    email = result.scalar_one_or_none()
    
    if email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    
    # Atualizar apenas os campos fornecidos
    update_data = email_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(email, field, value)
    
    await db.commit()
    await db.refresh(email)
    return email

@router.delete("/emails/{email_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_email(email_id: int, db: AsyncSession = Depends(get_db)):
    """Deletar um email."""
    result = await db.execute(select(Email).filter(Email.id == email_id))
    email = result.scalar_one_or_none()
    
    if email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    
    await db.delete(email)
    await db.commit()
    return None 