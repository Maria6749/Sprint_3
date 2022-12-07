from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Проверь переход по клику на «Конструктор»
def test_constructor_chrome(driver, email, password):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
    home_url = "https://stellarburgers.nomoreparties.site/"
    assert driver.current_url == home_url
    driver.quit()

#Проверь переход на логотип Stellar Burgers
def test_Stellar_Burgers_chrome(driver, email, password):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))
    driver.find_element(By.XPATH, ".//a").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
    home_url = "https://stellarburgers.nomoreparties.site/"
    assert driver.current_url == home_url
    driver.quit()

