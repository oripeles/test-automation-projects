import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.json_loader import load_json


class TestContactUsForm(BaseTest):
    @pytest.mark.order(6)
    def test_contact_us_form(self, driver):
        data = load_json("user_data")

        details_data = {
            "name": "Ori",
            "email": data["existing_user"]["email"],
            "subject": "QA Automation",
            "message": "123 Test"
        }
        home = HomePage(driver)
        contact = home.click_contact_us_tab()
        assert contact.verify_contact_us_page_visible(), "'verify contact us page visible' not visible"
        contact.fill_details(**details_data)
        contact.click_submit()
        contact.click_handle_alert()
        assert contact.verify_contact_us_success_page_visible(), "'verify contact us success page visible' not visible"
        contact.click_home()