from typing import Any

from app.core.logger import ILogger


class LoggerService(ILogger):
    _instance: "LoggerService | None" = None

    def __init__(self, provider: ILogger) -> None:
        # Prevenimos la reinicialización accidental si ya existe la instancia
        if LoggerService._instance is not None:
            raise RuntimeError(
                "Usa LoggerService.get_instance() para obtener la instancia Singleton."
            )
        self._provider = provider

    @classmethod
    def get_instance(cls, provider: ILogger | None = None) -> "LoggerService":
        if cls._instance is None:
            if provider is None:
                raise ValueError(
                    "Se requiere un ILogger provider para la inicialización."
                )
            # Creamos la instancia bypassing el check del __init__
            cls._instance = super().__new__(cls)
            cls._instance._provider = provider
        return cls._instance

    def info(self, message: str, context: dict[str, Any] | None = None) -> None:
        self._provider.info(message, context)

    def error(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        self._provider.error(message, trace, context)

    def warn(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        self._provider.warn(message, context)

    def critical(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        self._provider.critical(message, context)

