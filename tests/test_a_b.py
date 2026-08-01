import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.a_b_page import ABPage

def test_a_b_variations(page: Page, home: HomePage, a_b_page: ABPage):
    home.click_a_b()
    page.wait_for_url("**/abtest")
    expect(a_b_page.header).to_have_text(
        re.compile(r"A/B Test (Control|Variation \d) page for Automation Testing Practice")
    )
    page.goto(f"{page.url}?abtest_off=true")
    expect(a_b_page.header).to_have_text("No A/B Test page for Automation Testing Practice")
