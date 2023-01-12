# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_with_valid_email.py

from pages.auth_page import AuthPage
from settings import my_valid_email, my_email_pass

def test_auth_with_valid_email(web_browser):
    """Make sure that the user can authenticate with valid data at the email address and password
    and take a screenshot that the user is in the personal account"""
    page = AuthPage(web_browser)

    page.email_btn.click()
    page.login.send_keys(my_valid_email)
    page.password.send_keys(my_email_pass)
    page.enter_btn.click()
    # Делаем скриншот страницы с учетными данными
    page.account_data_title.highlight_and_make_screenshot('screenshots\\account_data_page.png')
    # Проверяем, что пользователь успешно авторизовался и находится на странице с учетными данными
    assert 'Учетные данные' == page.account_data_title.get_text()