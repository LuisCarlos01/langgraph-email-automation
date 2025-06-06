from prometheus_client import Counter, Histogram, Gauge
import time
from typing import Callable
from functools import wraps
from fastapi import Request
from app.core.logging import logger

# Métricas HTTP
http_requests_total = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status']
)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

# Métricas de Email
email_processing_total = Counter(
    'email_processing_total',
    'Total number of emails processed',
    ['status']
)

email_processing_duration_seconds = Histogram(
    'email_processing_duration_seconds',
    'Email processing duration in seconds'
)

# Métricas do Sistema
system_memory_usage = Gauge(
    'system_memory_usage_bytes',
    'Current system memory usage in bytes'
)

db_connections_active = Gauge(
    'db_connections_active',
    'Number of active database connections'
)

def track_request_metrics():
    """Decorator para rastrear métricas de requisições HTTP"""
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            start_time = time.time()
            
            try:
                response = await func(request, *args, **kwargs)
                status = response.status_code
            except Exception as e:
                status = 500
                raise e
            finally:
                duration = time.time() - start_time
                endpoint = request.url.path
                method = request.method
                
                # Atualizar métricas
                http_requests_total.labels(
                    method=method,
                    endpoint=endpoint,
                    status=status
                ).inc()
                
                http_request_duration_seconds.labels(
                    method=method,
                    endpoint=endpoint
                ).observe(duration)
                
                # Log para análise
                logger.info(
                    "request_metrics",
                    method=method,
                    endpoint=endpoint,
                    status=status,
                    duration=duration
                )
            
            return response
        return wrapper
    return decorator

def track_email_processing(func: Callable):
    """Decorator para rastrear métricas de processamento de email"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = await func(*args, **kwargs)
            status = "success"
        except Exception as e:
            status = "error"
            raise e
        finally:
            duration = time.time() - start_time
            
            # Atualizar métricas
            email_processing_total.labels(status=status).inc()
            email_processing_duration_seconds.observe(duration)
            
            # Log para análise
            logger.info(
                "email_processing_metrics",
                status=status,
                duration=duration
            )
        
        return result
    return wrapper

def update_system_metrics():
    """Atualiza métricas do sistema"""
    import psutil
    
    # Atualizar uso de memória
    memory = psutil.virtual_memory()
    system_memory_usage.set(memory.used)
    
    # Log para análise
    logger.info(
        "system_metrics",
        memory_used=memory.used,
        memory_percent=memory.percent
    ) 