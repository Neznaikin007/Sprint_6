import pytest
from selenium import webdriver
import curl
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get(curl.MAIN_PAGE_URL)
    yield driver
    driver.quit()
