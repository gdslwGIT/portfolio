from playwright.sync_api import Page


class FormValidationPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_name = page.get_by_label("Contact Name")
        self.contact_number = page.locator('input[name="contactnumber"]')
        self.pickup_date = page.locator('input[name="pickupdate"]')
        self.payment_method = page.get_by_label("Payment Method")
        self.submit_button = page.get_by_role("button", name = "Register",exact = True)
        self.success_message = page.locator(".alert-info")

    def fill_form(self, name:str, phone: str, date: str, payment_value: str):
        self.contact_name.fill(name)
        self.contact_number.fill(phone)
        self.pickup_date.fill(date)
        self.payment_method.select_option(value = payment_value)

    def click_submit(self):
        self.submit_button.click()

    
        
        
        