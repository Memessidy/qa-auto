from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from playwright.sync_api import sync_playwright


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


class BasePlaywright:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.timeout = 80_000

    def go_to(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    def wait_for_element_by_id(self, page, element_id):
        return page.wait_for_selector(f'#{element_id}', state='visible', timeout=self.timeout)

    def close_session(self):
        self.page.close()
        self.context.close()
        self.browser.close()
