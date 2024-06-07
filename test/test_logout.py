from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import StellarBurgersServiceTestData
from conftest import driver
from conftest import class_loc
import URLS


class TestLogOutInAccountStellarBurgers:
    def test_check_button_exit_in_account(self, driver, class_loc):
        driver.get(URLS.URL + "/login")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.HEADER_LOGIN))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_ORDER_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_PROFILE_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_MENU_ITEM_PROFILE))
        driver.find_element(*class_loc.PROFILE_PAGE_EXIT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.AUTH_PAGE_LOGIN_FIELD))

        assert driver.find_element(*class_loc.HEADER_LOGIN)