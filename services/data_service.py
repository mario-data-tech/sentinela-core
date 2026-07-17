import pandas as pd


def obtener_datos_demo() -> pd.DataFrame:
    """Devuelve datos de ejemplo para el dashboard."""

    return pd.DataFrame(
        {
            "Categoría": [
                "Críticas",
                "Altas",
                "Medias",
                "Bajas",
            ],
            "Cantidad": [2, 8, 15, 27],
        }
    )
