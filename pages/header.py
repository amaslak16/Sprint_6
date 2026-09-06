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
