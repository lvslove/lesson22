import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext, expect

# Папки для вывода
screenshots_folder = "output/screenshots"
videos_folder = "output/videos"
trace_folder = "output/trace"

@pytest.fixture(scope="function")
def playwright_setup() -> Page:
    with sync_playwright() as playwright:
        # Запуск браузера
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=videos_folder)  # Включаем запись видео
        page = context.new_page()

        # Включаем трассировку
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page  # Передаем страницу в тест

        # Завершаем трассировку 
        context.tracing.stop(path=f"{trace_folder}/trace.zip")
        
        # Сделаем скриншот перед завершением теста
        page.screenshot(path=f"{screenshots_folder}/{page.title()}_final.png")

        context.close()
        browser.close()  # Закрываем браузер

def test_valid_login(playwright_setup):
    page = playwright_setup
    page.goto("https://www.saucedemo.com/")

    # Скриншот страницы перед действиями
    page.screenshot(path=f"{screenshots_folder}/login_page.png")
    
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Скриншот после логина
    page.screenshot(path=f"{screenshots_folder}/after_login.png")
    
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()

def test_invalid_login(playwright_setup):
    page = playwright_setup
    page.goto("https://www.saucedemo.com/")
    
    # Скриншот страницы перед логином
    page.screenshot(path=f"{screenshots_folder}/invalid_login_page.png")
    
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"login-button\"]").click()

    # Скриншот после неудачного логина
    page.screenshot(path=f"{screenshots_folder}/error_login_page.png")
    
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Password is required")