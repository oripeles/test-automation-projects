import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestRegisterUserWithExistingEmail(BaseTest):
    @pytest.mark.order(5)
    def test_register_user_with_existing_email(self, driver):
        data = load_json("user_data")
        email = data["existing_user"]["email"]
        name = data["existing_user"]["name"]

        home = HomePage(driver)
        login = home.click_login_tab()
        assert login.verify_signup_title_visible(), "'New User Signup!' not visible"
        login.enter_name_and_email(name, email)
        login.click_signup_button()
        assert login.verify_email_exist_visible(), "'Email Address already exist!' not visible"