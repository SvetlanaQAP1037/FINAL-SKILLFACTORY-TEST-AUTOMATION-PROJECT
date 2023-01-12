# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_pass_rec_invalid_code.py

from pages.pass_recovery_page import PassRecoveryPage
from settings import my_valid_email

def test_pass_rec_invalid_code(web_browser):
    """Make sure that after incorrectly entering symbols in the captcha field, the system will not send
    a password recovery code and take a screenshot of the user stayed on the page"""
    page = PassRecoveryPage(web_browser)

    page.email_btn.click()
    page.login.send_keys(my_valid_email)
    page.captcha.send_keys("fakesymb")
    page.resume_btn.click()

    # Делаем скриншот сообщения об ошибке ввода данных
    page.error_mess.highlight_and_make_screenshot('screenshots\\wrong_symbols.png')
    # Проверяем, что в пользователь остался на странице формы "Восстановление пароля"
    assert page.pass_rec_tittle.get_text() == 'Восстановление пароля'