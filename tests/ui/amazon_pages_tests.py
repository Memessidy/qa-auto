from modules.ui.page_objects.amazon_page import AmazonPage
import pytest


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
