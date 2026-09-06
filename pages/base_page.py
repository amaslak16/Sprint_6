from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.find_clickable(locator).click()

    def fill(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def scroll_to_element(self, locator):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @staticmethod
    def format_locator(locator, **kwargs):
        by, value = locator
        return by, value.format(**kwargs)
