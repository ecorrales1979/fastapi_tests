from typing import Any

TRUTHY_VALUES: frozenset[str] = frozenset({"true", "1", "yes", "y", "on", "t"})


class Formatter:
    """Class with utilities for data conversion and formatting."""

    @staticmethod
    def to_bool(value: Any) -> bool:
        """Converts a value to boolean purely."""
        if isinstance(value, bool):
            return value
        if value is None:
            return False

        return str(value).strip().lower() in TRUTHY_VALUES

    @staticmethod
    def to_int(value: Any) -> int:
        """Converts a value to an integer. Raises ValueError/TypeError if invalid."""
        if isinstance(value, int) and not isinstance(value, bool):
            return value
        return int(value)

    @staticmethod
    def to_float(value: Any) -> float:
        """Converts a value to a float. Raises ValueError/TypeError if invalid."""
        if isinstance(value, float):
            return value
        return float(value)