from selenium.webdriver.common.by import By

from pages.page_base import PageBase


class AccountPage(PageBase):

    LOG_OUT_BTN = (By.CSS_SELECTOR, 'a.logout')

    def __init__(self, driver):
        super().__init__(driver)
