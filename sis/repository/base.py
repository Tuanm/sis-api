from enum import Enum
from typing import Any
from config import MySQLConfig
from mysql.connector.cursor import CursorBase
import mysql.connector


class BaseRepository:
    cursor: CursorBase
    _table_name: str
    _primary_key: Any

    def __init__(self, table_name: str, primary_key: Any):
        self._table_name = table_name
        self._primary_key = primary_key
        self._connection = mysql.connector.connect(
            host=MySQLConfig.HOST.value,
            user=MySQLConfig.USER.value,
            password=MySQLConfig.PASSWORD.value,
            database=MySQLConfig.DATABASE.value
        )
        self.cursor = self._connection.cursor()

    def close(self):
        self._connection.close()


class BaseRepositoryException(Exception):
    message: str


class EntityNotFoundException(BaseRepositoryException):
    def __init__(self, name: str) -> None:
        self.message = f'{name} not found'