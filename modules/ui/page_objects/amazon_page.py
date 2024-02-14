from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from modules.ui.page_objects import xpath_pathes


class AmazonPage(BasePage):
    URL = "https://www.amazon.in/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def find_search_field(self):
        search_field = self.search_element(By.ID, "twotabsearchtextbox")
        search_button = self.search_element(By.ID, "nav-search-submit-button")
        return search_field, search_button

    def find_product(self, product_name):
        field, button = self.find_search_field()
        field.send_keys(product_name)
        button.click()
        self.search_element(By.XPATH, xpath_pathes.AMAZON_PRODUCT_XPATH).click()

    def check_title(self, expected_title: str) -> bool:
        return self.driver.title == expected_title

    def check_enabled_search_field(self) -> bool:
        return all((self.find_search_field()))

    def test_buy_button(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        btn = self.search_element(By.ID, 'buy-now-button')
        btn.click()

    def check_substring_in_title(self, expected_substring: str) -> bool:
        return expected_substring.casefold() in self.driver.title

