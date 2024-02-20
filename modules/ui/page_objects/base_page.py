from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)

    def close(self) -> None:
        self.driver.close()

    def wait_for_element(self, by_what, context):
        element = self.wait.until(
            EC.presence_of_element_located((by_what, context)))
        return element
