from sis.domain.base import BaseInfo, IntIndexable, TextIndexable


class SubjectInfo(BaseInfo):
    id: str
    semester: str
    credits: int


class Subject:
    __info: SubjectInfo

    def __init__(self, id: str, info: SubjectInfo) -> None:
        self.__info = info
        self.__info.id = id

    @property
    def id(self) -> str:
        return self.__info.id

    @property
    def name(self) -> str:
        return self.__info.name

    @property
    def semester(self) -> str:
        return self.__info.semester

    @property
    def credits(self) -> int:
        return self.__info.credits