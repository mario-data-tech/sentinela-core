class SentinelaCoreError(Exception):
    """Excepción base de SENTINELA-CORE."""
    pass


class DataProcessingError(SentinelaCoreError):
    """Error durante el procesamiento de datos."""
    pass


class ConfigurationError(SentinelaCoreError):
    """Error de configuración."""
    pass
