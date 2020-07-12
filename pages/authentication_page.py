from selenium.webdriver.common.by import By

from pages.page_base import PageBase
from pages.account_page import AccountPage


class AuthenticationPage(PageBase):

    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, '#passwd')
    SIGN_IN_BTN = (By.CSS_SELECTOR, '#SubmitLogin')
    ALERT_MSG = (By.CSS_SELECTOR, '.alert-danger:not([style="display:none"])')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_email(self, email_address):
        self.driver_extensions.fill_input(self.LOGIN_EMAIL_INPUT, email_address)

    def fill_password(self, password):
        self.driver_extensions.fill_input(self.LOGIN_PASSWORD_INPUT, password)

    def sign_in_valid(self):
        self.driver_extensions.click_visible(self.SIGN_IN_BTN)
        return AccountPage(self.driver)

    def sign_in_invalid(self):
        self.driver_extensions.click_visible(self.SIGN_IN_BTN)

    def get_alert_message_text(self):
        self.driver_extensions.wait_until_visible(self.ALERT_MSG)
        return self.driver_extensions.elements_text(self.ALERT_MSG)

    def login_as(self, login, password):
        self.fill_email(login)
        self.fill_password(password)
        self.sign_in_valid()
