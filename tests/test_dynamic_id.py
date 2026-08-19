from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dynamic_id_page import DynamicIdPage

def test_dynamic_id_button_click(page: Page, home: HomePage, dynamic_id_page: DynamicIdPage):
    home.click_dynamic_id()
    page.wait_for_url("**/dynamic-id")
    page.wait_for_timeout(1000)

    id_before = dynamic_id_page.dynamic_btn.get_attribute("id")
    assert id_before is not None, "Button ID should exist"

    dynamic_id_page.dynamic_btn.click()
    page.wait_for_timeout(500)

    page.reload()
    page.wait_for_timeout(1000)

    id_after = dynamic_id_page.dynamic_btn.get_attribute("id")
    assert id_after is not None, "Button ID should exist after reload"

    assert id_before != id_after, f"Expected ID to change, but it remained: {id_before}"

    dynamic_id_page.dynamic_btn.click()
    page.wait_for_timeout(500)
