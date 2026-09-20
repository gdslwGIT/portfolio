import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_match_page import ShouldMatchPage

def test_should_match_page(page: Page, home: HomePage, should_match_page: ShouldMatchPage):
    home.click_should_match()
    page.wait_for_url("**/assertions/should-match")

    expect(should_match_page.header).to_be_visible()
    expect(should_match_page.header).to_have_text(re.compile(r"Should Match.*Automation Testing Practice"))

    expect(should_match_page.description).to_be_visible()
    expect(should_match_page.description).to_have_text(re.compile(r"should match.*regular expression"))

    expect(should_match_page.input1_heading).to_be_visible()
    expect(should_match_page.input1_heading).to_have_text(re.compile(r"input1"))
