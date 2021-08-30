from enum import IntEnum
from typing import Any


class BaseInfo:
    name: str


class Gender(IntEnum):
    MALE = 1
    FEMALE = 0


class PersonInfo(BaseInfo):
    birthday: str
    gender: Gender
    email: str


class Indexable:
    _id: Any
    
    @property
    def id(self) -> Any:
        return self.id


class IntIndexable(Indexable):
    _id: int

    @property
    def id(self) -> int:
        return self._id


class TextIndexable(Indexable):
    _id: str

    @property
    def id(self) -> str:
        return self._id