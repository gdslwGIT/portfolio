from playwright.sync_api import Page

class NotesAppPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.logout_btn = page.locator("[data-testid='logout']")
        self.add_note_btn = page.locator("[data-testid='add-new-note']")
        self.search_btn = page.locator("[data-testid='search-btn']")
        
        self.note_category_select = page.locator("[data-testid='note-category']")
        self.note_completed_checkbox = page.locator("[data-testid='note-completed']")
        self.note_title_input = page.locator("[data-testid='note-title']")
        self.note_description_input = page.locator("[data-testid='note-description']")
        self.note_submit_btn = page.locator("[data-testid='note-submit']")
        self.note_cancel_btn = page.locator("[data-testid='note-cancel']")

    def create_note(self, title: str, description: str, category: str = "Home", completed: bool = False):
        self.add_note_btn.click()
        self.note_category_select.select_option(category)
        if completed:
            self.note_completed_checkbox.check()
        self.note_title_input.fill(title)
        self.note_description_input.fill(description)
        self.note_submit_btn.click()
