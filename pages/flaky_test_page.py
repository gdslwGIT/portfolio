from playwright.sync_api import Page

class FlakyTestPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.header = page.locator("h1")
        self.status = page.locator("#status")
        
    def reload_until_ready(self, max_attempts: int = 5) -> bool:
        for _ in range(max_attempts):
            if self.status.inner_text().strip() == "Ready":
                return True
            self.page.reload()
            self.page.wait_for_timeout(500)
        return self.status.inner_text().strip() == "Ready"
