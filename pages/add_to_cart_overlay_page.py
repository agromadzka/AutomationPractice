from selenium.webdriver.common.by import By

from pages.page_base import PageBase
from pages.cart_page import CartPage


class AddToCartOverlayPage(PageBase):

    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_to_checkout_btn(self):
        self.driver_extensions.click_visible(self.PROCEED_CHECKOUT_BTN)
        return CartPage(self.driver)

