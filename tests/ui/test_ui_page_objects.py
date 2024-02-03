from modules.ui.page_objects.sign_in_page import SignInPage
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


# Індивідуальна частина

# TODO перевіряє, чи пошта нова (нещодавно зареєстрована)
# TODO перевіряється, чи користувач натискав next при ознайломленні з новими функціями
# TODO щоб не був постійно 1 непройдений тест я його коментую
@pytest.mark.ui
def test_is_new_protonmail(protonmail):
    assert protonmail.login_to_protonmail()


@pytest.mark.ui
def test_check_login(protonmail):
    protonmail.login_to_protonmail()
    assert protonmail.check_success_login()


@pytest.mark.ui
def test_new_messages(protonmail):
    protonmail.login_to_protonmail()
    assert protonmail.get_unread_messages() > 0


@pytest.mark.ui
def test_delete_messages(protonmail):
    protonmail.login_to_protonmail()
    time.sleep(5)  # TODO  Тут sleep, просто цей самий тест без нього інколи не працює
    messages_count = protonmail.get_unread_messages()
    print(f'Кількість повідомлень: {messages_count}')
    protonmail.delete_all_messages()
    messages_count = protonmail.get_unread_messages()
    print(f'Повідомлення були видалені. Кількість повідомлень зараз: {messages_count}')
    assert messages_count == 0
