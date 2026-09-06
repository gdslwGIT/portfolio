from playwright.sync_api import Page

class NotesAppPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.logout_btn = page.locator("[data-testid='logout']")
        self.add_note_btn = page.locator("[data-testid='add-new-note']")
        
        self.search_input = page.locator("[data-testid='search-input']")
        self.search_btn = page.locator("[data-testid='search-btn']")
        
        self.category_all_btn = page.locator("[data-testid='category-all']")
        self.category_home_btn = page.locator("[data-testid='category-home']")
        self.category_work_btn = page.locator("[data-testid='category-work']")
        self.category_personal_btn = page.locator("[data-testid='category-personal']")
        
        self.note_card = page.locator("[data-testid='note-card']")
        self.note_title = page.locator("[data-testid='note-card-title']")
        self.note_description = page.locator("[data-testid='note-card-description']")
        self.toggle_completed_switch = page.locator("[data-testid='toggle-note-switch']")
        self.note_edit_btn = page.locator("[data-testid='note-edit']")
        self.note_delete_btn = page.locator("[data-testid='note-delete']")
        self.note_delete_confirm_btn = page.locator("[data-testid='note-delete-confirm']")

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

    def search_notes(self, query: str):
        self.search_input.fill(query)
        self.search_btn.click()

    def delete_first_note(self):
        self.note_delete_btn.first.click()
        if self.note_delete_confirm_btn.is_visible():
            self.note_delete_confirm_btn.click()
