import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any
from datetime import datetime
import json
from app.core.config import settings
from app.core.logging import logger

class AlertManager:
    def __init__(self):
        self.alert_thresholds = {
            "error_rate": 0.1,  # 10% de erros
            "response_time": 5.0,  # 5 segundos
            "memory_usage": 0.9,  # 90% de uso
            "email_queue_size": 1000,  # 1000 emails na fila
        }
        
        self.alert_channels = {
            "critical": ["email", "slack"],
            "warning": ["slack"],
            "info": ["log"]
        }
    
    async def check_error_rate(self, error_count: int, total_requests: int) -> None:
        """Verifica taxa de erros"""
        if total_requests > 0:
            error_rate = error_count / total_requests
            if error_rate >= self.alert_thresholds["error_rate"]:
                await self.send_alert(
                    level="critical",
                    title="High Error Rate Detected",
                    message=f"Error rate is {error_rate:.2%}",
                    context={"error_rate": error_rate}
                )
    
    async def check_response_time(self, response_time: float) -> None:
        """Verifica tempo de resposta"""
        if response_time >= self.alert_thresholds["response_time"]:
            await self.send_alert(
                level="warning",
                title="Slow Response Time",
                message=f"Response time is {response_time:.2f}s",
                context={"response_time": response_time}
            )
    
    async def check_memory_usage(self, memory_percent: float) -> None:
        """Verifica uso de memória"""
        if memory_percent >= self.alert_thresholds["memory_usage"]:
            await self.send_alert(
                level="warning",
                title="High Memory Usage",
                message=f"Memory usage is {memory_percent:.2%}",
                context={"memory_percent": memory_percent}
            )
    
    async def check_email_queue(self, queue_size: int) -> None:
        """Verifica tamanho da fila de emails"""
        if queue_size >= self.alert_thresholds["email_queue_size"]:
            await self.send_alert(
                level="warning",
                title="Large Email Queue",
                message=f"Email queue size is {queue_size}",
                context={"queue_size": queue_size}
            )
    
    async def send_alert(
        self,
        level: str,
        title: str,
        message: str,
        context: Dict[str, Any] = None
    ) -> None:
        """Envia alertas pelos canais configurados"""
        channels = self.alert_channels.get(level, ["log"])
        
        alert_data = {
            "level": level,
            "title": title,
            "message": message,
            "timestamp": datetime.utcnow().isoformat(),
            "context": context or {}
        }
        
        for channel in channels:
            try:
                if channel == "email":
                    await self._send_email_alert(alert_data)
                elif channel == "slack":
                    await self._send_slack_alert(alert_data)
                elif channel == "log":
                    self._log_alert(alert_data)
            except Exception as e:
                logger.error(
                    "alert_send_failed",
                    channel=channel,
                    error=str(e),
                    alert_data=alert_data
                )
    
    async def _send_email_alert(self, alert_data: Dict[str, Any]) -> None:
        """Envia alerta por email"""
        msg = MIMEMultipart()
        msg["Subject"] = f"[{alert_data['level'].upper()}] {alert_data['title']}"
        msg["From"] = settings.ALERT_EMAIL_FROM
        msg["To"] = settings.ALERT_EMAIL_TO
        
        body = f"""
        Alert Level: {alert_data['level']}
        Time: {alert_data['timestamp']}
        
        {alert_data['message']}
        
        Context:
        {json.dumps(alert_data['context'], indent=2)}
        """
        
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_TLS:
                server.starttls()
            if settings.SMTP_USER and settings.SMTP_PASSWORD:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
    
    async def _send_slack_alert(self, alert_data: Dict[str, Any]) -> None:
        """Envia alerta para o Slack"""
        # Implementar integração com Slack aqui
        pass
    
    def _log_alert(self, alert_data: Dict[str, Any]) -> None:
        """Registra alerta nos logs"""
        logger.warning("alert_triggered", **alert_data)

# Instância global do gerenciador de alertas
alert_manager = AlertManager() 