from sis.domain.dto.base import *
from sis.domain.student import Student


class StudentDTO(BaseDTO):
    id: int
    name: str
    birthday: str
    gender: int
    email: str

    def __init__(self, student: Student):
        self.id = student.id
        self.name = student.name
        self.birthday = student.birthday
        self.gender = student.gender
        self.email = student.email

    @staticmethod
    def of(student: Student):
        return StudentDTO(student=student)