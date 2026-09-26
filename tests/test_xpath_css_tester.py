from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.xpath_css_tester_page import XpathCssTesterPage

def test_xpath_css_tester_css_mode(page: Page, home: HomePage, xpath_css_tester_page: XpathCssTesterPage):
    home.click_xpath_css_tester()
    page.wait_for_url("**/xpath-css-tester")

    expect(xpath_css_tester_page.header).to_be_visible()
    xpath_css_tester_page.switch_to_css()
    expect(xpath_css_tester_page.selector_label).to_contain_text("Css Selector:")

    xpath_css_tester_page.enter_selector("#chrome-cpu")
    expect(xpath_css_tester_page.matches_count).to_have_text("1 match")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-valid")
    expect(xpath_css_tester_page.html_preview.locator("#chrome-cpu")).to_have_class("bg-info p-1 highlight")

    xpath_css_tester_page.enter_selector("table tbody tr")
    expect(xpath_css_tester_page.matches_count).to_have_text("2 matches")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-valid")

    xpath_css_tester_page.enter_selector(".not-found-element")
    expect(xpath_css_tester_page.matches_count).to_have_text("No matches")

    xpath_css_tester_page.enter_selector("div[")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-invalid")
    expect(xpath_css_tester_page.selector_error).to_be_visible()
    expect(xpath_css_tester_page.selector_error).to_have_text("The entered selector is not a valid CSS selector.")

def test_xpath_css_tester_xpath_mode(page: Page, home: HomePage, xpath_css_tester_page: XpathCssTesterPage):
    home.click_xpath_css_tester()
    page.wait_for_url("**/xpath-css-tester")

    xpath_css_tester_page.switch_to_xpath()
    expect(xpath_css_tester_page.selector_label).to_contain_text("Xpath Selector:")

    xpath_css_tester_page.enter_selector("//p[@id='chrome-cpu']")
    expect(xpath_css_tester_page.matches_count).to_have_text("1 match")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-valid")
    expect(xpath_css_tester_page.html_preview.locator("#chrome-cpu")).to_have_class("bg-info p-1 highlight")

    xpath_css_tester_page.enter_selector("//tbody/tr")
    expect(xpath_css_tester_page.matches_count).to_have_text("2 matches")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-valid")

    xpath_css_tester_page.enter_selector("//div[@id='not-found']")
    expect(xpath_css_tester_page.matches_count).to_have_text("No matches")

    xpath_css_tester_page.enter_selector("//[")
    expect(xpath_css_tester_page.selector_input).to_have_class("form-control is-invalid")
    expect(xpath_css_tester_page.selector_error).to_be_visible()
    expect(xpath_css_tester_page.selector_error).to_have_text("The entered selector is not a valid XPath selector.")
