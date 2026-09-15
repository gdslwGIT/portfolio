from playwright.sync_api import Page, Locator

class PracticeApiDocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.swagger_ui = page.locator("#swagger-ui")
        self.info_title = page.locator(".swagger-ui .info .title")
        self.opblock_summaries = page.locator(".swagger-ui .opblock-summary")
        self.opblocks = page.locator(".swagger-ui .opblock")

    def get_endpoints_count(self) -> int:
        return self.opblock_summaries.count()

    def get_endpoint_by_id(self, operation_id: str) -> Locator:
        return self.page.locator(f"[id*='{operation_id}']")

    def execute_endpoint_by_id(self, operation_id: str):
        block = self.get_endpoint_by_id(operation_id)
        block.scroll_into_view_if_needed()
        if "is-open" not in (block.get_attribute("class") or ""):
            block.locator(".opblock-summary").click()
        try_btn = block.locator(".try-out__btn")
        try_btn.wait_for(state="visible", timeout=5000)
        if "cancel" not in (try_btn.get_attribute("class") or ""):
            try_btn.click()
        execute_btn = block.locator(".btn.execute")
        execute_btn.wait_for(state="visible", timeout=5000)
        execute_btn.click()

    def fill_param(self, operation_id: str, param_name: str, value: str):
        block = self.get_endpoint_by_id(operation_id)
        input_field = block.locator(f"input[placeholder='{param_name}'], input[data-param-name='{param_name}']").first
        if input_field.count() > 0:
            input_field.fill(value)

    def get_live_response_status(self, operation_id: str) -> Locator:
        block = self.get_endpoint_by_id(operation_id)
        status = block.locator(".live-responses-table .response .response-col_status, .live-responses-table .response-col_status:not(.col_header)").first
        status.wait_for(state="visible", timeout=10000)
        return status
