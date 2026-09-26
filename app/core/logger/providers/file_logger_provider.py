import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from app.core.logger.providers import BaseLoggerProvider
from app.utils import Helpers


class FileLoggerProvider(BaseLoggerProvider):

    def __init__(self) -> None:
        file_path: str = Helpers.get_env_var("FILE_LOGGER_PATH", "logs/app.log")
        max_bytes: int = Helpers.get_env_var(
            "FILE_LOGGER_MAX_BYTES", 5242880, value_type=int
        )
        backup_count: int = Helpers.get_env_var(
            "FILE_LOGGER_BACKUP_COUNT", 3, value_type=int
        )
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