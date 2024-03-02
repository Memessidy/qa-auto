import pytest


@pytest.mark.ui_playwright
def test_create_new_account(protonmail_full_creation_playwright):
    assert protonmail_full_creation_playwright.nickname in protonmail_full_creation_playwright.page.title()
