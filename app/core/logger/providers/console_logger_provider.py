from typing import Any

from app.core.logger.providers import BaseLoggerProvider


class ConsoleLoggerProvider(BaseLoggerProvider):

    def info(self, message: str, context: dict[str, Any] | None = None) -> None:
        print(self._format_line("INFO", message, context))

    def error(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        print(self._format_line("ERROR", message, context, trace))

    def warn(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        print(self._format_line("WARN", message, context))

    def critical(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        print(self._format_line("CRITICAL", message, context, trace))
