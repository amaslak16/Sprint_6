import allure
from typing import Any

from selenium.webdriver.support.ui import WebDriverWait

from locators import HeaderLocators
from pages.base_page import BasePage


def wait_for_new_window(driver, windows_count):
    def check_window_count(_: Any):
        return len(driver.window_handles) == windows_count

    return check_window_count


def wait_for_url_contains(expected_url_part):
    def check_url(driver: Any):
        return expected_url_part in driver.current_url

    return check_url


class Header(BasePage):
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)

    @allure.step("Открыть Дзен через логотип Яндекса")
    def open_dzen_by_yandex_logo(self):
        current_window = self.driver.current_window_handle
        self.click_yandex_logo()
        WebDriverWait(self.driver, 10).until(wait_for_new_window(self.driver, 2))
        new_window = next(
            window for window in self.driver.window_handles if window != current_window
        )
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(wait_for_url_contains("dzen.ru"))

    @allure.step("Проверить, что открыт Дзен")
    def is_dzen_opened(self):
        return "dzen.ru" in self.driver.current_url

    @allure.step("Проверить, что открыта главная страница Самоката")
    def is_scooter_page_opened(self, expected_url):
        return self.driver.current_url == expected_url
