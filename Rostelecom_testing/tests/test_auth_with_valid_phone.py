# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_with_valid_phone.py

from pages.auth_page import AuthPage
from settings import my_valid_phone, my_phone_pass

def test_auth_with_valid_phone(web_browser):
    """Make sure that the user can authenticate with valid phone number and password
    and take a screenshot that the user is in the personal account"""
    page = AuthPage(web_browser)

    page.phone_btn.click()
    page.login.send_keys(my_valid_phone)
    page.password.send_keys(my_phone_pass)
    page.enter_btn.click()
    # Делаем скриншот страницы с учетными данными
    page.account_data_title.highlight_and_make_screenshot('screenshots\\account_data_page_with_phone.png')
    # Проверяем, что пользователь успешно авторизовался и находится на странице с учетными данными
    assert 'Учетные данные' == page.account_data_title.find().text