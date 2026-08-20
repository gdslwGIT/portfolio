from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.entry_ad_page import EntryAdPage

def test_entry_ad_modal(page: Page, home: HomePage, entry_ad_page: EntryAdPage):
    home.click_entry_ad()
    page.wait_for_url("**/entry-ad")
    page.wait_for_timeout(1000)
    expect(entry_ad_page.modal).to_have_class("modal fade show")
    entry_ad_page.close_btn.click()
    page.wait_for_timeout(1000)
    expect(entry_ad_page.modal).not_to_have_class("modal fade show")

    page.reload()
    page.wait_for_timeout(1000)
    expect(entry_ad_page.modal).not_to_have_class("modal fade show")
    entry_ad_page.restart_link.click()
    page.wait_for_timeout(500)
    page.reload()
    page.wait_for_timeout(1000)

    expect(entry_ad_page.modal).to_have_class("modal fade show")
