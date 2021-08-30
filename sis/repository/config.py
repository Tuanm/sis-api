from enum import Enum


class TableNames(Enum):
    STUDENT = 'student'
    SUBJECT = 'subject'
    MARK = 'mark'


class StudentColumns(Enum):
    ID = 'id'
    NAME = 'name'
    BIRTHDAY = 'birthday'
    GENDER = 'gender'
    EMAIL = 'email'


class SubjectColumns(Enum):
    ID = 'id'
    NAME = 'name'
    SEMESTER = 'semester'
    CREDITS = 'credits'


class MarkColumns(Enum):
    STUDENT_ID = 'student_id'
    SUBJECT_ID = 'subject_id'
    MID_POINT = 'mid'
    END_POINT = 'end'
    MID_RATE = 'rate'