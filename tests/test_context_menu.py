from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.context_menu_page import ContextMenuPage

def test_context_menu_alert(page: Page, home: HomePage, context_menu_page: ContextMenuPage):
    home.click_context_menu()
    page.wait_for_url("**/context-menu")
    page.wait_for_timeout(1000)
    def handle_dialog(dialog):
        assert dialog.message == "You selected a context menu", f"Unexpected alert text: {dialog.message}"
        dialog.accept()
    page.once("dialog", handle_dialog)
    context_menu_page.right_click()
    page.wait_for_timeout(1000)