import allure
import pytest

from data import BASE_URL, FAQ_ANSWERS
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.title("Ответ в FAQ соответствует выбранному вопросу")
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_ANSWERS)
    def test_faq_answer_text(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        main_page.open_faq_question(question_index)

        assert main_page.get_faq_answer_text(question_index) == expected_answer
