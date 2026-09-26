import os
from typing import TypeVar

from dotenv import load_dotenv

from app.utils.formatters import Formatter

load_dotenv()

T = TypeVar("T", str, bool, int, float)


class MissingEnvironmentVariableError(Exception):
    """Raised when a required environment variable is not defined."""


class Helpers:
    """Class with general helper utilities."""

    @staticmethod
    def get_env_var(
        name: str,
        default: T | None = None,
        is_required: bool = False,
        value_type: type[T] = str,
    ) -> T | None:
        """Retrieves an environment variable and optionally converts it to the requested type."""
        value = os.getenv(name)

        if value is None:
            if is_required and default is None:
                raise MissingEnvironmentVariableError(
                    f"Required environment variable '{name}' is not defined"
                )
            value = default

        if value is None:
            return None

        if value_type is str:
            return str(value)
        if value_type is bool:
            return Formatter.to_bool(value)
        if value_type is int:
            return Formatter.to_int(value)
        if value_type is float:
            return Formatter.to_float(value)

        raise ValueError(f"Unsupported value_type: {value_type}")
