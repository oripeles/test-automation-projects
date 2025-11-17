import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestRegisterCheckout(BaseTest):
    @pytest.mark.order(16)
    def test_register_while_checkout(self, driver):
        home = HomePage(driver)
        product = home.click_product_tab()
        product.add_first_product_to_cart()
        product.continue_shopping()
        cart = product.open_cart()
        cart.click_checkout()
        cart.click_login()


