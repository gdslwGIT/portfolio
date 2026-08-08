from playwright.sync_api import Page

class HorizontalSliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = page.locator(".sliderContainer input[type='range']")
        self.value_span = page.locator("#range")