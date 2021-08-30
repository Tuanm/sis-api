class MarkInfo:
    student_id: int
    subject_id: str
    mid: float
    end: float
    rate: float



class Mark:
    __info: MarkInfo

    def __init__(self, student_id: int, subject_id: str, info: MarkInfo) -> None:
        self.__info = info
        self.__info.student_id = student_id
        self.__info.subject_id = subject_id

    @property
    def id(self):
        return (self.__info.student_id, self.__info.subject_id)

    @property
    def student_id(self) -> int:
        return self.__info.student_id

    @property
    def subject_id(self) -> str:
        return self.__info.subject_id

    @property
    def mid(self) -> float:
        return self.__info.mid

    @property
    def end(self) -> float:
        return self.__info.end

    @property
    def rate(self) -> float:
        return self.__info.rate
    
