from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_firefox_binary():
    snap_firefox = Path("/snap/firefox/current/usr/lib/firefox/firefox")
    if snap_firefox.exists():
        return str(snap_firefox)

    firefox_versions = sorted(Path("/snap/firefox").glob("*/usr/lib/firefox/firefox"))
    if firefox_versions:
        return str(firefox_versions[-1])

    return None


@pytest.fixture
def driver():
    options = Options()
    firefox_binary = get_firefox_binary()
    if firefox_binary:
        options.binary_location = firefox_binary
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()
