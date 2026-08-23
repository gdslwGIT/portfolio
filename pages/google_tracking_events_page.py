from playwright.sync_api import Page

class GoogleTrackingEventsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.flash_message = page.locator("#flash")
        
        self.click_btn = page.locator("#click-event-btn")
        self.click_link = page.locator("#click-event-link")
        
        self.email_input = page.locator("#exampleFormControlInput1")
        self.message_input = page.locator("#exampleFormControlTextarea1")
        self.submit_btn = page.locator("#submit-event-form button[type='submit']")
        
        self.conversion_btn = page.locator("#conversion-event-btn")
        
        self.scrollable_div = page.locator("#scrollable-div")
