from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    # Заголовок "Авторизация"
    auth_title = WebElement(xpath="//h1[contains(text(),'Авторизация')]")
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
    # Поле ввода пароля
    password = WebElement(id='password')
    # Кнопка "Войти"
    enter_btn = WebElement(id='kc-login')
    # Ссылка "Забыл пароль"
    forgot_pass = WebElement(id="forgot_password")
    # Чек-бокс "Запомнить меня"
    remember_me = WebElement(classname="rt-checkbox__label")
    # Сообщение "Неверный логин или пароль"
    error_log_or_pass = WebElement(id="form-error-message")

    # Заголовок "Восстановление пароля"
    recovery_pass = WebElement(xpath="//h1[contains(text(),'Восстановление пароля')]")

    # Соцсеть "ВКонтакте"
    vk_network = WebElement(id='oidc_vk')
    # Поле ввода логина (телефон или email) "ВКонтакте"
    # Кнопка "Привязать соцсеть"
    add_network_btn = WebElement(id='socials_action')
    # Иконка "ВКонтакте"
    vk_icon = WebElement(xpath="//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]")
    # Поле ввода логина "ВКонтакте"
    vk_login_input = WebElement(name='email')
    # Поле ввода пароля "ВКонтакте"
    vk_pass_input = WebElement(name='pass')
    # Кнопка "Войти" в "VK"
    vk_enter = WebElement(id='install_allow')
    # Кнопка "Разрешить"
    allow_btn = WebElement(xpath="//button[contains(text(),'Разрешить')]")
    # Кнопка "Выход"
    exit_btn = WebElement(id='logout-btn')

    return_btn = WebElement(classname='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded')

    account_data_title = WebElement(xpath="//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/h3[1]")