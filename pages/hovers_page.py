from playwright.sync_api import Page

class HoversPage:
    def __init__(self, page: Page):
        self.page = page

    def get_user_avatar(self, user_id: int):
        return self.page.locator(f'[data-testid="user-{user_id}"]')

    def get_user_caption(self, user_id: int):
        return self.page.locator(f'[data-testid="user-{user_id}"] .figcaption')

    def get_user_name(self, user_id: int):
        return self.page.locator(f'[data-testid="user-{user_id}"] h5')

    def get_user_link(self, user_id: int):
        return self.page.locator(f'[data-testid="user-{user_id}"] a')