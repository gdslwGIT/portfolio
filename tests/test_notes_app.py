from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.notes_login_page import NotesLoginPage
from pages.notes_app_page import NotesAppPage

def register_and_login(page: Page, home: HomePage, notes_login_page: NotesLoginPage, mailbox) -> NotesAppPage:
    test_email = mailbox.email
    test_password = "Password123!"

    home.click_notes_login()
    page.wait_for_url("**/notes/app/login")
    page.wait_for_timeout(1000)

    notes_login_page.register_link.click()
    page.wait_for_url("**/notes/app/register")
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

    return NotesAppPage(page)

def test_notes_categories_filter(page: Page, home: HomePage, notes_login_page: NotesLoginPage, mailbox):
    notes_app = register_and_login(page, home, notes_login_page, mailbox)
    
    notes_app.create_note("Home Note Title", "Home Category Description", category="Home")
    page.wait_for_timeout(1000)
    notes_app.create_note("Work Note Title", "Work Category Description", category="Work")
    page.wait_for_timeout(1000)

    notes_app.category_home_btn.click()
    page.wait_for_timeout(500)
    expect(page.locator("text=Home Note Title")).to_be_visible()
    expect(page.locator("text=Work Note Title")).not_to_be_visible()

    notes_app.category_work_btn.click()
    page.wait_for_timeout(500)
    expect(page.locator("text=Work Note Title")).to_be_visible()
    expect(page.locator("text=Home Note Title")).not_to_be_visible()

    notes_app.category_all_btn.click()
    page.wait_for_timeout(500)
    expect(page.locator("text=Home Note Title")).to_be_visible()
    expect(page.locator("text=Work Note Title")).to_be_visible()

def test_notes_search_and_delete(page: Page, home: HomePage, notes_login_page: NotesLoginPage, mailbox):
    notes_app = register_and_login(page, home, notes_login_page, mailbox)

    notes_app.create_note("Unique Searchable Note", "Description to search", category="Personal")
    page.wait_for_timeout(1000)

    notes_app.search_notes("Unique Searchable")
    page.wait_for_timeout(500)
    expect(page.locator("text=Unique Searchable Note")).to_be_visible()

    notes_app.delete_first_note()
    page.wait_for_timeout(1000)
    expect(page.locator("text=Unique Searchable Note")).not_to_be_visible()
