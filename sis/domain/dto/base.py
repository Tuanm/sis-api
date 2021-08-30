from typing import Any


class BaseDTO:
    @staticmethod
    def of(o: Any) -> Any: ...