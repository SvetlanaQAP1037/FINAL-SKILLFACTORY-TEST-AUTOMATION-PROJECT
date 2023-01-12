# Run test:
# python -m pytest -v --driver Chrome --driver-path C:/Chromedriver/chromedriver.exe test_pass_rec_update_captcha_img.py

from pages.pass_recovery_page import PassRecoveryPage

def test_pass_rec_update_captcha_img(web_browser):
    """Make sure that after clicking on the update captcha icon, the picture will change"""
    page = PassRecoveryPage(web_browser)

    cap_first = page.captcha_img.get_attribute("src")
    page.update_captcha_icon.click()
    cap_second = page.captcha_img.get_attribute("src")

    # Проверяем, что атрибуты картинок (current source) разные, значит картинки разные
    assert cap_first != cap_second