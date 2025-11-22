import pytest

from tests.base_test import BaseTest
from pages.home_page import HomePage

class TestRemoveProductsFromCart(BaseTest):
    @pytest.mark.order(15)
    def test_remove_products_from_cart(self, driver):
        home = HomePage(driver)
        product = home.click_product_tab()
        product.add_first_product_to_cart()
        product.continue_shopping()
        cart = product.open_cart()
        cart.click_delete()
        assert cart.verify_that_product_is_removed_from_the_cart(), "'product is not removed from the cart'"


