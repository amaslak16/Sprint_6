import allure

from locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить данные пользователя")
    def fill_customer_data(self, order):
        self.fill(OrderPageLocators.FIRST_NAME_INPUT, order["first_name"])
        self.fill(OrderPageLocators.LAST_NAME_INPUT, order["last_name"])
        self.fill(OrderPageLocators.ADDRESS_INPUT, order["address"])
        self.fill(OrderPageLocators.METRO_INPUT, order["metro"])
        metro_locator = self.format_locator(OrderPageLocators.METRO_OPTION, station=order["metro"])
        self.click(metro_locator)
        self.fill(OrderPageLocators.PHONE_INPUT, order["phone"])

    @allure.step("Перейти к данным аренды")
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды")
    def fill_rent_data(self, order):
        self.fill_and_press_enter(OrderPageLocators.DELIVERY_DATE_INPUT, order["date"])
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        period_locator = self.format_locator(OrderPageLocators.RENT_PERIOD_OPTION, period=order["period"])
        self.click(period_locator)
        color_locator = (
            OrderPageLocators.BLACK_COLOR_CHECKBOX
            if order["color"] == "black"
            else OrderPageLocators.GREY_COLOR_CHECKBOX
        )
        self.click(color_locator)
        self.fill(OrderPageLocators.COMMENT_INPUT, order["comment"])

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_success_modal_displayed(self):
        return self.find_visible(OrderPageLocators.SUCCESS_MODAL).is_displayed()

    @allure.step("Оформить заказ")
    def create_order(self, order):
        self.fill_customer_data(order)
        self.click_next_button()
        self.fill_rent_data(order)
        self.submit_order()
