from sis.domain.subject import *
from sis.repository.config import SubjectColumns, TableNames
from sis.repository.base import BaseRepository, EntityNotFoundException


class SubjectRepository(BaseRepository):
    __col_name: str = SubjectColumns.NAME.value
    __col_semester: str = SubjectColumns.SEMESTER.value
    __col_credits: str = SubjectColumns.CREDITS.value

    def __init__(self):
        super().__init__(table_name=TableNames.SUBJECT.value, primary_key=SubjectColumns.ID.value)

    def find_by_id(self, id: str) -> Subject:
        query = f'select {self._primary_key}, '\
            + f'{self.__col_name}, {self.__col_semester}, {self.__col_credits} '\
            + f'from {self._table_name} '\
            + f'where {self._table_name}.{self._primary_key} = \'{id}\';'
        print(f'query: {query}')
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        if record is None:
            raise EntityNotFoundException(self._table_name)
        info = SubjectInfo()
        info.name = record[1]
        info.semester = record[2]
        info.credits = record[3]
        return Subject(id=id, info=info)

    def find_all(self) -> list:
        query = f'select {self._primary_key}, '\
            + f'{self.__col_name}, {self.__col_semester}, {self.__col_credits} '\
            + f'from {self._table_name};'
        print(f'query: {query}')
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records is None:
            raise EntityNotFoundException(self._table_name)
        subjects = []
        for record in list(records):
            id = record[0]
            info = SubjectInfo()
            info.name = record[1]
            info.semester = record[2]
            info.credits = int(record[3])
            subjects.append(Subject(id=id, info=info))
        print(f'results: {len(subjects)}')
        return subjects

    def save(self, info: SubjectInfo) -> Subject:
        query = f'insert into {self._table_name} '\
            + f'({self._primary_key}, {self.__col_name}, {self.__col_semester}, {self.__col_credits}) '\
            + f'values (%s, %s, %s, %i);'
        print(f'query: {query}')
        values = (info.id, info.name, info.semester, info.credits)
        self.cursor.execute(query, values)
        self._connection.commit()
        return Subject(id=info.id, info=info)