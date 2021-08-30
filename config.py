from enum import Enum
import decouple


class MySQLConfig(Enum):
    HOST = decouple.config('DB_HOST')
    USER = decouple.config('DB_USER')
    PASSWORD = decouple.config('DB_PASSWORD')
    DATABASE = decouple.config('DB_DATABASE')


class AppConfig(Enum):
    HOST = decouple.config('APP_HOST')
    PORT = decouple.config('APP_PORT')
    DEBUG = decouple.config('APP_DEBUG')
