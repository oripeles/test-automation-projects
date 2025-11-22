from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.email_generator import generate_unique_email
from utilities.json_loader import load_json
import pytest

class TestRegisterUser(BaseTest):
    @pytest.mark.order(1)
    def test_register_user(self, driver):
        email = generate_unique_email()
        data = load_json("user_data")
        password = data["existing_user"]["password"]
        name = data["existing_user"]["name"]
        gender = "Mr"
        date_data = {
            "day": 10,
            "month": "January",
            "year": "2000"
        }
        address_data = {
            "first": "Ori",
            "last": "Peles",
            "company": "global",
            "addr1": "123 Test Street",
            "addr2": "Building 4",
            "country": "Israel",
            "state": "Center",
            "city": "Petah Tikva",
            "zipcode": "4950000",
            "mobile": "0501234567"
        }

        home = HomePage(driver)
        login = home.click_login_tab()
        assert login.verify_signup_title_visible(), "'New User Signup!' not visible"
        login.enter_name_and_email(name, email)
        info = login.click_signup_button()
        assert info.verify_account_title_visible(), "'Enter Account Information' not visible"
        info.select_title(gender)
        info.fill_password(password)
        info.select_date(**date_data)
        info.select_newsletter()
        info.select_optin()
        info.fill_details(**address_data)
        created = info.click_create_account_button()
        assert created.verify_account_title_visible(), "'ACCOUNT CREATED!' not visible"
        created.click_created_account_button()
        assert home.verify_Logged_in_as_username_visible(), "'Logged in as username' not visible or wrong name"
        delete_account =  home.click_delete_account()
        assert delete_account.verify_account_deleted_title_visible(),"'Account Deleted!' not visible"
        delete_account.click_deleted_account_button()





