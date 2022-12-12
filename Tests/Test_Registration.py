from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#Успешная регистрация
def test_registration_valid(driver, user):
    # С главной переходим в раздел регистрации
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTRATION_CSS)))
    driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTRATION_TEXT_WAIT)))
    # Регистрируемся с валидными данными
    driver.find_element(*TestLocators.REGISTRATION_USER_NAME).send_keys("Мария2")
    driver.find_element(*TestLocators.REGISTRARION_EMAIL).send_keys(user)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
    # Проверяем, что страница входа в систему
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

#Неуспешная регистрация
def test_registration_fail(driver, user):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTRATION_CSS)))
    driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.REGISTRATION_TEXT_WAIT)))
   # Регистрируемся с не валидными данными
    driver.find_element(*TestLocators.REGISTRATION_USER_NAME).send_keys("Мария2")
    driver.find_element(*TestLocators.REGISTRARION_EMAIL).send_keys(user)
    driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys('1234')
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
   # Проверяем, что появилась ошибка
    assert driver.find_element(*TestLocators.REGISTRATION_FAIL).text == 'Некорректный пароль'





