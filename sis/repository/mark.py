from sis.domain.mark import Mark, MarkInfo
from sis.repository.config import MarkColumns, TableNames
from sis.repository.base import BaseRepository, EntityNotFoundException


class MarkRepository(BaseRepository):
    __col_mid: str = MarkColumns.MID_POINT.value
    __col_end: str = MarkColumns.END_POINT.value
    __col_rate: str = MarkColumns.MID_RATE.value

    def __init__(self):
        super().__init__(
            table_name=TableNames.MARK.value,
            primary_key=(MarkColumns.STUDENT_ID.value, MarkColumns.SUBJECT_ID.value)
        )

    def find_by_id(self, student_id: int, subject_id: str) -> Mark:
        query = f'select {self._primary_key[0]}, {self._primary_key[1]}, '\
            + f'{self.__col_mid}, {self.__col_end}, {self.__col_rate} '\
            + f'from {self._table_name} '\
            + f'where {self._table_name}.{self._primary_key[0]} = {student_id} '\
            + f'and {self._table_name}.{self._primary_key[1]} = \'{subject_id}\';'
        print(f'query: {query}')
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        if record is None:
            raise EntityNotFoundException(self._table_name)
        info = MarkInfo()
        info.mid = float(record[2])
        info.end = float(record[3])
        info.rate = float(record[4])
        return Mark(student_id=student_id, subject_id=subject_id, info=info)

    def find_all(self) -> list:
        query = f'select {self._primary_key[0]}, {self._primary_key[1]}, '\
            + f'{self.__col_mid}, {self.__col_end}, {self.__col_rate} '\
            + f'from {self._table_name};'
        print(f'query: {query}')
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records is None:
            raise EntityNotFoundException(self._table_name)
        marks = []
        for record in list(records):
            student_id = record[0]
            subject_id = record[1]
            info = MarkInfo()
            info.mid = float(record[2])
            info.end = float(record[3])
            info.rate = float(record[4])
            marks.append(Mark(student_id=student_id, subject_id=subject_id, info=info))
        print(f'results: {len(marks)}')
        return marks

    def save(self, info: MarkInfo) -> Mark:
        query = f'insert into {self._table_name} '\
            + f'({self._primary_key[0]}, {self._primary_key[1]}, '\
            + f'{self.__col_mid}, {self.__col_end}, {self.__col_rate}) '\
            + f'values (%i, %s, %f, %f, %f);'
        print(f'query: {query}')
        values = (info.student_id, info.subject_id, info.mid, info.end, info.rate)
        self.cursor.execute(query, values)
        self._connection.commit()
        return Mark(student_id=info.student_id, subject_id=info.subject_id, info=info)