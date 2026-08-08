from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.horizontal_slider_page import HorizontalSliderPage

def test_horizontal_slider(page: Page, home: HomePage, horizontal_slider_page: HorizontalSliderPage):
    home.click_horizontal_slider()
    page.wait_for_url("**/horizontal-slider")
    page.wait_for_timeout(1000)

    expect(horizontal_slider_page.value_span).to_have_text("0")

    horizontal_slider_page.slider.focus()
    horizontal_slider_page.slider.press("ArrowRight")
    page.wait_for_timeout(500)
    expect(horizontal_slider_page.value_span).to_have_text("0.5")

    horizontal_slider_page.slider.fill("3.5")
    page.wait_for_timeout(500)
    expect(horizontal_slider_page.value_span).to_have_text("3.5")
