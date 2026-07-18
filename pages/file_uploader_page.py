from playwright.sync_api import Page

class FileUploaderPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input = page.locator("#fileInput")
        self.upload_button = page.locator("#fileSubmit")
        self.upload_files_header = page.locator("h1")
        self.upload_file_name = page.locator("#uploaded-files")

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
        
    def click_upload_button(self):
        self.upload_button.click()

