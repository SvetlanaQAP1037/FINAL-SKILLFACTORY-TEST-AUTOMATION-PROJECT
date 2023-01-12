# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_pass_rec_check_menu.py

from pages.pass_recovery_page import PassRecoveryPage

def test_pass_rec_check_menu(web_browser):
    """Check the menu for selecting the type of contact data entry and take screenshots of the data entry fields"""
    page = PassRecoveryPage(web_browser)

    page.email_btn.click()
    # Проверяем, что в поле ввода данных появилась подсказка "Электронная почта"
    assert "Электронная почта" == page.email_hint.get_text()
    # Делаем скриншот поля ввода данных
    page.login.highlight_and_make_screenshot('screenshots\\email_field.png')
    page.login_btn.click()
    # Проверяем, что в поле ввода данных появилась подсказка "Логин"
    assert 'Логин' == page.login_hint.get_text()
    # Делаем скриншот поля ввода данных
    page.login.highlight_and_make_screenshot('screenshots\\login_field.png')
    page.ls_btn.click()
    # Проверяем, что в поле ввода данных появилась подсказка "Лицевой счет"
    assert "Лицевой счёт" == page.ls_hint.get_text()
    # Делаем скриншот поля ввода данных
    page.login.highlight_and_make_screenshot('screenshots\\ls_field.png')
    page.phone_btn.click()
    # Проверяем, что в поле ввода данных появилась подсказка "Мобильный телефон"
    assert "Мобильный телефон" == page.phone_hint.get_text()
    # Делаем скриншот поля ввода данных
    page.login.highlight_and_make_screenshot('screenshots\\phone_field.png')