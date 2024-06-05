import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from test.locators import client_portal, registration_button, input_name, input_email_registration, input_password, \
    registration_button_in_registration_page
from test.test_data import BASE_URL


@pytest.fixture()
def chrome():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.binary_location = r"C:\Users\kemer\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(BASE_URL)
    return driver
@pytest.fixture()
def generate_login():
    login = f"paramonov_9{(str(round(time.time())))}@gmail.com"
    return login


@pytest.fixture()
def generate_name():
    name = f"kirill_paramonov_9{(str(round(time.time())))}"
    return name


@pytest.fixture()
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(random.randint(6, 20)))
    return password


@pytest.fixture()
def registration(chrome, generate_name, generate_password, generate_login):
    chrome.find_element(By.XPATH, client_portal).click()
    chrome.find_element(By.XPATH, registration_button).click()
    chrome.find_element(By.XPATH, input_name).send_keys(generate_name)
    chrome.find_element(By.XPATH, input_email_registration).send_keys(generate_login)
    chrome.find_element(By.XPATH, input_password).send_keys(generate_password)
    chrome.find_element(By.XPATH, registration_button_in_registration_page).click()


@pytest.fixture()
def close_browser(chrome):
    yield
    chrome.quit()
