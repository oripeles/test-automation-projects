from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        try:
         self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
          raise AssertionError(f"Element not clickable: {locator}")

    def handle_alert(self):
        try:
            WebDriverWait(self.driver,5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            raise AssertionError(f"Element not visible (get_text): {locator}")

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise AssertionError(f"Element not visible (get_text): {locator}")

    def select_by_value(self, locator, value):
        try:
           el = self.wait.until(EC.element_to_be_clickable(locator))
           Select(el).select_by_value(str(value))
        except TimeoutException:
            raise AssertionError(f"<select> not clickable (by value): {locator}")

    def select_by_text(self, locator, text):
        try:
          el = self.wait.until(EC.element_to_be_clickable(locator))
          Select(el).select_by_visible_text(str(text))
        except TimeoutException:
            raise AssertionError(f"<select> not clickable (by text): {locator}")

    def js_click(self, locator):
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", el)
        except TimeoutException:
            raise AssertionError(f"Element not found for JS click: {locator}")
        except Exception as e:
            raise AssertionError(f"JS click failed on {locator}: {str(e)}")

    def get_value(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.get_attribute("value")

    def compare_letters_only(self, text: str) -> str:
        return "".join(text.split())

    def texts_equal(self, locator_expected, locator_actual):
        text1 = self.compare_letters_only(self.get_value(locator_expected))
        text2 = self.compare_letters_only(self.get_text(locator_actual))
        return text1 == text2

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def hover(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(el).perform()
        return el

    def count(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return len(elements)