from playwright.sync_api import Page

class TyposPage:
    def __init__(self, page: Page):
        self.page = page
        self.typo_paragraph = page.locator(".page-layout p").nth(1)

    def get_paragraph_text(self) -> str:
        return self.typo_paragraph.inner_text()
