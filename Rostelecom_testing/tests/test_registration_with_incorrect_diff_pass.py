# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_with_incorrect_diff_pass.py

from pages.reg_page import RegPage
from faker import Faker
from settings import rand_email

def test_registration_with_incorrect_diff_pass(web_browser):
    """Make sure that the user will not be able to register with an incorrect different passwords, and take a screenshot
    that the user stayed on the registration page"""
    fake_name = Faker('ru_RU')
    fake_pass = Faker()
    page = RegPage(web_browser)

    page.register_link.click()

    page.name.send_keys(fake_name.first_name_female())
    page.surname.send_keys(fake_name.last_name_female())
    page.address.send_keys(rand_email)
    page.password.send_keys(fake_pass.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
    page.confirm_password.send_keys(fake_pass.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
    page.register_btn.click()

    # Делаем скриншот сообщения "Пароли не совпадают"
    page.diff_pass_message.highlight_and_make_screenshot('screenshots\\different_pass.png')
    # Проверяем, что пользователь все еще находится на странице с формой "Регистрация"
    assert page.register_title.get_text() == "Регистрация"