from playwright.sync_api import Page

class LocatorsPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_item_button = page.get_by_role("button", name="Add Item")
        self.contact_button = page.get_by_role("link", name="Contact")
        self.hot_deal_alert = page.get_by_text("🔥 Hot Deal: Buy 1 Get 1 Free")
        self.country_selector = page.get_by_label("Choose a country")
        self.email_field = page.get_by_label("Email for newsletter")
        self.search_input = page.get_by_placeholder("Search the site")
        self.filter_tag_input = page.get_by_placeholder("Filter by tag")
        self.user_avatar = page.get_by_alt_text("User avatar")
        self.reload_button = page.get_by_title("Refresh content")
        self.settings_badge = page.get_by_title("Settings panel")
        self.status_message = page.get_by_test_id("status-message")
        self.username_text = page.get_by_test_id("user-name")
        self.task_one = page.locator("//li[contains(text(),'Task 1: Review')]")
        self.headphones_stock = page.locator("//tr[td[text()='Headphones']]/td[3]")


    def select_country(self, county_name: str):
        self.country_selector.select_option(label=county_name)
    
    def fill_email(self, email: str):
        self.email_field.fill(email)
        
    def click_contact(self):
        self.contact_button.click()

    def click_add_item(self):
        self.add_item_button.click()
    
    def fill_search_and_tag(self, search_text: str, tag_text: str):
        self.search_input.fill(search_text)
        self.filter_tag_input.fill(tag_text)

    def click_reload(self):
        self.reload_button.click()
        

        