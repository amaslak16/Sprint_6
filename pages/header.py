import allure

from locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)

    @allure.step("Открыть Яндекс через логотип Яндекса")
    def open_yandex_by_yandex_logo(self):
        current_window = self.get_current_window()
        self.click_yandex_logo()
        self.wait_for_windows_count(2)
        self.switch_to_new_window(current_window)
        self.wait_for_url_contains("ya.ru")

    @allure.step("Проверить, что открыт Яндекс")
    def is_yandex_opened(self):
        return self.is_url_contains("ya.ru")

    @allure.step("Проверить, что открыта главная страница Самоката")
    def is_scooter_page_opened(self, expected_url):
        return self.is_url_equal(expected_url)
