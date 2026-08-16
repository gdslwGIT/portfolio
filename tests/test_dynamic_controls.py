from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dynamic_controls_page import DynamicControlsPage

def test_dynamic_controls_checkbox(page: Page, home: HomePage, dynamic_controls_page: DynamicControlsPage):
    home.click_dynamic_controls()
    page.wait_for_url("**/dynamic-controls")
    page.wait_for_timeout(1000)

    expect(dynamic_controls_page.checkbox).to_be_visible()

    dynamic_controls_page.checkbox_btn.click()
    expect(dynamic_controls_page.loading).to_be_visible()
    expect(dynamic_controls_page.loading).not_to_be_visible()

    expect(dynamic_controls_page.checkbox).not_to_be_visible()
    expect(dynamic_controls_page.message).to_have_text("It's gone!")

    dynamic_controls_page.checkbox_btn.click()
    expect(dynamic_controls_page.loading).to_be_visible()
    expect(dynamic_controls_page.loading).not_to_be_visible()

    expect(dynamic_controls_page.checkbox).to_be_visible()
    expect(dynamic_controls_page.message).to_have_text("It's back!")


def test_dynamic_controls_input(page: Page, home: HomePage, dynamic_controls_page: DynamicControlsPage):
    if not page.url.endswith("/dynamic-controls"):
        home.click_dynamic_controls()
        page.wait_for_url("**/dynamic-controls")
        page.wait_for_timeout(1000)

    expect(dynamic_controls_page.input_field).to_be_disabled()

    dynamic_controls_page.input_btn.click()
    expect(dynamic_controls_page.loading).to_be_visible()
    expect(dynamic_controls_page.loading).not_to_be_visible()

    expect(dynamic_controls_page.input_field).to_be_editable()
    expect(dynamic_controls_page.message).to_have_text("It's enabled!")

    dynamic_controls_page.input_btn.click()
    expect(dynamic_controls_page.loading).to_be_visible()
    expect(dynamic_controls_page.loading).not_to_be_visible()

    expect(dynamic_controls_page.input_field).to_be_disabled()
    expect(dynamic_controls_page.message).to_have_text("It's disabled!")
