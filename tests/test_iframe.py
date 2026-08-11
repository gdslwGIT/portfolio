from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.iframe_page import IFramePage

def test_iframe_subscription(page: Page, home: HomePage, iframe_page: IFramePage, mailbox):
    home.click_iframe()
    page.wait_for_url("**/iframe")
    page.wait_for_timeout(1000)

    iframe_page.email_input.fill(mailbox.email)
    page.wait_for_timeout(500)

    iframe_page.subscribe_button.click()
    page.wait_for_timeout(500)

    expect(iframe_page.success_message).to_have_text("You are now subscribed!")
