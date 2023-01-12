# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_by_code_check_invalid_data.py

from pages.auth_by_code_page import AuthByCodePage
from faker import Faker

def test_auth_by_code_check_invalid_data(web_browser):
    # """Make sure that the user cannot log in using the incorrect code and take a screenshot of the error message"""
    page = AuthByCodePage(web_browser)

    fake_num = Faker()
    for i in range(0, 11):
        test_num = fake_num.random_digit()
        # Ввод чисел тел без знака "+"
        page.login_field.send_keys(str(test_num))

    page.get_code_btn.click()
    # Делаем скриншот сообщения об ошибке
    page.error_input_mess.highlight_and_make_screenshot('screenshots\\wrong_digital_format.png')
    # Проверяем, что пользователь все еще не странице "Авторизация по коду"
    assert page.auth_bc_title.get_text() == "Авторизация по коду"

    page.refresh()
    # Ввод пробелов
    page.login_field.send_keys("             ")
    page.get_code_btn.click()
    # Делаем скриншот сообщения об ошибке
    page.error_input_mess.highlight_and_make_screenshot('screenshots\\wrong_spaces_format.png')
    # Проверяем, что пользователь все еще не странице "Авторизация по коду"
    assert page.auth_bc_title.get_text() == "Авторизация по коду"

    page.refresh()
    # Ввод спецсимволов
    page.login_field.send_keys("&+#?_<,;)(,%(^<:<>?№")
    page.get_code_btn.click()
    # Делаем скриншот сообщения об ошибке
    page.error_input_mess.highlight_and_make_screenshot('screenshots\\wrong_symb_format.png')
    # Проверяем, что пользователь все еще не странице "Авторизация по коду"
    assert page.auth_bc_title.get_text() == "Авторизация по коду"

    page.refresh()
    # Ввод иероглифов
    page.login_field.send_keys("饭昂稀笑车淋话谢淋不火用饭谢话")
    page.get_code_btn.click()
    # Делаем скриншот сообщения об ошибке
    page.error_input_mess.highlight_and_make_screenshot('screenshots\\wrong_hieroglyph_format.png')
    # Проверяем, что пользователь все еще не странице "Авторизация по коду"
    assert page.auth_bc_title.get_text() == "Авторизация по коду"



