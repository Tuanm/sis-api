from typing import Any
from sis.domain.subject import Subject
from sis.repository.base import EntityNotFoundException
from sis.domain.dto.subject import SubjectDTO
from sis.repository.subject import SubjectRepository
from sis.service.base import BaseService


class SubjectService(BaseService):
    def __init__(self):
        self._repository = SubjectRepository()

    def find_by_id(self, id: str) -> SubjectDTO:
        try:
            dto = SubjectDTO.of(self._repository.find_by_id(id=id))
            return dto
        except EntityNotFoundException as exception:
            raise exception

    def find_all(self) -> list:
        try:
            subjects: list[Subject] = self._repository.find_all()
            dtos: list[SubjectDTO] = [SubjectDTO(subject) for subject in subjects]
            return dtos
        except EntityNotFoundException as exception:
            raise exception
    
    def save(self, info: Any) -> SubjectDTO:
        try:
            # validate info here
            return SubjectDTO.of(self._repository.save(info=info))
        except Exception as exception:
            raise exception