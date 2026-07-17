from pydantic import BaseModel

class Kpi(BaseModel):
    nombre: str
    valor: str
    estado: str
