from playwright.sync_api import Page


class DragAndDropCirclesPage:
    def __init__(self, page: Page):
        self.page = page
        self.target = page.locator("#target")
        self.red_circle = page.locator(".red")
        self.blue_circle = page.locator(".blue")
        self.green_circle = page.locator(".green")
        self.red_in_target = self.target.locator(".red")
        self.green_in_target = self.target.locator(".green")
        self.blue_in_target = self.target.locator(".blue")

    def drag_circle_to_target(self, color: str):
        self.page.locator(f".{color}").drag_to(self.target)