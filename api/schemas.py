"""
Schemas Pydantic para validação de dados da API.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class EmailRequest(BaseModel):
    subject: str
    body: str
    sender: EmailStr
    recipients: List[EmailStr]
    
class EmailResponse(BaseModel):
    id: str
    request: EmailRequest
    response: str
    created_at: datetime
    status: str
    
    class Config:
        from_attributes = True 