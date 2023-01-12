# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_with_invalid_latin_name.py

from pages.reg_page import RegPage
from faker import Faker
from settings import rand_email, rand_email_pass

def test_registration_with_invalid_latin_name(web_browser):
    """Make sure that the user can't register with invalid latin name and take a screenshot invalid input"""
    fake = Faker()
    page = RegPage(web_browser)

    page.register_link.click()

    registration_url = page.get_current_url()
    # Вводим некорректные данные (имя и фамилия латиницей) - негативный тест-кейс
    try:
        page.name.send_keys(fake.first_name_male())
        page.surname.send_keys(fake.last_name_male())
    except AttributeError:
        pass

    else:
        print('Баг: Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

    finally:
        page.address.send_keys(rand_email)
        page.password.send_keys(rand_email_pass)
        page.confirm_password.send_keys(rand_email_pass)
        page.register_btn.click()
        # Делаем скриншот некорректно заполненного поля
        page.name.highlight_and_make_screenshot('screenshots\\name_invalid_input.png')
        # Проверяем, что пользователь остался на странице регистрации
        assert page.get_current_url() == registration_url