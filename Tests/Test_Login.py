from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#вход через кнопку «Личный кабинет»
def test_login_from_account(driver, email, password):
  driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
  driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
  driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
  driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
  assert By.XPATH, driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == "Оформить заказ"
  driver.quit()

#вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main(driver, email, password):
  driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
  driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
  driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
  driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
  WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
  assert driver.find_element(By.XPATH,".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == "Оформить заказ"
  driver.quit()


#вход через кнопку в форме регистрации
def test_login_from_registration(driver_register, email, password):
   driver_register.find_element(By.XPATH, ".//a[text()='Войти']").click()
   WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
   driver_register.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
   driver_register.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
   driver_register.find_element(By.XPATH, ".//button[text()='Войти']").click()
   WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
   assert driver_register.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == "Оформить заказ"
   driver_register.quit()


#вход через восстановление пароля
def test_login_chrome_password(driver_reset, email, password):
  driver_reset.find_element(By.XPATH, ".//a[text()='Войти']").click()
  WebDriverWait(driver_reset, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
  driver_reset.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
  driver_reset.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
  driver_reset.find_element(By.XPATH, ".//button[text()='Войти']").click()
  WebDriverWait(driver_reset, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
  assert driver_reset.find_element(By.XPATH,".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == "Оформить заказ"
  driver_reset.quit()
