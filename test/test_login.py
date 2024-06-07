from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import StellarBurgersServiceTestData
from conftest import driver
from conftest import class_loc
import URLS


class TestLogInStellarBurgers:
    def test_check_button_login_in_main_page(self, driver, class_loc):
        driver.get(URLS.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_LOGIN_BUTTON).click()

        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_ORDER_BUTTON))

        assert driver.find_element(*class_loc.MAIN_PAGE_ORDER_BUTTON)

    def test_check_button_personal_account(self, driver, class_loc):
        driver.get(URLS.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_PROFILE_LINK))
        driver.find_element(*class_loc.MAIN_PAGE_PROFILE_LINK).click()

        assert driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON)

    def test_check_button_login_in_form_registration(self, driver, class_loc):
        driver.get(URLS.URL + "/register")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.REG_PAGE_LOGIN_LINK))
        driver.find_element(*class_loc.REG_PAGE_LOGIN_LINK).click()

        assert driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON)

    def test_check_button_in_forgot_password(self, driver, class_loc):
        driver.get(URLS.URL + "/forgot-password")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.RECOVER_PAGE_LINK))
        driver.find_element(*class_loc.RECOVER_PAGE_LINK).click()

        assert driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON)