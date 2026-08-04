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
        self.notification_message_button = page.locator('a[href="/notification-message"].btn')
        self.autocomplete_button = page.locator('a[href="/autocomplete"].btn')
        self.cypress_spies_button = page.locator('a[href="/spies-stubs-clocks"].btn') 
        self.challenging_dom_button = page.locator('a[href="/challenging-dom"].btn')
        self.large_deep_dom_button = page.locator('a[href="/large"].btn')
        self.shadow_dom_button = page.locator('a[href="/shadowdom"].btn')
        self.typos_button = page.locator('a[href="/typos"].btn')
        self.my_ip_button = page.locator('a[href="/my-ip"].btn')
        self.broken_images_button = page.locator('a[href="/broken-images"].btn')
        self.infinite_scroll_button = page.locator('a[href="/infinite-scroll"].btn')
        self.slow_button = page.locator('a[href="/slow"].btn')
        self.js_dialogs_button = page.locator('a[href="/js-dialogs"].btn')
        self.js_error_button = page.locator('a[href="/javascript-error"].btn')
        self.jquery_button = page.locator('a[href="/jqueryui"].btn')
        self.a_b_button = page.locator('a[href="/abtest"].btn')
        self.checkboxes_button = page.locator('a[href="/checkboxes"].btn')
        self.context_menu_button = page.locator('a[href="/context-menu"].btn').first
        self.key_presses_button = page.locator('a[href="/key-presses"].btn')
        self.dissapearing_elements_button = page.locator('a[href="/disappearing-elements"].btn')
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

    def click_notification_message(self):
        self.notification_message_button.click()

    def click_autocomplete(self):
        self.autocomplete_button.click()
    
    def click_cypress_spies(self):
        self.cypress_spies_button.click()
    
    def click_challenging_dom(self):
        self.challenging_dom_button.click()
    
    def click_large_deep_dom(self):
        self.large_deep_dom_button.click()

    def click_shadow_dom(self):
        self.shadow_dom_button.click()

    def click_typos(self):
        self.typos_button.click()

    def click_my_ip(self):
        self.my_ip_button.click()

    def click_broken_images(self):
        self.broken_images_button.click()

    def click_infinite_scroll(self):
        self.infinite_scroll_button.click()

    def click_slow_page(self):
        self.slow_button.click()

    def click_js_dialogs(self):
        self.js_dialogs_button.click()

    def click_js_error(self):
        self.js_error_button.click()

    def click_jquery(self):
        self.jquery_button.click()

    def click_a_b(self):
        self.a_b_button.click()

    def click_checkboxes(self):
        self.checkboxes_button.click()

    def click_context_menu(self):
        self.context_menu_button.click()

    def click_key_presses(self):
        self.key_presses_button.click()

    def click_dissapearing_elements(self):
        self.dissapearing_elements_button.click()