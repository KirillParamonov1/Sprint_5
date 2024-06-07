from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import StellarBurgersServiceTestData
from Emails import generate_emails
from conftest import driver
from conftest import class_loc
import URLS


class TestStellarBurgersRegistration:
    def test_completed_registration(self, driver, class_loc):
        driver.get(URLS.URL + "/register")
        driver.find_element(*class_loc.USER_NAME_INPUT).send_keys(StellarBurgersServiceTestData.NAME)
        email = generate_emails()
        driver.find_element(*class_loc.USER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*class_loc.USER_PASSWORD_INPUT).send_keys("paramonov123")
        driver.find_element(*class_loc.REG_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.AUTH_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(email)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys("paramonov123")
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_ORDER_BUTTON))

        assert driver.find_element(*class_loc.MAIN_PAGE_ORDER_BUTTON)

    def test_check_incorrect_password(self, driver, class_loc):
        driver.get(URLS.URL + "/register")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.REG_BUTTON))
        driver.find_element(*class_loc.USER_NAME_INPUT).send_keys(StellarBurgersServiceTestData.NAME)
        email = generate_emails()
        driver.find_element(*class_loc.USER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*class_loc.USER_PASSWORD_INPUT).send_keys("kp")
        driver.find_element(*class_loc.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.REG_PAGE_ERROR_MESSAGE))

        assert driver.find_element(*class_loc.REG_PAGE_ERROR_MESSAGE)