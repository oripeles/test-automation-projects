import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestSearchProduct(BaseTest):
    @pytest.mark.order(9)
    def test_search_product(self, driver):
        product_search = "Men Tshirt"
        home = HomePage(driver)
        product = home.click_product_tab()
        assert product.verify_cases_test_title_visible(), "'ALL PRODUCTS' not visible"
        product.search_product(product_search)
        product.search_product_click()
        assert product.verify_cases_test_title_visible(), "'SEARCHED PRODUCTS' not visible"
        assert product.verify_products_related_to_search_are_visible(), "The displayed product does not match the searched text"