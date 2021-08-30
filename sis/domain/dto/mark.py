from sis.domain.dto.base import *
from sis.domain.mark import Mark


class MarkDTO(BaseDTO):
    student_id: int
    subject_id: str
    mid: float
    end: float
    rate: float

    def __init__(self, mark: Mark):
        self.student_id = mark.student_id
        self.subject_id = mark.subject_id
        self.mid = mark.mid
        self.end = mark.end
        self.rate = mark.rate

    @staticmethod
    def of(mark: Mark):
        return MarkDTO(mark=mark)