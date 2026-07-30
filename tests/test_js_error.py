from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.js_error_page import JsErrorPage


def test_js_error(page: Page, home: HomePage, js_error_page: JsErrorPage):
    errors = []
    page.on("pageerror", lambda err: errors.append(err))
    home.click_js_error()
    page.wait_for_url("**/javascript-error")
    page.wait_for_timeout(1000)
    assert len(errors) > 0, "No JS errors caught"
    assert any("Cannot read properties of undefined" in str(err) for err in errors), f"Expected error not found. Caught: {errors}"
