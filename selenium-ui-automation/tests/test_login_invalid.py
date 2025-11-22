import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestLoginInvalidUser(BaseTest):
    @pytest.mark.order(4)
    def test_login_invalid_user(self, driver):
        cases = load_json("invalid_logins")
        home = HomePage(driver)
        login = home.click_login_tab()
        assert login.verify_login_title_visible(), "'verify login title visible' not visible"
        for case in cases:
            email = case["email"]
            password = case["password"]
            login.enter_email_and_password(email, password)
            login.click_login_button()
            assert login.verify_login_incorrect_title_visible(), "'Your email or password is incorrect!' not visible"