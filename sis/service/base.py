from enum import Enum
from typing import Any
from sis.repository.base import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def find_all(self) -> Any: ...
    def find_by_id(self, id: Any) -> Any: ...
    def save(self, entity: Any) -> Any: ...
