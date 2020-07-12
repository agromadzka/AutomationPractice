from selenium.webdriver.common.by import By
from pages.page_base import PageBase


class CartPage(PageBase):

    PRODUCT_NAME = (By.CSS_SELECTOR, '#cart_summary .product-name')

    def __init__(self, driver):
        super().__init__(driver)

    def get_added_product_name(self):
        self.driver_extensions.wait_until_visible(self.PRODUCT_NAME)
        return self.driver.find_element(*self.PRODUCT_NAME).text
