from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Проверь, что работают переходы к разделу соусы
def test_sous_main(driver, email, password):
   driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
   WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
   driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
   driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
   driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
   driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
   assert driver.find_element(By.XPATH, ".//p[text()='Соус Spicy-X']").is_displayed()
   driver.quit()

#Проверь, что работают переходы к разделу булки
def test_bulki_main(driver, email, password):
   driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
   driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
   driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
   driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
   driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
   driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Булки']")))
   assert driver.find_element(By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']").is_displayed()
   driver.quit()

# Проверь, что работают переходы к разделу начинки

def test_nachinka_main(driver, email, password):
   driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
   WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
   driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
   driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
   driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
   WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
   driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
   WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
   assert driver.find_element(By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']").is_displayed()
   driver.quit()

