from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.notes_login_page import NotesLoginPage

def test_notes_login_validation(page: Page, home: HomePage, notes_login_page: NotesLoginPage, mailbox):
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
    expect(notes_login_page.header).to_have_text("Login")
    expect(notes_login_page.forgot_password_link).to_have_attribute("href", "/notes/app/forgot-password")
    expect(notes_login_page.google_login_btn).to_have_attribute("href", "https://practice.expandtesting.com/notes/app/auth/google")
    expect(notes_login_page.linkedin_login_btn).to_have_attribute("href", "https://practice.expandtesting.com/notes/app/auth/linkedin")
    expect(notes_login_page.register_link).to_have_attribute("href", "/notes/app/register")
    notes_login_page.email_input.fill(test_email)
    notes_login_page.password_input.fill("wrong_password")
    notes_login_page.submit_btn.click()
    page.wait_for_timeout(1000)
    expect(notes_login_page.alert_message).to_be_visible()
    expect(notes_login_page.alert_message).to_have_text("Incorrect email address or password")

    notes_login_page.email_input.fill(test_email)
    notes_login_page.password_input.fill(test_password)
    notes_login_page.submit_btn.click()
    page.wait_for_timeout(1000)
    page.wait_for_url("**/notes/app")
    logout_btn = page.locator("[data-testid='logout']")
    expect(logout_btn).to_be_visible()
    logout_btn.click()
    page.wait_for_timeout(1000)
    expect(logout_btn).not_to_be_visible()
    expect(page.locator("text=Welcome to Notes App")).to_be_visible()

