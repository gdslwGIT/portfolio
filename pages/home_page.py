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
        self.my_browser_button = page.locator('a[href="/my-browser"].btn')
        self.radio_buttons_button = page.locator('a[href="/radio-buttons"].btn')
        self.drag_and_drop_button = page.locator('a[href="/drag-and-drop"].btn')
        self.drag_and_drop_circles_button = page.locator('a[href="/drag-and-drop-circles"].btn')
        self.form_validation_button = page.locator('a[href="/form-validation"].btn')
        self.file_uploader_button = page.locator('a[href="/upload"].btn')
        self.add_remove_button = page.locator('a[href="/add-remove-elements"].btn')
        self.download_secure_button = page.locator('a[href="/download-secure"].btn')
        


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

    def click_my_browser(self):
        self.my_browser_button.click()
    
    def click_radio_buttons(self):
        self.radio_buttons_button.click()

    def click_drag_and_drop(self):
        self.drag_and_drop_button.click()
    
    def click_drag_and_drop_circles(self):
        self.drag_and_drop_circles_button.click()
    
    def click_form_validation(self):
        self.form_validation_button.click()

    def click_file_uploader(self):
        self.file_uploader_button.click()

    def click_add_remove(self):
        self.add_remove_button.click()

    def click_download_secure(self):
        self.download_secure_button.click()