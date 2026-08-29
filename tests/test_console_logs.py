from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.console_logs_page import ConsoleLogsPage

def test_console_logs(page: Page, home: HomePage, console_logs_page: ConsoleLogsPage):
    captured_messages = []
    page.on("console", lambda msg: captured_messages.append((msg.type, msg.text)))

    home.click_console_logs()
    page.wait_for_url("**/console-logs")
    page.wait_for_timeout(1000)

    assert any(t == "log" and "The page was successfully loaded" in text for t, text in captured_messages), \
        "Expected page load log was not found"

    captured_messages.clear()
    console_logs_page.btn_log.click()
    page.wait_for_timeout(500)
    assert any(t == "log" and "[console.log()]" in text and "simple message" in text for t, text in captured_messages), \
        f"Expected console.log not found, got: {captured_messages}"

    captured_messages.clear()
    console_logs_page.btn_warn.click()
    page.wait_for_timeout(500)
    assert any(t == "warning" and "[console.warn()]" in text and "warning message" in text for t, text in captured_messages), \
        f"Expected console.warn not found, got: {captured_messages}"

    captured_messages.clear()
    console_logs_page.btn_error.click()
    page.wait_for_timeout(500)
    assert any(t == "error" and "[console.error()]" in text and "error message" in text for t, text in captured_messages), \
        f"Expected console.error not found, got: {captured_messages}"

    captured_messages.clear()
    console_logs_page.btn_info.click()
    page.wait_for_timeout(500)
    assert any(t == "info" and "[console.info()]" in text and "info message" in text for t, text in captured_messages), \
        f"Expected console.info not found, got: {captured_messages}"

    captured_messages.clear()
    console_logs_page.btn_debug.click()
    page.wait_for_timeout(500)
    assert any(t == "debug" and "[console.debug()]" in text and "debugging message" in text for t, text in captured_messages), \
        f"Expected console.debug not found, got: {captured_messages}"

    captured_messages.clear()
    console_logs_page.btn_table.click()
    page.wait_for_timeout(500)
    assert any(t == "table" and "[Object, Object]" in text for t, text in captured_messages), \
        f"Expected console.table not found, got: {captured_messages}"
