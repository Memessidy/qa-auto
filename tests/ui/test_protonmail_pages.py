import pytest


# Protonmail
# TODO перевіряє, чи пошта нова (нещодавно зареєстрована)
# TODO перевіряється, чи користувач натискав next при ознайломленні з новими функціями
# TODO щоб не був постійно 1 непройдений тест я його коментую
@pytest.mark.ui
def test_is_new_protonmail(protonmail):
    is_new_protonmail = protonmail.login_to_protonmail()
    assert is_new_protonmail


@pytest.mark.ui
def test_check_login(protonmail):
    assert protonmail.check_success_login()


@pytest.mark.ui
def test_new_messages(protonmail):
    assert protonmail.get_unread_messages() > 0


@pytest.mark.ui
def test_delete_messages(protonmail):
    messages_count = protonmail.get_unread_messages()
    print(f'Кількість повідомлень: {messages_count}')
    protonmail.delete_all_messages()
    messages_count = protonmail.get_unread_messages()
    print(f'Повідомлення були видалені. Кількість повідомлень зараз: {messages_count}')
    assert messages_count == 0
