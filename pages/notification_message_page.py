from playwright.sync_api import Page

class NotificationMessagePage:
    def __init__(self, page: Page):
        self.page = page
        self.trigger_link = page.get_by_role("link", name="Click here")
        self.flash_message = page.locator("#flash")

    def click_trigger_link(self):
        self.trigger_link.click()