from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.typos_page import TyposPage

def test_typos(page: Page, home: HomePage, typos_page: TyposPage):
    home.click_typos()
    page.wait_for_url("**/typos")
    page.wait_for_timeout(1000)
    text = typos_page.get_paragraph_text()
    expected_texts = [
        "Sometimes you'll see a typo, other times you won't.",
        "Sometimes you'll see a typo, other times you won,t."
    ]
    assert text in expected_texts, f"Wrong text: {text}"
