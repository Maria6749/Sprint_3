from selenium.webdriver.common.by import By
class TestLocators():
    LOGIN_EMAIL=By.XPATH, ".//input[@name='name']"
    LOGIN_BUTTON_ACCOUNT=By.XPATH, ".//button[text()='Войти в аккаунт']"
    LOGIN_PASSWORD=By.XPATH, ".//input[@name='Пароль']"
    LOGIN_BUTTON=By.XPATH, ".//button[text()='Войти']"
    REGISTRATION_LOGIN=By.XPATH, ".//a[text()='Войти']"
    LOGIN_ASSERT_TEXT=By.XPATH,".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    LOGIN_TEXT=By.XPATH, ".//h2[text()='Вход']"
    LOGIN_BURGER_TEXT=By.XPATH, ".//h1[text()='Соберите бургер']"
    LOGIN_PESRONAL_ACCOUNT=By.XPATH, ".//p[text()='Личный Кабинет']"
    REGISTRATION_CSS=By.CSS_SELECTOR, ".Auth_link__1fOlj"
    REGISTRATION_TEXT=By.XPATH, ".//a[text()='Зарегистрироваться']"
    REGISTRATION_USER_NAME=By.XPATH, ".//input[@class='text input__textfield text_type_main-default']"
    REGISTRARION_EMAIL=By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']"
    REGISTRATION_BUTTON=By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    REGISTRATION_TEXT_WAIT=By.XPATH, ".//h2[text()='Регистрация']"
    REGISTRATION_FAIL=By.XPATH, ".//p[@class='input__error text_type_main-default']"
    ORDER=By.XPATH, ".//button[text()='Оформить заказ']"
    PROFILE=By.XPATH, ".//a[text()='Профиль']"
    LOGOUT=By.XPATH, ".//button[text()='Выход']"
    LOGO_BURGER=By.XPATH, ".//a"
    CONSTRUCTOR=By.XPATH, ".//p[text()='Конструктор']"
    SOUS_BUTTON=By.XPATH, ".//span[text()='Соусы']"
    SOUS_TEXT=By.XPATH, ".//h2[text()='Соусы']"
    SOUS_DISPLAYID=By.XPATH, ".//p[text()='Соус Spicy-X']"
    BULKI_BUTTON=By.XPATH, ".//span[text()='Булки']"
    BULKI_TEXT=By.XPATH, ".//h2[text()='Булки']"
    BULKI_DISPLAYID=By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"
    NACINKI_BUTTON=By.XPATH, ".//span[text()='Начинки']"
    NACHINKI_TEXT=By.XPATH, ".//h2[text()='Начинки']"
    NACHINKI_DISPLAYID=By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']"