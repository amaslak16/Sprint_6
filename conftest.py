import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()
