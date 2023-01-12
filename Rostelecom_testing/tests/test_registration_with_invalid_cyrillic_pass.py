# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_with_invalid_cyrillic_pass.py

from pages.reg_page import RegPage
from faker import Faker
from settings import rand_email

def test_registration_with_invalid_cyrillic_pass(web_browser):
    """Make sure that the user will not be able to register with incorrect cyrillic password, and take a screenshot
    that the user stayed on the registration page"""
    fake_name = Faker('ru_RU')
    fake_pass = Faker()
    page = RegPage(web_browser)

    page.register_link.click()

    registration_url = page.get_current_url()
    page.name.send_keys(fake_name.first_name_male())
    page.surname.send_keys(fake_name.last_name_male())

    page.address.send_keys(rand_email)
    page.eye_icon.click()
    page.password.send_keys(fake_pass.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True) + 'Абв')

    page.confirm_password.click()

    # Делаем скриншот некорректно заполненного поля
    page.latin_message.highlight_and_make_screenshot('screenshots\\cyrillic_pass.png')
    # Проверяем, что пользователь все еще находится на странице с формой "Регистрация"
    assert registration_url == page.get_current_url()
