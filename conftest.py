import pytest
import URLS
from selenium import webdriver
from locators import StellarBurgersLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(URLS.URL)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def class_loc():
    class_loc = StellarBurgersLocators()
    return class_loc