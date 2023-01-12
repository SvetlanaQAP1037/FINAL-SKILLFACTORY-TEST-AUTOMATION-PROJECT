# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_with_vk_network.py

from pages.auth_page import AuthPage
from settings import my_valid_phone, my_phone_pass, my_phone_pass_vk

def test_auth_with_vk_network(web_browser):
    """Make sure that the user can authenticate using the social network 'VK',
    and take a screenshot confirming that the user is in the personal account"""
    page = AuthPage(web_browser)

    page.phone_btn.click()
    page.login.send_keys(my_valid_phone)
    page.password.send_keys(my_phone_pass)
    page.enter_btn.click()
    page.add_network_btn.click()
    page.vk_icon.click()
    # Вводим данные "ВКонтакте"
    page.vk_login_input.send_keys(my_valid_phone)
    page.vk_pass_input.send_keys(my_phone_pass_vk)
    page.vk_enter.click()

    page.exit_btn.click()
    # Авторизуемся с помощью "ВКонтакте"
    page.vk_network.click()
    # Делаем скриншот, что пользователь вошел в "Учетные данные", используя соцсеть "ВКонтакте"
    page.screenshot('screenshots\\auth_with_vk.png')
    # Проверяем, что пользователь авторизовался и находится на странице "Учетные данные"
    assert 'Учетные данные' == page.account_data_title.get_text()