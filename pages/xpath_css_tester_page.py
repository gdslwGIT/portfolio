from playwright.sync_api import Page

class XpathCssTesterPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1").first
        self.selector_label = page.locator("#selector-label")
        self.selector_input = page.locator("#selector-input")
        self.selector_switch = page.locator("#selector-switch")
        self.selector_error = page.locator("#selector-error")
        self.matches_count = page.locator("#matches-count")
        self.html_preview = page.locator("#html-preview")

    def switch_to_xpath(self):
        if self.selector_switch.is_checked():
            self.selector_switch.set_checked(False, force=True)

    def switch_to_css(self):
        if not self.selector_switch.is_checked():
            self.selector_switch.set_checked(True, force=True)

    def enter_selector(self, selector: str):
        self.selector_input.fill(selector)
