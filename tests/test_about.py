from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.about_page import AboutPage

def test_about_page(page: Page, home: HomePage, about_page: AboutPage):
    home.click_about()
    page.wait_for_url("**/about")
    page.wait_for_timeout(500)
    
    expect(about_page.header).to_have_text("About This Website for Automation Testing Practice")
    
    expect(about_page.welcome_heading).to_be_visible()
    
    expect(about_page.contact_email_link).to_be_visible()
    expect(about_page.contact_email_link).to_have_attribute("href", "mailto:expand.testing@gmail.com")
