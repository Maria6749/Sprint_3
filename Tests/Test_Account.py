from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#Проверь переход по клику на «Личный кабинет»
def test_account_chrome(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
    driver.find_element(*TestLocators.LOGIN_PESRONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE)))
    url_profile = "https://stellarburgers.nomoreparties.site/account/profile"
    assert driver.current_url == url_profile
