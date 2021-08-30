from sis.service.mark import MarkService
from sis.service.subject import SubjectService
from sis.service.base import BaseService
from sis.service.student import StudentService
from sis.json.base import *
from flask import Flask, request
from config import AppConfig


student_service: BaseService = StudentService()
subject_service: BaseService = SubjectService()
mark_service: BaseService = MarkService()

app = Flask(__name__)


@app.route('/')
def index():
    return str(app), 200


@app.route('/students', methods=['GET'])
def load_students():
    try:
        result = student_service.find_all()
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/students/<id>', methods=['GET'])
def load_student(id: int):
    try:
        result = student_service.find_by_id(id=id)
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/students/add', methods=['POST'])
def add_student():
    info = decode(request.json)
    result = student_service.save(info)
    return encode(result), 200


@app.route('/subjects', methods=['GET'])
def load_subjects():
    try:
        result = subject_service.find_all()
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/subjects/<id>', methods=['GET'])
def load_subject(id: str):
    try:
        result = subject_service.find_by_id(id=id)
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/subjects/add', methods=['POST'])
def add_subject():
    info = decode(request.json)
    result = subject_service.save(info)
    return encode(result), 200


@app.route('/marks', methods=['GET'])
def load_marks():
    try:
        result = mark_service.find_all()
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/marks/<student_id>/<subject_id>', methods=['GET'])
def load_mark(student_id: int, subject_id: str):
    try:
        result = mark_service.find_by_id((student_id, subject_id))
        return encode(result), 200
    except Exception as exception:
        return encode(exception), 404


@app.route('/marks/add', methods=['POST'])
def add_mark():
    info = decode(request.json)
    result = subject_service.save(info)
    return encode(result), 200


if __name__ == '__main__':
    app.run(
        host=str(AppConfig.HOST.value),
        port=str(AppConfig.PORT.value),
        debug=bool(AppConfig.DEBUG.value)
    )