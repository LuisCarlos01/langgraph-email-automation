from sqlalchemy import Column, String, Text, DateTime, Enum, ARRAY, Float
from sqlalchemy.orm import declarative_base
import enum
from datetime import datetime

Base = declarative_base()

class EmailStatus(str, enum.Enum):
    PENDENTE = "pendente"
    ENVIADO = "enviado"
    IGNORADO = "ignorado"

class Email(Base):
    __tablename__ = "emails"

    id = Column(String, primary_key=True, index=True)  # ID do Gmail
    remetente = Column(String, nullable=False)
    assunto = Column(String, nullable=False)
    conteudo = Column(Text, nullable=False)
    resposta_gerada = Column(Text, nullable=False)
    resposta_editada = Column(Text, nullable=True)
    status = Column(Enum(EmailStatus), default=EmailStatus.PENDENTE, nullable=False)
    data_recebido = Column(DateTime, default=datetime.utcnow)
    embedding = Column(ARRAY(Float), nullable=True)  # Vetor de embedding do conteúdo
