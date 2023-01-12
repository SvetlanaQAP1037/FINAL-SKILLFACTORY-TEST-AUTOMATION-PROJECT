# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_auth_by_code_return_standard_auth.py

from pages.auth_by_code_page import AuthByCodePage

def test_auth_by_code_return_standard_auth(web_browser):
    """Make sure that the user can log in with a password from the authorization by code form
    and take a screenshot of the standard authorization form"""
    page = AuthByCodePage(web_browser)

    page.standard_auth_btn.click()
    # Делаем скриншот заголовка "Авторизация"
    page.auth_title.highlight_and_make_screenshot('screenshots\\auth_form.png')
    # Проверяем, что пользователь находится на странице формы "Авторизация"
    assert page.auth_title.get_text() == "Авторизация"

    page.enter_temp_btn.click()
    # Проверяем, что пользователь находится на странице формы "Авторизацияо коду"
    assert page.auth_bc_title.get_text() == "Авторизация по коду"