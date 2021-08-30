from typing import Any
from sis.domain.dto.student import StudentDTO
from sis.repository.base import EntityNotFoundException
from sis.domain.student import *
from sis.service.base import BaseService
from sis.repository.student import StudentRepository


class StudentService(BaseService):
    def __init__(self):
        self._repository = StudentRepository()

    def find_by_id(self, id: int) -> StudentDTO:
        try:
            dto = StudentDTO.of(self._repository.find_by_id(id=id))
            return dto
        except EntityNotFoundException as exception:
            raise exception

    def find_all(self) -> list:
        try:
            students: list[Student] = self._repository.find_all()
            dtos: list[StudentDTO] = [StudentDTO(student) for student in students]
            return dtos
        except EntityNotFoundException as exception:
            raise exception
    
    def save(self, info: Any) -> StudentDTO:
        try:
            # validate info here
            return StudentDTO.of(self._repository.save(info=info))
        except Exception as exception:
            raise exception