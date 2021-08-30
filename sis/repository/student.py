from sis.repository.base import BaseRepository, EntityNotFoundException
from typing import Any
from sis.domain.student import *
from sis.repository.config import StudentColumns, TableNames


class StudentRepository(BaseRepository):
    __col_name: str = StudentColumns.NAME.value
    __col_birthday: str = StudentColumns.BIRTHDAY.value
    __col_gender: str = StudentColumns.GENDER.value
    __col_email: str = StudentColumns.EMAIL.value

    def __init__(self):
        super().__init__(table_name=TableNames.STUDENT.value, primary_key=StudentColumns.ID.value)

    def find_by_id(self, id: int) -> Student:
        query = f'select {self._primary_key}, '\
            + f'{self.__col_name}, {self.__col_birthday}, {self.__col_gender}, {self.__col_email} '\
            + f'from {self._table_name} '\
            + f'where {self._table_name}.{self._primary_key} = {id};'
        print(f'query: {query}')
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        if record is None:
            raise EntityNotFoundException(self._table_name)
        info = StudentInfo()
        info.name = record[1]
        info.birthday = record[2]
        info.gender = record[3]
        info.email = record[4]
        return Student(id=id, info=info)

    def find_all(self) -> list:
        query = f'select {self._primary_key}, '\
            + f'{self.__col_name}, {self.__col_birthday}, {self.__col_gender}, {self.__col_email} '\
            + f'from {self._table_name};'
        print(f'query: {query}')
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records is None:
            raise EntityNotFoundException(self._table_name)
        students = []
        for record in list(records):
            id = int(record[0])
            info = StudentInfo()
            info.name = record[1]
            info.birthday = record[2]
            info.gender = record[3]
            info.email = record[4]
            students.append(Student(id=id, info=info))
        print(f'results: {len(students)}')
        return students

    def save(self, info: StudentInfo) -> Student:
        query = f'insert into {self._table_name} '\
            + f'({self._primary_key}, {self.__col_name}, {self.__col_birthday}, {self.__col_gender}, {self.__col_email}) '\
            + f'values (%i, %s, %s, %i, %s);'
        print(f'query: {query}')
        values = (info.id, info.name, info.birthday, info.gender, info.email)
        self.cursor.execute(query, values)
        self._connection.commit()
        return Student(id=info.id, info=info)