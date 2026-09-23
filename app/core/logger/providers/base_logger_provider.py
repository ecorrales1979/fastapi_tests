import json
from datetime import datetime, timezone
from typing import Any

from app.core.logger import ILogger


class BaseLoggerProvider(ILogger):

    def _get_context_str(self, context: dict[str, Any] | None) -> str:
        return f" | Context: {json.dumps(context, ensure_ascii=False)}" if context else ""

    def _get_trace_str(self, trace: str | None) -> str:
        return f"\nTrace: {trace}" if trace else ""

    def _get_date_str(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    def _format_line(
        self,
        level: str,
        message: str,
        context: dict[str, Any] | None = None,
        trace: str | None = None,
    ) -> str:
        ctx = self._get_context_str(context)
        tr = self._get_trace_str(trace)
        date_str = self._get_date_str()
        return f"[{level}] {date_str} {message}{ctx}{tr}"