"""
Configuração de autenticação OAuth2 com Google.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from typing import Optional

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/v2/auth",
    tokenUrl="https://oauth2.googleapis.com/token"
)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> Optional[str]:
    """
    Valida o token OAuth2 e retorna o usuário atual.
    
    Args:
        token: Token de acesso OAuth2
        
    Returns:
        ID do usuário autenticado
        
    Raises:
        HTTPException: Se a autenticação falhar
    """
    # TODO: Implementar validação do token
    pass 