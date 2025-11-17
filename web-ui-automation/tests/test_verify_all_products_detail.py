import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestVerifyAllProductsDetail(BaseTest):
    @pytest.mark.order(8)
    def test_verify_all_products_detail(self, driver):
        home = HomePage(driver)
        product = home.click_product_tab()
        assert product.verify_cases_test_title_visible(), "'ALL PRODUCTS' not visible"
        assert product.verify_view_product_visible(), "'The products list is visible' not visible"
        product.click_product_view()
