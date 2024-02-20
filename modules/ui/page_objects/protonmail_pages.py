from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from modules.ui.page_objects.xpath_pathes import custom_xpath

proton_account = {'alreadyeci@proton.me': 'k`JUypT8;>K'}


class SignInNewProtonmail(BasePage):
    URL = 'https://account.proton.me/login?product=mail&language=en'

    def __init__(self):
        super().__init__()
        self.proton_login, self.proton_password = tuple(proton_account.items())[0]

    def go_to(self, url):
        self.driver.get(url)

    def login_to_protonmail(self):
        is_new_email = False
        self.go_to(self.URL)

        username_filed = self.wait_for_element(By.ID, 'username')
        password_filed = self.wait_for_element(By.ID, 'password')
        btn = self.wait_for_element(By.XPATH, '//button[text() = "Sign in"]')

        username_filed.send_keys(self.proton_login)
        password_filed.send_keys(self.proton_password)
        btn.click()

        # Чекаємо, поки сторінка точно прогрузиться
        try:
            self.wait_for_element(By.XPATH, "//h1[contains(text(),'Congratulations on choosing privacy')]")
            # Скіп фіч (виникає, якщо заходимо на пошту першого разу)
            self.skip_another_features()
            is_new_email = True
        except:
            self.wait_for_element(By.XPATH, '//button[text() = "New message"]')
            is_new_email = False
        return is_new_email

    def skip_another_features(self):
        try:
            for _ in range(2):
                button = self.wait_for_element(By.XPATH, '//button[text() = "Next"]')
                button.click()
            button = self.wait_for_element(By.XPATH, '//button[text() = "Skip"]')
            button.click()
        except:
            raise ValueError('В аккаунт вже заходили')

    def check_success_login(self):
        return 'proton.me' in self.driver.title

    def check_title(self, expected_title) -> bool:
        return self.driver.title == expected_title

    def get_unread_messages(self):
        try:
            span_element = self.wait_for_element(By.XPATH, custom_xpath)
            aria_label_value = span_element.get_attribute("aria-label")
            unread_messages_count = int(aria_label_value[0])

            return unread_messages_count
        except:
            return 0

    def select_all_messages(self):
        checkbox = self.wait_for_element(By.ID, "idSelectAll")
        checkbox.click()

    def delete_all_messages(self):
        self.select_all_messages()
        delete_btn = self.wait_for_element(By.XPATH, "//button[@data-testid='toolbar:movetotrash']")
        delete_btn.click()

    def make_messages_as_read(self):
        self.select_all_messages()
        read_btn = self.wait_for_element(By.XPATH, "//button[@data-testid='toolbar:read']")
        read_btn.click()
