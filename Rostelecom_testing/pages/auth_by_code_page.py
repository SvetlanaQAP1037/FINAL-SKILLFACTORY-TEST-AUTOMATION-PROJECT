from pages.base import WebPage
from pages.elements import WebElement


class AuthByCodePage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&' \
              'redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'
        super().__init__(web_driver, url)

    # Заголовок "Авторизация по коду"
    auth_bc_title = WebElement(xpath="// h1[contains(text(), 'Авторизация по коду')]")
    # Поле "E-mail или мобильный телефон"
    login_field = WebElement(id="address")
    # Кнопка "Получить код"
    get_code_btn = WebElement(id="otp_get_code")
    # Кнопка "Войти с паролем"
    standard_auth_btn = WebElement(id="standard_auth_btn")
    # Сообщение "Неверный код. Повторите попытку"
    wrong_code_message = WebElement(id="form-error-message")
    # Сообщение "Введите телефон или email в формате.."
    error_input_mess = WebElement(xpath="//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')]")
    # Заголовок "Код подтверждения отправлен"
    code_tittle = WebElement(xpath="// h1[contains(text(), 'Код подтверждения отправлен')]")
    # Поля ввода кода
    code_input_1 = WebElement(id="rt-code-0")
    code_input_2 = WebElement(id="rt-code-1")
    code_input_3 = WebElement(id="rt-code-2")
    code_input_4 = WebElement(id="rt-code-3")
    code_input_5 = WebElement(id="rt-code-4")
    code_input_6 = WebElement(id="rt-code-5")
    # Заголовок "Авторизация"
    auth_title = WebElement(xpath="//h1[contains(text(),'Авторизация')]")
    # Кнопка "Войти по временному коду"
    enter_temp_btn = WebElement(id="back_to_otp_btn")

    change_phone = WebElement(name="otp_back_phone")