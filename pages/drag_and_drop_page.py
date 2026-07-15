from playwright.sync_api import Page


class DragAndDropPage:
    def __init__(self, page: Page):
        self.page = page
        self.column_a = page.locator("#column-a")
        self.column_b = page.locator("#column-b")


    def drag_a_to_b(self):
        self.column_a.drag_to(self.column_b)