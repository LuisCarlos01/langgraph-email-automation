from pydantic_settings import BaseSettings
from pydantic import Field, validator
from typing import Optional, List
import json

class Settings(BaseSettings):
    PROJECT_NAME: str = "iPass Email Automation"
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:210011@localhost:5432/ipass_email_db",
        description="URL de conexão com o banco de dados"
    )
    
    # Configurações adicionais do banco
    DB_POOL_SIZE: int = Field(default=5, description="Tamanho do pool de conexões")
    DB_MAX_OVERFLOW: int = Field(default=10, description="Máximo de conexões extras permitidas")
    DB_ECHO: bool = Field(default=False, description="Habilitar log de SQL")
    
    # Configurações CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000", "http://localhost:5173"],
        description="Lista de origens permitidas para CORS"
    )
    CORS_METHODS: List[str] = Field(
        default=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        description="Métodos HTTP permitidos"
    )
    CORS_HEADERS: List[str] = Field(
        default=[
            "Content-Type",
            "Authorization",
            "X-Total-Count",
            "accept",
            "Origin",
            "Access-Control-Allow-Origin",
        ],
        description="Headers HTTP permitidos"
    )
    
    # Configurações de Email para Alertas
    ALERT_EMAIL_FROM: str = Field(
        default="contato@ipass.com.br",
        description="Email remetente para alertas"
    )
    ALERT_EMAIL_TO: str = Field(
        default="gabriel@ipass.com.br",
        description="Email destinatário para alertas"
    )
    SMTP_HOST: str = Field(
        default="smtp.gmail.com",
        description="Host do servidor SMTP"
    )
    SMTP_PORT: int = Field(
        default=587,
        description="Porta do servidor SMTP"
    )
    SMTP_USER: str = Field(
        default="contato@ipass.com.br",
        description="Usuário SMTP"
    )
    SMTP_PASSWORD: str = Field(
        default="210011",
        description="Senha SMTP"
    )
    SMTP_TLS: bool = Field(
        default=True,
        description="Usar TLS para SMTP"
    )
    
    # Configurações de Monitoramento
    ENABLE_METRICS: bool = Field(
        default=True,
        description="Habilitar coleta de métricas"
    )
    METRICS_PORT: int = Field(
        default=9090,
        description="Porta para métricas Prometheus"
    )
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Nível de log"
    )
    ENABLE_REQUEST_LOGGING: bool = Field(
        default=True,
        description="Habilitar log de requisições"
    )
    ENABLE_PERFORMANCE_METRICS: bool = Field(
        default=True,
        description="Habilitar métricas de performance"
    )
    
    # Configurações de Alertas
    ALERT_ERROR_RATE_THRESHOLD: float = Field(
        default=0.1,
        description="Limite de taxa de erro para alertas (10%)"
    )
    ALERT_RESPONSE_TIME_THRESHOLD: float = Field(
        default=5.0,
        description="Limite de tempo de resposta para alertas (segundos)"
    )
    ALERT_MEMORY_USAGE_THRESHOLD: float = Field(
        default=80.0,
        description="Limite de uso de memória para alertas (%)"
    )
    ALERT_CPU_USAGE_THRESHOLD: float = Field(
        default=90.0,
        description="Limite de uso de CPU para alertas (%)"
    )
    ALERT_EMAIL_QUEUE_SIZE_THRESHOLD: int = Field(
        default=1000,
        description="Limite de tamanho da fila de emails para alertas"
    )

    @validator("CORS_ORIGINS", "CORS_METHODS", "CORS_HEADERS", pre=True)
    def parse_list(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return v.split(",")
        return v

    @validator("SMTP_TLS", "ENABLE_METRICS", "ENABLE_REQUEST_LOGGING", "ENABLE_PERFORMANCE_METRICS", pre=True)
    def parse_bool(cls, v):
        if isinstance(v, str):
            return v.lower() == "true"
        return v

    @validator(
        "ALERT_ERROR_RATE_THRESHOLD",
        "ALERT_RESPONSE_TIME_THRESHOLD",
        "ALERT_MEMORY_USAGE_THRESHOLD",
        "ALERT_CPU_USAGE_THRESHOLD",
        pre=True
    )
    def parse_float(cls, v):
        if isinstance(v, str):
            return float(v.split("#")[0].strip())
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 