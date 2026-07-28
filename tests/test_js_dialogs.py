from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.js_dialogs_page import JsDialogsPage

def test_js_dialogs(page: Page, home: HomePage, js_dialogs_page: JsDialogsPage):
    home.click_js_dialogs()
    page.wait_for_url("**/js-dialogs")
    page.wait_for_timeout(1000)
    page.once("dialog", lambda dialog: dialog.accept())
    js_dialogs_page.alert_button.click()
    expect(js_dialogs_page.response).to_have_text("OK")
    page.once("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(1000)
    js_dialogs_page.confirm_button.click()
    expect(js_dialogs_page.response).to_have_text("Ok")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(1000)
    js_dialogs_page.confirm_button.click()
    expect(js_dialogs_page.response).to_have_text("Cancel")
    page.once("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    page.wait_for_timeout(1000)
    js_dialogs_page.prompt_button.click()
    expect(js_dialogs_page.response).to_have_text("Hello Playwright")
