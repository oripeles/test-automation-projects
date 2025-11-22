import pytest
from pages.home_page import HomePage

BASE_URL = "https://www.automationexercise.com/"


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_base_home_page(self, driver):
        driver.get(BASE_URL)
        home = HomePage(driver)
        assert home.verify_home_page_visible(), "Home page not active or visible"

