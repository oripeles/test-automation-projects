import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestLoginValidUser(BaseTest):
    @pytest.mark.order(2)
    def test_login_valid_user(self, driver):
        data = load_json("user_data")
        password = data["existing_user"]["password"]
        email = data["existing_user"]["email"]

        home = HomePage(driver)
        login = home.click_login_tab()
        assert login.verify_login_title_visible(), "'verify login title visible' not visible"
        login.enter_email_and_password(email,password)
        login.click_login_button()


