import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict
from fastapi import Request, Response
import structlog
from app.core.config import settings

# Configurar diretório de logs
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configurar logging básico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "app.log"),
        logging.StreamHandler()
    ]
)

# Configurar structlog para logs estruturados
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Criar logger estruturado
logger = structlog.get_logger()

class RequestResponseMiddleware:
    async def __call__(
        self,
        request: Request,
        call_next: Any,
    ) -> Response:
        start_time = datetime.utcnow()
        
        # Log request
        logger.info(
            "request_started",
            method=request.method,
            url=str(request.url),
            client_host=request.client.host if request.client else None,
        )
        
        response = await call_next(request)
        
        # Calcular duração
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        # Log response
        logger.info(
            "request_finished",
            method=request.method,
            url=str(request.url),
            status_code=response.status_code,
            duration=duration,
        )
        
        return response

def log_error(error: Exception, request: Request = None, **kwargs) -> None:
    """
    Log errors with context information
    """
    error_context = {
        "error_type": type(error).__name__,
        "error_message": str(error),
        **kwargs
    }
    
    if request:
        error_context.update({
            "method": request.method,
            "url": str(request.url),
            "client_host": request.client.host if request.client else None,
        })
    
    logger.error("error_occurred", **error_context)

def log_email_operation(operation: str, email_id: str, **kwargs) -> None:
    """
    Log email operations with context
    """
    logger.info(
        f"email_{operation}",
        email_id=email_id,
        **kwargs
    )

def log_performance_metric(
    metric_name: str,
    value: float,
    tags: Dict[str, str] = None
) -> None:
    """
    Log performance metrics
    """
    logger.info(
        "performance_metric",
        metric=metric_name,
        value=value,
        tags=tags or {}
    ) 