from decimal import *
import random
from selenium.webdriver.common.by import By

from domain.product import Product
from domain.promo_product import PromoProduct
from pages.page_base import PageBase
from pages.add_to_cart_overlay_page import AddToCartOverlayPage


class DressesCategoryPage(PageBase):

    NTH_PRODUCT = (By.CSS_SELECTOR, 'ul.product_list>li:nth-child({})')
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, '.product-container')
    PROMO_PRODUCT = (By.XPATH, '//div[@class="product-container"][div[div[div[@class="content_price"][span[@class="price-percent-reduction"]]]]]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-name')
    DISCOUNT_BADGE = (By.CSS_SELECTOR, '.price-percent-reduction')
    CURRENT_PRICE = (By.CSS_SELECTOR, '.price')
    OLD_PRICE = (By.CSS_SELECTOR, '.old-price')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a.ajax_add_to_cart_button')
    ADD_TO_CART_POPUP = (By.CSS_SELECTOR, '.layer_cart')

    def __init__(self, driver):
        super().__init__(driver)

    def get_random_page_product_number(self):
        products_count = len(self.driver.find_elements(*self.PRODUCT_CONTAINER))
        return random.randrange(1, products_count+1)

    def get_nth_product(self, number):
        product = self.driver.find_element(self.NTH_PRODUCT[0], self.NTH_PRODUCT[1].format(str(number)))

        name = self.__get_product_name(product)
        current_price = Decimal(self.__get_current_price(product))

        return Product(name=name, current_price=current_price)

    def add_product_to_cart(self, number):
        product = self.driver.find_element(self.NTH_PRODUCT[0], self.NTH_PRODUCT[1].format(str(number)))
        product_name = self.__get_product_name(product)

        self.driver_extensions.hover_element(product)
        add_to_cart_btn = product.find_element(*self.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

        print("Product \"" + product_name + "\" added to cart")
        return AddToCartOverlayPage(self.driver)

    def get_list_of_promo_products(self):
        self.driver_extensions.wait_until_visible(self.PROMO_PRODUCT)
        promo_products = self.driver.find_elements(*self.PROMO_PRODUCT)

        products_list = []

        for product in promo_products:
            name = self.__get_product_name(product)
            old_price = Decimal(self.__get_old_price(product))
            current_price = Decimal(self.__get_current_price(product))
            discount_percent = self.__get_displayed_discount_percent(product)
            products_list.append(PromoProduct(name=name, current_price=current_price, old_price=old_price, discount_percent=discount_percent))

        return products_list

    def __get_product_name(self, product):
        product_name = product.find_element(*self.PRODUCT_NAME).get_attribute('title')
        return product_name

    def __get_displayed_discount_percent(self, product):
        discount_text = product.find_element(*self.DISCOUNT_BADGE).get_attribute('innerText')
        discount_value = ''.join([n for n in discount_text if n.isdigit()])
        return int(discount_value)

    def __get_old_price(self, product):
        old_price = product.find_element(*self.OLD_PRICE).get_attribute('innerText')
        return old_price.replace('$', '')

    def __get_current_price(self, product):
        current_price = product.find_element(*self.CURRENT_PRICE).get_attribute('innerText')
        return current_price.replace('$', '')
