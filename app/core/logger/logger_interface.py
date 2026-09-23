from abc import ABC, abstractmethod
from typing import Any


class ILogger(ABC):

    @abstractmethod
    def info(self, message: str, context: dict[str, Any] | None = None) -> None:
        pass

    @abstractmethod
    def error(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        pass

    @abstractmethod
    def warn(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        pass

    @abstractmethod
    def critical(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        pass