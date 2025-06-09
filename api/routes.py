"""
Rotas da API FastAPI para o iPassResponder.
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from .schemas import EmailResponse, EmailRequest
from .auth_google import get_current_user

router = APIRouter()

@router.post("/email/process", response_model=EmailResponse)
async def process_email(
    request: EmailRequest,
    current_user = Depends(get_current_user)
):
    """Processa um novo email recebido"""
    # TODO: Implementar processamento
    pass

@router.get("/email/history", response_model=List[EmailResponse])
async def get_email_history(
    current_user = Depends(get_current_user)
):
    """Retorna histórico de emails processados"""
    # TODO: Implementar histórico
    pass 