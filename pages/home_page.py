from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.web_inputs_button = page.locator('a[href="/inputs"].btn')
        self.test_login_page_button = page.locator('a[href="/login"].btn')
        self.test_register_page_button = page.locator('a[href="/register"].btn')
        self.forgot_password_button = page.locator('a[href="/forgot-password"].btn')
        self.otp_login_button = page.locator('a[href="/otp-login"].btn')
        self.dynamic_table_button = page.locator('a[href="/dynamic-table"].btn')
        self.dynamic_pagination_table_button = page.locator('a[href="/dynamic-pagination-table"].btn')
        self.locators_button = page.locator('a[href="/locators"].btn')

    def click_web_inputs(self):
        self.web_inputs_button.click()
    
    def click_login_page(self):
        self.test_login_page_button.click()
        
    def click_register_page(self):
        self.test_register_page_button.click()

    def click_forgot_password(self):
        self.forgot_password_button.click()

    def click_otp_login(self):
        self.otp_login_button.click()

    def click_dynamic_table(self):
        self.dynamic_table_button.click()
    
    def click_dynamic_pagination_table(self):
        self.dynamic_pagination_table_button.click()

    def click_locators(self):
        self.locators_button.click()