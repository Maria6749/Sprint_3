from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Проверь выход по кнопке «Выйти» в личном кабинете.

def test_logout_chrome_(driver, email, password):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    url_login = "https://stellarburgers.nomoreparties.site/login"
    assert driver.current_url == url_login
