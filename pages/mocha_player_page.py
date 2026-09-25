from playwright.sync_api import Page, Locator

class MochaPlayerPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1").first
        self.run_button = page.locator("button:has-text('Run')").first
        self.clear_button = page.locator("button:has-text('Clear')").first
        self.report = page.locator("#mocha, #mocha-stats, [id*='report'], [id*='console']").first

    def click_template(self, name: str):
        self.page.locator(f"button:has-text('{name}'), a:has-text('{name}'), :text-is('{name}')").first.click()

    def click_run(self):
        if self.run_button.count() > 0 and self.run_button.is_visible():
            self.run_button.click()

    def click_clear(self):
        if self.clear_button.count() > 0 and self.clear_button.is_visible():
            self.clear_button.click()
