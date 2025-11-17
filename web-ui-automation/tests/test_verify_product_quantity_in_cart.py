import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

class TestVerifyAllProductsDetail(BaseTest):
    @pytest.mark.order(13)
    def test_verify_verify_product_quantity_in_cart(self, driver):
        qty = "4"
        home = HomePage(driver)
        product = home.click_view_product()
        product.set_quantity(qty)
        product.click_add_to_cart()
        product.click_continue_shopping()
        card = home.go_to_cart()
        card.verify_that_product_is_displayed()
