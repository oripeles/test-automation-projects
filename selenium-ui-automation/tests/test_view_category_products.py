import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

class TestViewCategoryProduct(BaseTest):
    @pytest.mark.order(14)
    def test_view_category_products(self, driver):
        home = HomePage(driver)
        assert home.verify_left_sidebar_visible(), "'categories on left side bar' not visible"
        home.click_women_category()
        home.click_dress_category()
        assert home.verify_category_title_women_visible(), "'categories women' not visible"
        home.click_men_category()
        home.click_shirt_category()
        assert home.verify_category_title_men_visible(), "'categories men' not visible"

