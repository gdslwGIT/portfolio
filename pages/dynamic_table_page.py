from playwright.sync_api import Page

class DynamicTablePage:
    def __init__(self, page: Page):
        self.page = page
        self.chrome_cpu_cell = page.get_by_role("row", name="Chrome").locator("td").filter(has_text="%")
        self.yellow_label = page.locator("#chrome-cpu")

    def get_chrome_cpu_value(self):
        return self.chrome_cpu_cell.inner_text()
    
    def get_yellow_label_text(self):
        return self.yellow_label.inner_text()