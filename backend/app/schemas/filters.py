from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.db.models.models import EmailStatus

class BaseFilter(BaseModel):
    order: str = "desc"  # asc ou desc
    order_by: str = "id"

class EmailFilter(BaseModel):
    subject: Optional[str] = None
    sender: Optional[str] = None
    status: Optional[EmailStatus] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None

class ResponseFilter(BaseModel):
    email_id: Optional[int] = None
    generated_by_ai: Optional[bool] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None

class RuleFilter(BaseModel):
    keyword: Optional[str] = None
    is_active: Optional[bool] = None 