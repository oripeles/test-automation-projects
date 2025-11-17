import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCasesTest(BaseTest):
    @pytest.mark.order(7)
    def test_cases_test(self, driver):
        home = HomePage(driver)
        cases = home.click_test_cases_tab()
        assert cases.verify_cases_test_title_visible(), "'test cases' not visible"

