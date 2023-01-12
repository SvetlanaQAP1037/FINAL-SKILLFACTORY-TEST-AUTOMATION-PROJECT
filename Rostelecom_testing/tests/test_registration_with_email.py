# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_with_email.py

from pages.reg_page import RegPage
from faker import Faker
from settings import rand_email, rand_email_pass

def test_registration_with_email(web_browser):
    """Make sure that the user can register with valid data at the email address and password and take a screenshot
    that a code has been sent to the user to finish registration"""
    fake = Faker('ru_RU')
    page = RegPage(web_browser)

    page.register_link.click()
    page.name.send_keys(fake.first_name_female())
    page.surname.send_keys(fake.last_name_female())

    page.address.send_keys(rand_email)
    page.password.send_keys(rand_email_pass)
    page.confirm_password.send_keys(rand_email_pass)
    page.register_btn.click()

    # Делаем скриншот страницы с формой "Подтверждение email"
    page.screenshot('screenshots\\email_conf_form.png')
    # Проверяем, что пользователь находится на странице с формой "Подтверждение email"
    assert page.email_conf_title.find().text == 'Подтверждение email'