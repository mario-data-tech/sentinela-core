import pandas as pd
import logging
from typing import List, Optional
from models.data_models import DataEntry

logger = logging.getLogger(__name__)

class DataService:
    """Servicio encargado de la lógica de procesamiento de datos."""
    
    @staticmethod
    def process_raw_data(file_path: str) -> pd.DataFrame:
        """Carga y procesa archivos de datos (CSV/Excel)."""
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Formato de archivo no soportado.")
            
            logger.info(f"Datos cargados exitosamente desde {file_path}")
            return df
        except Exception as e:
            logger.error(f"Error procesando el archivo: {e}")
            raise e

    @staticmethod
    def validate_entries(data: List[dict]) -> List[DataEntry]:
        """Valida una lista de diccionarios contra el modelo DataEntry."""
        validated_data = []
        for entry in data:
            try:
                validated_data.append(DataEntry(**entry))
            except Exception as e:
                logger.warning(f"Error de validación en registro {entry}: {e}")
        return validated_data
