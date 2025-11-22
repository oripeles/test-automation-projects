import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestSubscriptionFromCard(BaseTest):
    @pytest.mark.order(11)
    def test_subscription(self, driver):
        data = load_json("user_data")
        email = data["existing_user"]["email"]
        home = HomePage(driver)
        cart = home.go_to_cart()
        cart.scroll_down_to_footer()
        assert cart.is_subscription_title_visible(), "SUBSCRIPTION not visible"
        cart.subscribe(email)
        assert cart.is_subscription_success_visible(), "Success message not visible"