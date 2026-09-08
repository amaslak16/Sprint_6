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

    def fill_and_press_enter(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)
        element.send_keys("\ue007")

    def scroll_to_element(self, locator):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_current_window(self):
        return self.driver.current_window_handle

    def wait_for_windows_count(self, windows_count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda _: len(self.driver.window_handles) == windows_count
        )

    def switch_to_new_window(self, current_window):
        new_window = next(
            window for window in self.driver.window_handles if window != current_window
        )
        self.driver.switch_to.window(new_window)

    def wait_for_url_contains(self, expected_url_part, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda _: expected_url_part in self.driver.current_url,
            f"Current URL does not contain {expected_url_part}: {self.driver.current_url}",
        )

    def is_url_contains(self, expected_url_part):
        return expected_url_part in self.driver.current_url

    def is_url_equal(self, expected_url):
        return self.driver.current_url == expected_url

    @staticmethod
    def format_locator(locator, **kwargs):
        by, value = locator
        return by, value.format(**kwargs)
