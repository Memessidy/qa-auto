import pytest


@pytest.mark.ui_playwright
def test_create_acc_using_email_services_is_available(protonmail_creation_playwright):
    protonmail_creation_playwright.get_another_mail_box()
    assert protonmail_creation_playwright.continue_registration_using_email_page()
