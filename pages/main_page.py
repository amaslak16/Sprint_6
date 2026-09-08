import allure

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Открыть вопрос FAQ")
    def open_faq_question(self, index):
        question_locator = self.format_locator(MainPageLocators.FAQ_QUESTION, index=index)
        self.scroll_to_element(question_locator)
        self.click(question_locator)

    @allure.step("Получить текст ответа FAQ")
    def get_faq_answer_text(self, index):
        answer_locator = self.format_locator(MainPageLocators.FAQ_ANSWER, index=index)
        return self.find_visible(answer_locator).text
