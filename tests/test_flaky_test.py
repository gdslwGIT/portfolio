from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.flaky_test_page import FlakyTestPage

def test_flaky_test_recovery(page: Page, home: HomePage, flaky_test_page: FlakyTestPage):
    home.click_flaky_test()
    page.wait_for_url("**/flaky-test")
    page.wait_for_timeout(500)
    
    expect(flaky_test_page.header).to_have_text("Flaky Test page for Automation Testing")
    expect(flaky_test_page.status).to_be_visible()
    
    is_ready = flaky_test_page.reload_until_ready(max_attempts=5)
    assert is_ready, "Page did not reach 'Ready' status after 5 attempts"
    expect(flaky_test_page.status).to_have_text("Ready")
