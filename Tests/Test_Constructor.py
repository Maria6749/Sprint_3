from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

#Проверь, что работают переходы к разделу соусы
def test_sous_main(driver, email, password):
   driver.get('https://stellarburgers.nomoreparties.site/')
   driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
   WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
   driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
   driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
   driver.find_element(*TestLocators.SOUS_BUTTON).click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.SOUS_TEXT)))
   assert driver.find_element(*TestLocators.SOUS_DISPLAYID).is_displayed()

#Проверь, что работают переходы к разделу булки
def test_bulki_main(driver, email, password):
   driver.get('https://stellarburgers.nomoreparties.site/')
   driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
   driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
   driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
   driver.find_element(*TestLocators.SOUS_BUTTON).click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.SOUS_TEXT)))
   driver.find_element(*TestLocators.BULKI_BUTTON).click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.BULKI_TEXT)))
   assert driver.find_element(*TestLocators.BULKI_DISPLAYID).is_displayed()

# Проверь, что работают переходы к разделу начинки

def test_nachinka_main(driver, email, password):
   driver.get('https://stellarburgers.nomoreparties.site/')
   driver.find_element(*TestLocators.LOGIN_BUTTON_ACCOUNT).click()
   WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TEXT)))
   driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(email)
   driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(password)
   driver.find_element(*TestLocators.LOGIN_BUTTON).click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER)))
   driver.find_element(*TestLocators.NACINKI_BUTTON).click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.NACHINKI_TEXT)))
   assert driver.find_element(*TestLocators.NACHINKI_DISPLAYID).is_displayed()


