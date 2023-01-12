# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_forgot_pass.py

from pages.auth_page import AuthPage
from faker import Faker
from settings import my_valid_phone

def test_auth_forgot_pass(web_browser):
    """Make sure that the forgot password link change the color, it works and take a screenshot
    of the password recovery form"""
    fake = Faker()
    page = AuthPage(web_browser)

    page.login_btn.click()

    page.login.send_keys(my_valid_phone)
    page.password.send_keys(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
    page.enter_btn.click()

    color = page.forgot_pass.find().value_of_css_property('color')

    # Делаем скриншот ссылки "Забыл пароль"
    page.forgot_pass.highlight_and_make_screenshot('screenshots\\orange_color_link.png')
    # Проверяем, что цвет ссылки поменялся на оранжевый
    assert color == "rgba(255, 79, 18, 1)", "Wrong color"

    page.forgot_pass.click()

    # Проверяем, что пользователь находится на странице "Восстановление пароля"
    assert page.recovery_pass.get_text() == "Восстановление пароля"