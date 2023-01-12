# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_with_phone.py

from pages.reg_page import RegPage
from faker import Faker
from settings import rand_phone_pass

def test_registration_with_phone(web_browser):
    """Make sure that the user can register with valid data at the email address and password and take a screenshot
    that a code has been sent to the user to finish registration"""
    fake = Faker('ru_RU')
    page = RegPage(web_browser)

    page.register_link.click()
    page.name.send_keys(fake.first_name_male())
    page.surname.send_keys(fake.last_name_male())

    page.address.send_keys("+79267546695")
    page.password.send_keys(rand_phone_pass)
    page.confirm_password.send_keys(rand_phone_pass)
    page.register_btn.click()

    # Делаем скриншот страницы с формой "Подтверждение телефона"
    page.phone_conf_title.highlight_and_make_screenshot('screenshots\\phone_conf_form.png')
    # Проверяем, что пользователь находится на странице с формой "Подтверждение телефона"
    assert page.phone_conf_title.find().text == 'Подтверждение телефона'