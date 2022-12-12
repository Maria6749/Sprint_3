from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#Проверь выход по кнопке «Выйти» в личном кабинете.

def test_logout_chrome_(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
    driver.find_element(*TestLocators.LOGIN_PESRONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE)))
    driver.find_element(*TestLocators.LOGOUT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    url_login = "https://stellarburgers.nomoreparties.site/login"
    assert driver.current_url == url_login
