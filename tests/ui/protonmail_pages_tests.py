import pytest


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
    messages_count = protonmail_with_login.get_unread_messages()
    print(f'Кількість повідомлень: {messages_count}')
    protonmail_with_login.delete_all_messages()
    messages_count = protonmail_with_login.get_unread_messages()
    print(f'Повідомлення були видалені. Кількість повідомлень зараз: {messages_count}')
    assert messages_count == 0
