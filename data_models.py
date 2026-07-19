from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class DataEntry(BaseModel):
    """Modelo Pydantic para validar entradas de datos del sistema."""
    id: int
    timestamp: datetime = Field(default_factory=datetime.now)
    sensor_id: str
    value: float
    status: str = "active"
    description: Optional[str] = None

class SystemMetrics(BaseModel):
    """Modelo para métricas del sistema."""
    cpu_usage: float
    memory_usage: float
    active_connections: int
    updated_at: datetime = Field(default_factory=datetime.now)

class UserProfile(BaseModel):
    """Modelo para usuarios del sistema."""
    user_id: int
    username: str
    email: EmailStr
    is_admin: bool = False
