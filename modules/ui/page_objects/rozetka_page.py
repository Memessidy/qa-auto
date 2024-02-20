from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RozetkaPage(BasePage):
    URL = "https://rozetka.com.ua/ua/"

    def __init__(self) -> None:
        super().__init__()
        self.product_link = None
        self.product_name = None
        self.prices = dict()

    def go_to(self):
        self.driver.get(self.URL)

    def find_search_field(self):
        search_field = self.wait_for_element(By.NAME, "search")
        search_button = self.wait_for_element(By.XPATH, "//button[contains(text(),'Знайти')]")
        return search_field, search_button

    def find_product(self, product_name):
        self.product_name = product_name
        field, button = self.find_search_field()
        field.send_keys(product_name)
        button.click()
        product_link = self.wait_for_element(
            By.XPATH, f"//a[contains(@title,'{product_name}')]").get_attribute('href')
        self.product_link = product_link

    def open_product_page(self):
        self.driver.get(self.product_link)

    @staticmethod
    def parse_text_price_ro_int(value):
        return int(value[:-1].replace(" ", ""))

    def save_product_price(self):
        price = self.wait_for_element(By.CLASS_NAME, "product-price__big").text
        price = self.parse_text_price_ro_int(price)
        self.prices[self.product_name] = price

    def find_buy_button(self):
        return self.wait_for_element(By.XPATH, "//button[@aria-label='Купити']")

    def add_product_to_cart(self):
        button = self.find_buy_button()
        button.click()

    def add_one_more_product(self):
        add_one_more_button = self.wait_for_element(By.XPATH, "//button[@aria-label='Додати ще один товар']")
        add_one_more_button.click()

    def delete_one_more_product(self):
        delete_one_more_button = self.wait_for_element(By.XPATH, "//button[@aria-label='Видалити один товар']")
        delete_one_more_button.click()

    def get_product_count_in_cart(self):
        return int(self.wait_for_element(By.XPATH, "//input[@type='number']").get_attribute('value'))

    def delete_product_from_cart(self):
        self.wait_for_element(By.ID, "cartProductActions0").click()
        self.wait_for_element(
            By.XPATH, "//button[@class='button button--medium button--with-icon button--link']").click()

    def find_full_price(self):
        element = self.wait_for_element(
            By.CLASS_NAME, "cart-receipt__sum-price").find_element(By.XPATH, ".//span")
        full_price = element.text
        full_price = self.parse_text_price_ro_int(full_price)
        return full_price

    def check_cart_is_empty(self):
        cart_text = self.wait_for_element(By.CLASS_NAME, "cart-dummy__heading").text
        return cart_text == 'Кошик порожній'

    def add_new_product_to_cart(self, product_name):
        self.go_to()
        self.find_product(product_name)
        self.open_product_page()
        self.save_product_price()
        self.find_buy_button()
        self.add_product_to_cart()
