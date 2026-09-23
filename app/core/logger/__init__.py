from app.core.logger.logger_interface import ILogger
from app.core.logger.logger_service import LoggerService
from app.core.logger.providers import ConsoleLoggerProvider

# Create the singleton logger instance
_provider = ConsoleLoggerProvider()
logger: ILogger = LoggerService.get_instance(_provider)

# Expose the clean instance for direct import
__all__ = ["ILogger", "logger"]
