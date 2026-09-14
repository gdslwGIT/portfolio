from playwright.sync_api import Page

class ApiDocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.swagger_ui = page.locator("#swagger-ui")
        self.info_title = page.locator(".swagger-ui .info .title")
        self.opblock_summaries = page.locator(".swagger-ui .opblock-summary")
        self.opblocks = page.locator(".swagger-ui .opblock")

    def get_endpoints_count(self) -> int:
        return self.opblock_summaries.count()

    def get_endpoint_text(self, index: int = 0) -> str:
        return self.opblock_summaries.nth(index).inner_text()

    def expand_endpoint(self, index: int = 0):
        self.opblock_summaries.nth(index).click()
