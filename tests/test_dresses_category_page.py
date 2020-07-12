from pages.dresses_category_page import DressesCategoryPage
from urls import Urls


class TestDressesCategoryPage:

    def test_dresses_category_pg_01_check_discount_value(self, driver):
        dresses_category_pg = DressesCategoryPage(driver)
        dresses_category_pg.navigate(Urls.dresses_category_url)

        promo_products = dresses_category_pg.get_list_of_promo_products()
        for product in promo_products:
            calculated_discount_percent = round(100 * (product.old_price - product.current_price) / product.old_price)
            assert product.discount_percent == calculated_discount_percent, \
                print('Invalid discount value for product: ' + product.name)

    def test_dresses_category_pg_02_add_random_product_to_cart(self, driver):
        dresses_category_pg = DressesCategoryPage(driver)
        dresses_category_pg.navigate(Urls.dresses_category_url)

        product_number = dresses_category_pg.get_random_page_product_number()
        product = dresses_category_pg.get_nth_product(product_number)

        add_to_cart_popup = dresses_category_pg.add_product_to_cart(product_number)
        cart_pg = add_to_cart_popup.click_proceed_to_checkout_btn()
        added_product_name = cart_pg.get_added_product_name()
        assert product.name == added_product_name
