# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_registration_user_agreement_link.py

from pages.reg_page import RegPage

def test_registration_user_agreement_link(web_browser):
    """Make sure that the user agreement link works and take
    a screenshot of where the user is on the user agreement page"""
    page = RegPage(web_browser)

    page.register_link.click()
    page.user_agreement.click()
    page.get('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html')

    # Делаем скриншот страницы с "Условиями пользовательского соглашения"
    page.screenshot('screenshots\\user_agreement.png')
    # Проверяем, что пользователь находится на странице с "Условиями пользовательского соглашения"
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'