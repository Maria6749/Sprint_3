from selenium import webdriver
import pytest
import random


@pytest.fixture
def user():
    user = f"Mariya_Rashchupkina_{random.randint(1000,9999)}_@yandex.ru"
    return user

@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    return driver

@pytest.fixture
def driver_register():
    driver_register = webdriver.Chrome()
    driver_register.get('https://stellarburgers.nomoreparties.site/register')
    return driver_register

@pytest.fixture
def driver_reset():
    driver_reset = webdriver.Chrome()
    driver_reset.get('https://stellarburgers.nomoreparties.site/forgot-password')
    return driver_reset

@pytest.fixture
def email():
    email = "mariiiihaa@yandex.ru"
    return email

@pytest.fixture
def password():
    password = "123456"
    return password