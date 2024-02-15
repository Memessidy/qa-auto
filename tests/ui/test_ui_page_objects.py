from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.amazon_page import AmazonPage
import pytest
import time


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему Github
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()


# Individual part

# Protonmail
# TODO перевіряє, чи пошта нова (нещодавно зареєстрована)
# TODO перевіряється, чи користувач натискав next при ознайломленні з новими функціями
# TODO щоб не був постійно 1 непройдений тест я його коментую
@pytest.mark.ui
def test_is_new_protonmail(protonmail):
    assert protonmail.login_to_protonmail()


@pytest.mark.ui
def test_check_login(protonmail_with_login):
    assert protonmail_with_login.check_success_login()


@pytest.mark.ui
def test_new_messages(protonmail_with_login):
    assert protonmail_with_login.get_unread_messages() > 0


@pytest.mark.ui
def test_delete_messages(protonmail_with_login):
    time.sleep(5)  # TODO  Тут sleep, просто цей самий тест без нього інколи не працює
    messages_count = protonmail_with_login.get_unread_messages()
    print(f'Кількість повідомлень: {messages_count}')
    protonmail_with_login.delete_all_messages()
    messages_count = protonmail_with_login.get_unread_messages()
    print(f'Повідомлення були видалені. Кількість повідомлень зараз: {messages_count}')
    assert messages_count == 0


# Amazon part

class AmazonTestObject:
    def __init__(self):
        self.amazon_page = AmazonPage()
        self.amazon_page.go_to()


amazon_obj = AmazonTestObject()


@pytest.mark.ui
def test_search_field_enabled():
    global amazon_obj
    assert amazon_obj.amazon_page.check_enabled_search_field()


@pytest.mark.ui
def test_find_product_by_name():
    global amazon_obj
    product_name = 'iphone 15'
    amazon_obj.amazon_page.find_product(product_name)
    assert amazon_obj.amazon_page.check_substring_in_title(product_name)


@pytest.mark.ui
def test_buy_button():
    global amazon_obj
    amazon_obj.amazon_page.test_buy_button()
    assert amazon_obj.amazon_page.check_title('Amazon Sign In')
    amazon_obj.amazon_page.close()
