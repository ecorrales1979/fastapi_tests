import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from app.core.logger.providers import BaseLoggerProvider


class FileLoggerProvider(BaseLoggerProvider):

    def __init__(
        self,
        file_path: str = "logs/app.log",
        max_bytes: int = 5 * 1024 * 1024,  # 5 MB por archivo
        backup_count: int = 3,              # Conserva hasta 3 archivos
    ) -> None:
        log_file = Path(file_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)

        self._logger = logging.getLogger("FileLoggerProvider")
        self._logger.setLevel(logging.INFO)

        if not self._logger.handlers:
            handler = RotatingFileHandler(
                log_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
            # Single format for all log messages
            handler.setFormatter(logging.Formatter("%(message)s"))
            self._logger.addHandler(handler)

    def info(self, message: str, context: dict[str, Any] | None = None) -> None:
        line = self._format_line("INFO", message, context)
        self._logger.info(line)

    def warn(self, message: str, context: dict[str, Any] | None = None) -> None:
        line = self._format_line("WARN", message, context)
        self._logger.warning(line)

    def error(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        line = self._format_line("ERROR", message, context, trace)
        self._logger.error(line)

    def critical(
        self,
        message: str,
        trace: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        line = self._format_line("CRITICAL", message, context, trace)
        self._logger.critical(line)