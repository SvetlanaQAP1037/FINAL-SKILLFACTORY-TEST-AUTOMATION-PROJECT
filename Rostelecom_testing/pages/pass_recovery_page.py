from pages.base import WebPage
from pages.elements import WebElement


class PassRecoveryPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=" \
              "lk_decosystems&tab_id=VNgg_Dy3yqM"
        super().__init__(web_driver, url)

    # Заголовок 'Восстановление пароля'
    pass_rec_tittle = WebElement(xpath="//h1[contains(text(),'Восстановление пароля')]")
    # Кнопка "Телефон"
    phone_btn = WebElement(id='t-btn-tab-phone')
    # Кнопка "Почта"
    email_btn = WebElement(id='t-btn-tab-mail')
    # Кнопка "Логин"
    login_btn = WebElement(id='t-btn-tab-login')
    # Кнопка "Лицевой счет"
    ls_btn = WebElement(id='t-btn-tab-ls')
    # Поле ввода логина: "Мобильный телефон"/"Электронная почта"/"Логин"/"Лицевой счет"
    login = WebElement(id='username')
    # Подсказка для поля ввода "Телефон"
    phone_hint = WebElement(xpath="//span[contains(text(),'Мобильный телефон')]")
    # Подсказка для поля ввода "Почта"
    email_hint = WebElement(xpath="//span[contains(text(),'Электронная почта')]")
    # Подсказка для поля ввода "Логин"
    login_hint = WebElement(xpath="//span[contains(text(),'Логин')]")
    # Подсказка для поля ввода "Лицевой счет"
    ls_hint = WebElement(xpath="//span[contains(text(),'Лицевой счёт')]")
    # Картинка с символами
    captcha_img = WebElement(xpath="//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']"
                                       "/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/img[1]")
    # Поле ввода "Капча"
    captcha = WebElement(id='captcha')
    # Иконка "Обновить капчу"
    update_captcha_icon = WebElement(xpath="//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']"
                                           "/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/*[1]")
    # Кнопка "Продолжить"
    resume_btn = WebElement(id="reset")
    # Кнопка "Вернуться назад"
    return_btn = WebElement(id="reset-back")
    # Сообщение "Неверный логин или текст с картинки"
    error_mess = WebElement(id="form-error-message")