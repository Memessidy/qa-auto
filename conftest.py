import pytest
from modules.api.clients.github import Github
from modules.common.database import Database

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Yehor'
        self.second_name = 'Mukomel'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = Github()
    yield api


@pytest.fixture
def db():
    db = Database()
    yield db
    db.connection.close()


@pytest.fixture
def updated_orders():
    db = Database()
    db.add_new_order_now(2, 2, 3)

    yield db

    db.delete_order_by_id(2)


@pytest.fixture
def updated_products():
    db = Database()
    db.insert_multiple_products()

    yield db

    db.delete_new_products()
