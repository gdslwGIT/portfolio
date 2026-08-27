from playwright.sync_api import Page, expect, BrowserContext
from pages.home_page import HomePage
from pages.cookie_alert_page import CookieAlertPage

def test_cookie_alert(page: Page, context: BrowserContext, home: HomePage, cookie_alert_page: CookieAlertPage):
    home.click_cookie_alert()
    page.wait_for_url("**/cookie-alert")
    page.wait_for_timeout(1000)

    expect(cookie_alert_page.cookie_box).not_to_have_class("cookie-box cookie-box-hide")

    cookie_alert_page.accept_btn.click()
    page.wait_for_timeout(1000)

    expect(cookie_alert_page.cookie_box).to_have_class("cookie-box cookie-box-hide")

    cookies = context.cookies()
    cookie_box_cookie = next((c for c in cookies if c["name"] == "cookie-box"), None)
    assert cookie_box_cookie is not None, "Cookie 'cookie-box' was not set"
    assert cookie_box_cookie["value"] == "true", f"Expected cookie value to be 'true', but got '{cookie_box_cookie['value']}'"

    page.reload()
    page.wait_for_timeout(1000)
    expect(cookie_alert_page.cookie_box).to_have_class("cookie-box cookie-box-hide")
