from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.bmi_page import BmiPage

def test_bmi_underweight(page: Page, home: HomePage, bmi_page: BmiPage):
    home.click_bmi()
    page.wait_for_url("**/bmi")
    page.wait_for_timeout(500)

    bmi_page.calculate_bmi(gender="Female", age="25", height="180", weight="50")
    page.wait_for_timeout(500)

    expect(bmi_page.result_box).to_be_visible()
    expect(bmi_page.bmi_text).to_contain_text("Thinness")

def test_bmi_normal(page: Page, home: HomePage, bmi_page: BmiPage):
    home.click_bmi()
    page.wait_for_url("**/bmi")
    page.wait_for_timeout(500)

    bmi_page.calculate_bmi(gender="Male", age="35", height="190", weight="70")
    page.wait_for_timeout(500)

    expect(bmi_page.result_box).to_be_visible()
    expect(bmi_page.bmi_text).to_contain_text("Normal")

def test_bmi_overweight(page: Page, home: HomePage, bmi_page: BmiPage):
    home.click_bmi()
    page.wait_for_url("**/bmi")
    page.wait_for_timeout(500)

    bmi_page.calculate_bmi(gender="Male", age="30", height="175", weight="80")
    page.wait_for_timeout(500)

    expect(bmi_page.result_box).to_be_visible()
    expect(bmi_page.bmi_text).to_contain_text("Overweight")

def test_bmi_obesity(page: Page, home: HomePage, bmi_page: BmiPage):
    home.click_bmi()
    page.wait_for_url("**/bmi")
    page.wait_for_timeout(500)

    bmi_page.calculate_bmi(gender="Female", age="40", height="160", weight="90")
    page.wait_for_timeout(500)

    expect(bmi_page.result_box).to_be_visible()
    expect(bmi_page.bmi_text).to_contain_text("Obese")

def test_bmi_clear_form(page: Page, home: HomePage, bmi_page: BmiPage):
    home.click_bmi()
    page.wait_for_url("**/bmi")
    page.wait_for_timeout(500)

    bmi_page.calculate_bmi(gender="Female", age="25", height="180", weight="50")
    page.wait_for_timeout(500)

    bmi_page.clear_form()
    page.wait_for_timeout(500)

    expect(bmi_page.result_box).not_to_be_visible()
