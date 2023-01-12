# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_with_invalid_email.py

from pages.auth_page import AuthPage
from settings import my_email_pass
from faker import Faker

def test_auth_with_invalid_email(web_browser):
    """Make sure that the user can't authenticate with invalid data at the email address and password
    and take a screenshot of error message"""
    fake = Faker()
    page = AuthPage(web_browser)

    page.email_btn.click()
    page.login.send_keys(fake.ascii_email())
    page.password.send_keys(my_email_pass)
    page.enter_btn.click()

    # Делаем скриншот сообщения об ошибке ввода данных
    page.error_log_or_pass.highlight_and_make_screenshot('screenshots\\error_email.png')
    # Проверяем, что пользователь все еще находится на странице "Авторизация"
    assert page.auth_title.get_text() == "Авторизация"