import pytest
from modules.api.clients.github import Github
from modules.common.database import Database
from modules.ui.page_objects.amazon_page import AmazonPage
from modules.ui.page_objects.protonmail_creation_pages import CreationProtonMail
from modules.ui.page_objects.protonmail_pages import SignInNewProtonmail
from modules.ui.page_objects.rozetka_page import RozetkaPage


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


@pytest.fixture(scope='module')
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


@pytest.fixture(scope='module')
def protonmail():
    ui = SignInNewProtonmail()
    yield ui
    ui.close()


@pytest.fixture(scope='module')
def amazon():
    ui = AmazonPage()
    ui.go_to()
    yield ui
    ui.close()


@pytest.fixture(scope='module')
def rozetka():
    ui = RozetkaPage()
    ui.go_to()
    yield ui
    ui.close()


@pytest.fixture
def rozetka_with_one_product():
    ui = RozetkaPage()
    ui.add_new_product_to_cart('iPhone 15')
    yield ui
    ui.close()


@pytest.fixture
def protonmail_creation_playwright():
    ui = CreationProtonMail()
    ui.prepare_registration_data()
    ui.go_to(ui.base_url)
    ui.create_new_user_start_page()
    yield ui
    ui.close_session()


@pytest.fixture
def protonmail_full_creation_playwright():
    ui = CreationProtonMail()
    ui.prepare_registration_data()
    ui.go_to(ui.base_url)
    ui.create_new_user_start_page()
    ui.continue_registration_using_email_page()
    ui.insert_verification_code_page()
    ui.continue_verification_pages()
    ui.skip_another_features_pages()
    yield ui
    ui.close_session()
