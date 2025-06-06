from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional
from app.db.models.models import EmailStatus

# Schemas para Email
class EmailBase(BaseModel):
    subject: str
    sender: EmailStr
    recipient: EmailStr
    content: str

class EmailCreate(EmailBase):
    pass

class EmailUpdate(BaseModel):
    subject: Optional[str] = None
    content: Optional[str] = None
    status: Optional[EmailStatus] = None

class EmailResponse(EmailBase):
    id: int
    status: EmailStatus
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Schemas para Response
class ResponseBase(BaseModel):
    content: str
    generated_by_ai: bool = True

class ResponseCreate(ResponseBase):
    email_id: int

class ResponseUpdate(BaseModel):
    content: Optional[str] = None
    generated_by_ai: Optional[bool] = None

class ResponseResponse(ResponseBase):
    id: int
    email_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schemas para Rule
class RuleBase(BaseModel):
    keyword: str
    custom_response: str
    is_active: bool = True

class RuleCreate(RuleBase):
    pass

class RuleUpdate(BaseModel):
    keyword: Optional[str] = None
    custom_response: Optional[str] = None
    is_active: Optional[bool] = None

class RuleResponse(RuleBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 