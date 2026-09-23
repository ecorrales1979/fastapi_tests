import json
from datetime import datetime, timezone
from typing import Any

from app.core.logger import ILogger


class ConsoleLoggerProvider(ILogger):

    def info(self, message: str, context: dict[str, Any] | None = None) -> None:
        ctx = self._get_context_str(context)
        print(f"[INFO] {self._get_date_str()} {message}{ctx}")

    def error(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        tr = self._get_trace_str(trace)
        ctx = self._get_context_str(context)
        print(f"[ERROR] {self._get_date_str()} {message}{ctx}{tr}")

    def warn(
        self, message: str, context: dict[str, Any] | None = None
    ) -> None:
        ctx = self._get_context_str(context)
        print(f"[WARN] {self._get_date_str()} {message}{ctx}")

    def critical(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        tr = self._get_trace_str(trace)
        ctx = self._get_context_str(context)
        print(f"[CRITICAL] {self._get_date_str()} {message}{ctx}{tr}")

    def _get_context_str(self, context: dict[str, Any] | None) -> str:
        return f" | Context: {json.dumps(context)}" if context else ""

    def _get_trace_str(self, trace: str | None) -> str:
        return f"\nTrace: {trace}" if trace else ""

    def _get_date_str(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")