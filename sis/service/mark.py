from typing import Any
from sis.domain.mark import Mark
from sis.repository.base import EntityNotFoundException
from sis.domain.dto.mark import MarkDTO
from sis.repository.mark import MarkRepository
from sis.service.base import BaseService


class MarkService(BaseService):
    def __init__(self):
        self._repository = MarkRepository()

    def find_by_id(self, id: Any) -> MarkDTO:
        student_id, subject_id = id
        try:
            dto = MarkDTO.of(self._repository.find_by_id(student_id=student_id, subject_id=subject_id))
            return dto
        except EntityNotFoundException as exception:
            raise exception

    def find_all(self) -> list:
        try:
            marks: list[Mark] = self._repository.find_all()
            dtos: list[MarkDTO] = [MarkDTO(mark) for mark in marks]
            return dtos
        except EntityNotFoundException as exception:
            raise exception
    
    def save(self, info: Any) -> MarkDTO:
        try:
            # validate info here
            return MarkDTO.of(self._repository.save(info=info))
        except Exception as exception:
            raise exception