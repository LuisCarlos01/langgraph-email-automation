"""
Arquivo base para importar todos os modelos.
Isso é necessário para que o Alembic possa detectar todos os modelos durante a geração de migrações.
"""

from app.db.database import Base
from app.db.models.models import Email, Response, Rule 