from sis.domain.base import IntIndexable, PersonInfo


class StudentInfo(PersonInfo):
    id: int


class Student:
    __info: StudentInfo

    def __init__(self, id: int, info: StudentInfo) -> None:
        self.__info = info
        self.__info.id = id

    @property
    def id(self) -> int:
        return self.__info.id

    @property
    def name(self) -> str:
        return self.__info.name

    @property
    def birthday(self) -> str:
        return self.__info.birthday

    @property
    def gender(self) -> int:
        return int(self.__info.gender)

    @property
    def email(self) -> str:
        return self.__info.email

    def __str__(self) -> str:
        return '{id=%i,name=\"%s\",birthday=\"%s\",gender=%i,email=\"%s\"}'\
            % (self.id, self.name, self.birthday, self.gender, self.email)

    def __repr__(self) -> str:
        return self.__str__()

    