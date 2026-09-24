from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.mochawesome_reports_page import MochawesomeReportsPage

def test_mochawesome_reports_page(page: Page, home: HomePage, mochawesome_reports_page: MochawesomeReportsPage):
    home.click_mochawesome_reports()
    page.wait_for_url("**/mochawesome-reports")

    expect(mochawesome_reports_page.header).to_be_visible()
    expect(mochawesome_reports_page.header).to_contain_text("Mochawesome Reports")
    expect(mochawesome_reports_page.header).to_contain_text("Automation Testing Practice")

    expect(mochawesome_reports_page.report_heading).to_be_visible()
    expect(mochawesome_reports_page.report_heading).to_contain_text("Report #1")
