from app.core.logger.logger_interface import ILogger
from app.core.logger.logger_service import LoggerService
from app.core.logger.providers import ConsoleLoggerProvider, FileLoggerProvider

providers = {
    'file': FileLoggerProvider(),
    'console': ConsoleLoggerProvider()
}

# Create the singleton logger instance
_provider = providers['file']
logger: ILogger = LoggerService.get_instance(_provider)

# Expose the clean instance for direct import
__all__ = ["ILogger", "logger"]
