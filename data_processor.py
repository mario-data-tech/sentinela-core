import logging
from typing import List, Dict, Any

# Configuración de logs para detectar fallos en la nube
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def filtrar_datos(datos: List[Dict[str, Any]], criterio: str, valor: Any) -> List[Dict[str, Any]]:
    """
    Filtra una lista de diccionarios de forma segura.
    - datos: Lista de logs o registros.
    - criterio: La clave que buscamos (ej: 'status', 'ip', 'nivel').
    - valor: Lo que queremos filtrar.
    """
    resultados_filtrados = []
    
    try:
        if not isinstance(datos, list):
            raise ValueError("El formato de los datos no es una lista válida.")

        for registro in datos:
            try:
                # Verificamos si existe la clave para evitar KeyError
                if registro.get(criterio) == valor:
                    resultados_filtrados.append(registro)
            except Exception as e:
                logger.warning(f"Error procesando un registro individual: {e}")
                continue # Saltamos el registro corrupto y seguimos
                
    except Exception as e:
        logger.error(f"Fallo crítico en el módulo de filtrado: {e}")
        return []

    return resultados_filtrados
