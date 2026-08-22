import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contact_page import ContactPage

def test_contact_form(page: Page, home: HomePage, contact_page: ContactPage):
    home.click_contact()
    page.wait_for_url("**/contact")
    page.wait_for_timeout(1000)

    contact_page.name_input.fill("John Doe")
    contact_page.email_input.fill("john.doe@example.com")
    contact_page.message_input.fill("Hello, this is a test message from automation script!")
    page.wait_for_timeout(500)

    contact_page.send_btn.click()
    page.wait_for_timeout(500)

    expect(page).to_have_url(re.compile(r".*/contact#$"))
