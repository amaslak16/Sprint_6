import allure
import pytest
from typing import Any

from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL, ORDER_DATA
from pages.header import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage


def wait_for_new_window(driver, windows_count):
    def check_window_count(_: Any):
        return len(driver.window_handles) == windows_count

    return check_window_count


def wait_for_url_contains(expected_url_part):
    def check_url(driver: Any):
        return expected_url_part in driver.current_url

    return check_url


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Успешный заказ самоката через верхнюю и нижнюю кнопку Заказать")
    @pytest.mark.parametrize(
        "order_button, order",
        [
            ("top", ORDER_DATA[0]),
            ("bottom", ORDER_DATA[1]),
        ],
    )
    def test_successful_order(self, driver, order_button, order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        if order_button == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_customer_data(order)
        order_page.click_next_button()
        order_page.fill_rent_data(order)
        order_page.submit_order()

        assert order_page.is_success_modal_displayed()

    @allure.title("Логотип Самоката ведет на главную страницу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        header = Header(driver)
        main_page.open(f"{BASE_URL}order")
        main_page.accept_cookies()

        header.click_scooter_logo()

        assert driver.current_url == BASE_URL

    @allure.title("Логотип Яндекса открывает главную страницу Дзена в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        header = Header(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        current_window = driver.current_window_handle

        header.click_yandex_logo()
        WebDriverWait(driver, 10).until(wait_for_new_window(driver, 2))
        new_window = next(
            window for window in driver.window_handles if window != current_window
        )
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 10).until(wait_for_url_contains("dzen.ru"))

        assert "dzen.ru" in driver.current_url
