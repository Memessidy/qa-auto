from modules.common.data_generators.reg_values_generators.generators import return_user_data
from modules.common.email_services.mailbox_interface import get_mail_box
from modules.ui.page_objects.base_page import BasePlaywright


class CreationProtonMail(BasePlaywright):
    def __init__(self):
        super().__init__()

        self.base_url = "https://account.proton.me/mail/signup?plan=free"

        self.nickname = None
        self.password = None
        self.gen = None
        self.mail_box = None
        self.full_email_name = None

    def set_user_data(self):
        self.nickname, self.password = return_user_data()
        self.gen = get_mail_box(self.nickname)

    def get_another_mail_box(self):
        try:
            self.mail_box, self.full_email_name = next(self.gen)
        except StopIteration as exc:
            raise StopIteration('All services has been used')

    def create_new_user_start_page(self):
        self.page.get_by_test_id("dropdown-button").click()
        self.page.get_by_role("button", name="English").click()
        (self.page.frame_locator("iframe[title=\"Username\"]")
         .get_by_test_id("input-input-element").fill(self.nickname))

        password_field = self.wait_for_element_by_id(self.page, element_id='password')
        password_field.fill(self.password)

        repeat_password = self.wait_for_element_by_id(self.page, element_id='repeat-password')
        repeat_password.fill(self.password)

        self.page.get_by_label("Repeat password").fill(self.password)
        self.page.get_by_role("button", name="Create account").click()

    def continue_registration_using_email_page(self):
        email_button = self.page.get_by_test_id("tab-header-email-button")
        if email_button:
            email_button.click()

        self.page.get_by_test_id("input-input-element").fill(self.full_email_name)
        self.page.get_by_role("button", name="Get verification code").click()
        alert_text = self.page.locator('[role="alert"]').first.inner_text()

        problems_messages = ['Email address verification temporarily disabled',
                             'Sending to email address failed',
                             'Email address verification temporarily disabled for this email domain']

        if any((msg in alert_text for msg in problems_messages)):
            raise Exception("This domain is not enable now. Please try another domain from services")
        return True

    def insert_verification_code_page(self):
        verification_code = self.mail_box.get_verification_code()
        print(f"Verification code: {verification_code}")
        self.page.get_by_test_id("input-input-element").fill(verification_code)
        self.page.get_by_role("button", name="Verify").click()

    def continue_verification_pages(self):
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Maybe later").click()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.wait_for_load_state('networkidle')

    def skip_another_features_pages(self):
        self.page.get_by_role("button", name="Next", exact=True).click()
        self.page.get_by_role("button", name="Next", exact=True).click()
        self.page.get_by_role("button", name="Skip").click()
        self.page.wait_for_load_state('networkidle')

    def prepare_registration_data(self):
        self.set_user_data()
        self.get_another_mail_box()
