from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.color_wheel_page import ColorWheelPage

def test_color_wheel_elements_visible(page: Page, home: HomePage, color_wheel_page: ColorWheelPage):
    home.click_color_wheel()
    page.wait_for_url("**/color-wheel")
    page.wait_for_timeout(500)

    expect(color_wheel_page.play_button).to_be_visible()
    expect(color_wheel_page.reset_button).to_be_visible()
    expect(color_wheel_page.color_wheel_canvas).to_be_visible()

def test_play_game_shows_answers(page: Page, home: HomePage, color_wheel_page: ColorWheelPage):
    home.click_color_wheel()
    page.wait_for_url("**/color-wheel")
    page.wait_for_timeout(500)

    color_wheel_page.click_play()
    page.wait_for_timeout(1000)

    expect(color_wheel_page.answers_container).to_be_visible()

def test_correct_color_answer(page: Page, home: HomePage, color_wheel_page: ColorWheelPage):
    home.click_color_wheel()
    page.wait_for_url("**/color-wheel")
    page.wait_for_timeout(500)

    color_wheel_page.click_play()
    page.wait_for_timeout(1500)

    target_color = color_wheel_page.get_selected_color()
    color_wheel_page.click_color_answer(target_color.capitalize())
    page.wait_for_timeout(500)

    expect(color_wheel_page.result_text).to_have_text("")

def test_wrong_color_answer(page: Page, home: HomePage, color_wheel_page: ColorWheelPage):
    home.click_color_wheel()
    page.wait_for_url("**/color-wheel")
    page.wait_for_timeout(500)

    color_wheel_page.click_play()
    page.wait_for_timeout(1500)

    target_color = color_wheel_page.get_selected_color()
    colors = ["Red", "Green", "Blue", "Yellow", "Violet", "Gray", "Pink"]
    wrong_color = next(c for c in colors if c.lower() != target_color.lower())

    color_wheel_page.click_color_answer(wrong_color)
    page.wait_for_timeout(500)

    expect(color_wheel_page.result_text).to_contain_text("Incorrect Answer")

def test_reset_game(page: Page, home: HomePage, color_wheel_page: ColorWheelPage):
    home.click_color_wheel()
    page.wait_for_url("**/color-wheel")
    page.wait_for_timeout(500)

    color_wheel_page.click_play()
    page.wait_for_timeout(1000)

    color_wheel_page.click_reset()
    page.wait_for_timeout(500)

    expect(color_wheel_page.play_button).to_be_visible()
