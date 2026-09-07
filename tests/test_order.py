import allure

from data import BASE_URL, ORDER_DATA
from pages.header import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Успешный заказ самоката через верхнюю кнопку Заказать")
    def test_successful_order_by_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.create_order(ORDER_DATA[0])

        assert order_page.is_success_modal_displayed()

    @allure.title("Успешный заказ самоката через нижнюю кнопку Заказать")
    def test_successful_order_by_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.create_order(ORDER_DATA[1])

        assert order_page.is_success_modal_displayed()

    @allure.title("Логотип Самоката ведет на главную страницу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        header = Header(driver)
        main_page.open(f"{BASE_URL}order")
        main_page.accept_cookies()

        header.click_scooter_logo()

        assert header.is_scooter_page_opened(BASE_URL)

    @allure.title("Логотип Яндекса открывает главную страницу Дзена в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        header = Header(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        header.open_dzen_by_yandex_logo()

        assert header.is_dzen_opened()
