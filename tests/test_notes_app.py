from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.notes_login_page import NotesLoginPage
from pages.notes_app_page import NotesAppPage

def test_notes_app_flow(page: Page, home: HomePage, notes_login_page: NotesLoginPage, mailbox):
    test_email = mailbox.email
    test_password = "Password123!"


    page.goto("https://practice.expandtesting.com/notes/app/register")
    page.wait_for_timeout(1000)
    page.locator("[data-testid='register-name']").fill("Playwright Tester")
    page.locator("[data-testid='register-email']").fill(test_email)
    page.locator("[data-testid='register-password']").fill(test_password)
    page.locator("[data-testid='register-confirm-password']").fill(test_password)
    page.locator("[data-testid='register-submit']").click()
    page.wait_for_timeout(1000)

    page.goto("https://practice.expandtesting.com/notes/app/login")
    page.wait_for_timeout(1000)
    notes_login_page.email_input.fill(test_email)
    notes_login_page.password_input.fill(test_password)
    notes_login_page.submit_btn.click()
    page.wait_for_timeout(1000)

    page.wait_for_url("**/notes/app")
    notes_app_page = NotesAppPage(page)
    expect(notes_app_page.logout_btn).to_be_visible()
    expect(notes_app_page.add_note_btn).to_be_visible()
    note_title = "My Test Note"
    note_desc = "This is a description for automated test note."
    notes_app_page.create_note(title=note_title, description=note_desc, category="Home")
    page.wait_for_timeout(1000)
    expect(page.locator(f"text={note_title}")).to_be_visible()
