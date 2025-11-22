import os

import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestLogoutUser(BaseTest):
    @pytest.mark.order(3)
    def test_logout_user(self, driver):
        data = load_json("user_data")
        password = os.getenv("USER_PASSWORD")
        email = data["existing_user"]["email"]

        home = HomePage(driver)
        login = home.click_login_tab()
        assert login.verify_login_title_visible(), "'verify login title visible' not visible"
        login.enter_email_and_password(email, password)
        login.click_login_button()
        home.click_logout_tab()
        assert login.verify_login_title_visible(), "'verify login title visible' not visible"