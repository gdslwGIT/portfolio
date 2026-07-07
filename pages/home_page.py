from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.web_inputs_button = page.locator('a[href="/inputs"].btn')
        self.test_login_page_button = page.locator('a[href="/login"].btn')
        self.test_register_page_button = page.locator('a[href="/register"].btn')

    def click_web_inputs(self):
        self.web_inputs_button.click()
    
    def click_login_page(self):
        self.test_login_page_button.click()
        
    def click_register_page(self):
        self.test_register_page_button.click()