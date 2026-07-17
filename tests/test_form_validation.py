from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.form_validation_page import FormValidationPage


def test_form_validation(page: Page, home: HomePage, form_validation_page: FormValidationPage):
    home.click_form_validation()
    page.wait_for_url("**/form-validation")
    form_validation_page.fill_form("Ahmed", "123-4567890", "2026-03-12", "card")
    form_validation_page.click_submit()
    page.wait_for_timeout(1000)
    page.wait_for_url("**/form-confirmation")
    expect(form_validation_page.success_message).to_be_visible()
    expect(form_validation_page.success_message).to_contain_text("Thank you for validating your ticket")
    page.wait_for_timeout(1000)
    