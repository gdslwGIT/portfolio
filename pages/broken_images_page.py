from playwright.sync_api import Page

class BrokenImagesPage:
    def __init__(self, page: Page):
        self.page = page
        self.images = page.locator(".page-layout img")

    def is_image_broken(self, index: int) -> bool:
        return self.images.nth(index).evaluate("element => element.naturalWidth === 0")
