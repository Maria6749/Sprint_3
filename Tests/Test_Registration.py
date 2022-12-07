from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Успешная регистрация
def test_registration_valid(driver, user):
    # С главной переходим в раздел регистрации
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_link__1fOlj")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))
    # Регистрируемся с валидными данными
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default']").send_keys("Мария2")
    driver.find_element(By.XPATH,".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(user)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(By.XPATH,".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
    # Проверяем, что страница входа в систему
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

#Неуспешная регистрация
def test_registration_fail(driver, user):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_link__1fOlj")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))
    # Регистрируемся с не валидными данными
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default']").send_keys("Мария2")
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(user)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('1234')
    driver.find_element(By.XPATH,".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    # Проверяем, что появилась ошибка
    assert driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
    driver.quit()





