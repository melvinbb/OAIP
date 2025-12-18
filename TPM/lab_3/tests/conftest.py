import pytest
import os
import sys
import tempfile
from PyQt6.QtWidgets import QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Database
from app.addDataWin import AddDataWindow
from app.mainWin import MainWindow
from app.viewDataWin import ViewDataWindow


@pytest.fixture(scope="session")
def qapp():

    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


@pytest.fixture
def temp_db():

    db_file = tempfile.NamedTemporaryFile(suffix='.db', delete=False)
    db_path = db_file.name
    db_file.close()
    db = Database(db_path)
    yield db
    if hasattr(db, '_connection'):
        if db._connection:
            db._connection.close()


@pytest.fixture
def sample_data():

    return [
        {"name": "Евгеха", "age": 18, "grade": "Отлично"},
        {"name": "Бобер", "age": 14, "grade": "Хорошо"},
        {"name": "Асадбек", "age": 16, "grade": "Удовлетворительно"}
    ]


@pytest.fixture
def db_with_data(temp_db, sample_data):

    for data in sample_data:
        temp_db.add_student(data["name"], data["age"], data["grade"])
    return temp_db


@pytest.fixture
def main_window(qapp, temp_db):

    window = MainWindow()
    window.db = temp_db
    yield window
    window.close()


@pytest.fixture
def view_data_window(qapp, temp_db):

    window = ViewDataWindow(temp_db)
    yield window
    window.close()


@pytest.fixture
def view_data_window_with_data(qapp, db_with_data):

    window = ViewDataWindow(db_with_data)
    yield window
    window.close()


@pytest.fixture
def add_data_window(qapp, temp_db):

    window = AddDataWindow(temp_db)
    yield window
    window.close()


@pytest.fixture
def edit_data_window(qapp, db_with_data):

    students = db_with_data.get_all_students()
    student_id = students[0]["id"]
    window = AddDataWindow(db_with_data, student_id)
    yield window
    window.close()