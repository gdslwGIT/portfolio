from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.hovers_page import HoversPage

def test_hovers(page: Page, home: HomePage, hovers_page: HoversPage):
    home.click_hovers()
    page.wait_for_url("**/hovers")
    page.wait_for_timeout(1000)

    # 2. Проверяем каждого из 3 пользователей по очереди
    for i in range(1, 4):
        avatar = hovers_page.get_user_avatar(i)
        caption = hovers_page.get_user_caption(i)
        name = hovers_page.get_user_name(i)
        link = hovers_page.get_user_link(i)

        expect(caption).not_to_be_visible()

        avatar.hover()
        expect(caption).to_be_visible()
        expect(name).to_have_text(f"name: user{i}")
        expect(link).to_have_attribute("href", f"/users/{i}")
