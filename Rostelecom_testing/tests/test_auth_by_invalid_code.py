# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_by_invalid_code.py

from pages.auth_by_code_page import AuthByCodePage
from settings import rand_phone

def test_auth_by_invalid_code(web_browser):
    """Make sure that the user cannot log in using the incorrect code and take a screenshot of the error message"""
    page = AuthByCodePage(web_browser)

    page.login_field.send_keys(rand_phone)
    page.get_code_btn.click()
    page.code_input_1.send_keys("1")
    page.code_input_2.send_keys("1")
    page.code_input_3.send_keys("1")
    page.code_input_4.send_keys("1")
    page.code_input_5.send_keys("1")
    page.code_input_6.send_keys("1")

    # Делаем скриншот сообщения "Неверный код. Повторите попытку"
    page.wrong_code_message.highlight_and_make_screenshot('screenshots\\wrong_code.png')
    # Проверяем, что пользователь все еще находится на странице формы "Код подтверждения отправлен"
    assert page.code_tittle.get_text() == "Код подтверждения отправлен"