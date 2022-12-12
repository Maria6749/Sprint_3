from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main(driver, email, password):
  driver.get('https://stellarburgers.nomoreparties.site/')
  driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
  driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
  driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
  driver.find_element(*TestLocators.LOGIN_BUTTON).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
  assert driver.find_element(*TestLocators.LOGIN_ASSERT_TEXT).text == "Оформить заказ"

#вход через кнопку «Личный кабинет»
def test_login_from_account(driver, email, password):
  driver.get('https://stellarburgers.nomoreparties.site/')
  driver.find_element(*TestLocators.LOGIN_PESRONAL_ACCOUNT).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
  driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
  driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
  driver.find_element(*TestLocators.LOGIN_BUTTON).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
  assert driver.find_element(*TestLocators.LOGIN_ASSERT_TEXT).text == "Оформить заказ"

#вход через кнопку в форме регистрации
def test_login_from_registration(driver, email, password):
  driver.get('https://stellarburgers.nomoreparties.site/register')
  driver.find_element(*TestLocators.REGISTRATION_LOGIN).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
  driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
  driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
  driver.find_element(*TestLocators.LOGIN_BUTTON).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
  assert driver.find_element(*TestLocators.LOGIN_ASSERT_TEXT).text == "Оформить заказ"

#вход через восстановление пароля
def test_login_chrome_password(driver, email, password):
  driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
  driver.find_element(*TestLocators.REGISTRATION_LOGIN).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
  driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
  driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
  driver.find_element(*TestLocators.LOGIN_BUTTON).click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_BURGER_TEXT)))
  assert driver.find_element(*TestLocators.LOGIN_ASSERT_TEXT).text == "Оформить заказ"



