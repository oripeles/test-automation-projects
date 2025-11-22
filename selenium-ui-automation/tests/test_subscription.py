import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestSubscription(BaseTest):
    @pytest.mark.order(10)
    def test_subscription(self, driver):
        data = load_json("user_data")
        email = data["existing_user"]["email"]
        home = HomePage(driver)
        home.scroll_down()
        assert home.is_subscription_title_visible(), "SUBSCRIPTION not visible"
        home.subscribe(email)
        assert home.is_subscription_success_visible(), "Success message not visible"