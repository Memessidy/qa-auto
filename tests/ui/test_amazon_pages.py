import pytest


@pytest.mark.ui
def test_search_field_enabled(amazon):
    assert amazon.check_enabled_search_field()


@pytest.mark.ui
def test_find_product_by_name(amazon):
    product_name = 'iphone 15'
    amazon.find_product(product_name)
    assert amazon.check_substring_in_title(product_name)


@pytest.mark.ui
def test_buy_button(amazon):
    amazon.test_buy_button()
    assert amazon.check_title('Amazon Sign In')
