from sis.domain.dto.base import *
from sis.domain.subject import Subject


class SubjectDTO(BaseDTO):
    id: str
    name: str
    semester: str
    credits: int

    def __init__(self, subject: Subject):
        self.id = subject.id
        self.name = subject.name
        self.semester = subject.semester
        self.credits = subject.credits

    @staticmethod
    def of(subject: Subject):
        return SubjectDTO(subject=subject)