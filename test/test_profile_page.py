from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import StellarBurgersServiceTestData
from conftest import driver
from conftest import class_loc
import URLS


class TestProfilePageStellarBurgers:

    def test_check_open_profile_from_main_page(self, driver, class_loc):
        driver.get(URLS.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.AUTH_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON)

        assert driver.find_element(*class_loc.HEADER_LOGIN)

    def test_check_transfer_from_account_page_to_constructor(self, driver, class_loc):
        driver.get(URLS.URL + "/login")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.HEADER_LOGIN))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_PROFILE_LINK))
        driver.find_element(*class_loc.MAIN_PAGE_PROFILE_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.PROFILE_PAGE_CONSTRUCTOR_LINK))
        driver.find_element(*class_loc.PROFILE_PAGE_CONSTRUCTOR_LINK).click()

        assert driver.find_element(*class_loc.PROFILE_PAGE_CONSTRUCTOR_LINK)

    def test_check_transfer_from_account_page_to_logo_stellarburgers(self, driver, class_loc):
        driver.get(URLS.URL + "/login")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.HEADER_LOGIN))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_PROFILE_LINK))
        driver.find_element(*class_loc.MAIN_PAGE_PROFILE_LINK).click()

        driver.find_element(*class_loc.PROFILE_PAGE_LOGO_LINK)

        assert driver.find_element(*class_loc.PROFILE_PAGE_LOGO_LINK)