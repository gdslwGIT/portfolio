from playwright.sync_api import Page

class CypressSpiesPage:
    def __init__(self, page:Page):
        self.page = page
        self.like_button = page.locator("#likeBtn")
        self.dislike_button = page.locator("#dislikeBtn")
        self.feedback_message = page.get_by_test_id("feedback-text")
        self.my_location_button = page.locator("#myLocation")
        self.country_name = page.locator("#countryName")
        self.lat_value = page.locator("#lat-value")
        self.long_value = page.locator("#long-value")
        self.discover_button = page.locator("#discoverScientificMethod")
        self.steps = page.locator("#steps p")

    def click_like(self):
        self.like_button.click()
    
    def click_find_my_location(self):
        self.my_location_button.click()
        
    def click_browser_method(self):
        self.discover_button.click()


    
