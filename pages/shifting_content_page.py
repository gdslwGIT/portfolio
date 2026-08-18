from playwright.sync_api import Page

class ShiftingContentPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.menu_element_link = page.locator("a[href='/shifting-content/menu']")
        self.image_element_link = page.locator("a[href='/shifting-content/image']")
        self.list_element_link = page.locator("a[href='/shifting-content/list']")
        
        self.shift_element = page.locator("#shift")
        
        self.list_items = page.locator("ol li")
