from datetime import datetime


def obtener_fecha_actual() -> str:
    """Devuelve la fecha y hora actual."""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
