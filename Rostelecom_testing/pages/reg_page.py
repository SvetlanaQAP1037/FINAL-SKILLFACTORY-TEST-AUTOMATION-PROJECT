from pages.base import WebPage
from pages.elements import WebElement


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    # Ссылка "Зарегистрироваться"
    register_link = WebElement(id='kc-register')
    # Заголовок "Регистрация"
    register_title = WebElement(xpath="//h1[contains(text(),'Регистрация')]")
    # Поле "Имя"
    name = WebElement(name='firstName')
    # Поле "Фамилия"
    surname = WebElement(name='lastName')
    # Поле "Регион"
    district = WebElement(xpath='//span[@class="rt-input__placeholder rt-input__placeholder--top"]')
    # Поле "Email или мобильный телефон"
    address = WebElement(xpath="//input[@id='address']")
    # Поле "Пароль"
    password = WebElement(id='password')
    # Поле "Подтверждение пароля"
    confirm_password = WebElement(xpath="//input[@id='password-confirm']")
    # Кнопка "Зарегистрироваться"
    register_btn = WebElement(name="register")
    # Заголовок "Подтверждение email"
    email_conf_title = WebElement(xpath='//h1[contains(text(), "Подтверждение email")]')
    # Заголовок "Подтверждение телефона"
    phone_conf_title = WebElement(xpath="// h1[contains(text(), 'Подтверждение телефона')]")
    # Ссылка на страницу с "Условиями пользовательского соглашения"
    user_agreement = WebElement(link_text="пользовательского соглашения")
    # Сообщение "Пароль должен содержать хотя бы одну заглавную букву"
    uppercase_message = WebElement(
        xpath="//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную букву')]")
    # Иконка "Глаз"
    eye_icon = WebElement(xpath="//body/div[@id='app']/main[@id='app-container']"
                                "/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/*[1]")
    # Сообщение "Пароль должен содержать только латинские буквы"
    latin_message = WebElement(
        xpath="//span[contains(text(),'Пароль должен содержать только латинские буквы')]")
    # Сообщение "Длина пароля должна быть не более 20 символов"
    length_pass_message = WebElement(xpath="//span[contains(text(),'Длина пароля должна быть не более 20 символов')]")
    # Сообщение "Пароли не совпадают"
    diff_pass_message = WebElement(xpath="//span[contains(text(),'Пароли не совпадают')]")

    error_message = WebElement(classname='rt-input-container__meta rt-input-container__meta--error')