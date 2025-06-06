from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.database import Base

class EmailStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(Text, nullable=False)
    sender = Column(Text, nullable=False)
    recipient = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    status = Column(Enum(EmailStatus), default=EmailStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relacionamentos
    responses = relationship("Response", back_populates="email", cascade="all, delete-orphan")

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, ForeignKey("emails.id", ondelete="CASCADE"))
    content = Column(Text, nullable=False)
    generated_by_ai = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    email = relationship("Email", back_populates="responses")

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(Text, unique=True, nullable=False)
    custom_response = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 