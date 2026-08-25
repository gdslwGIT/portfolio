import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.feedback_page import FeedbackPage

def test_feedback_form(page: Page, home: HomePage, feedback_page: FeedbackPage):
    home.click_feedback()
    page.wait_for_url("**/feedback")
    page.wait_for_timeout(1000)
    page.evaluate("() => document.querySelectorAll('.row.collapse').forEach(el => el.style.display = 'block')")
    page.wait_for_timeout(500)

    feedback_page.contact_header.click()
    page.wait_for_timeout(500)

    feedback_page.name_input.fill("John Doe")
    feedback_page.email_input.fill("john.doe@example.com")
    feedback_page.message_input.fill("This is my automated feedback text.")
    page.wait_for_timeout(500)

    feedback_page.submit_btn.click()
    page.wait_for_timeout(1000)

    expect(page).to_have_url(re.compile(r".*/feedback\?#panel1$"))
