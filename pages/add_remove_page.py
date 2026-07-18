from playwright.sync_api import Page

class AddRemovePage: 
    def __init__(self, page: Page):
        self.page = Page
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_button = page.get_by_role("button", name="Delete")

    def add_element(self):
        self.add_button.click()

    def delete_element(self):
        self.delete_button.first.click()
