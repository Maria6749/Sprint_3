from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#Проверь переход по клику на «Конструктор»
def test_constructor_chrome(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
    driver.find_element(*TestLocators.LOGIN_PESRONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE)))
    driver.find_element(*TestLocators.CONSTRUCTOR).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
    home_url = "https://stellarburgers.nomoreparties.site/"
    assert driver.current_url == home_url

#Проверь переход на логотип Stellar Burgers
def test_Stellar_Burgers_chrome(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
    driver.find_element(*TestLocators.LOGIN_PESRONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE)))
    driver.find_element(*TestLocators.LOGO_BURGER).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
    home_url = "https://stellarburgers.nomoreparties.site/"
    assert driver.current_url == home_url


