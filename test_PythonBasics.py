import time
from playwright.sync_api import Page


def test_browser_launch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    time.sleep(5)

def test_launch(page:Page):
    page.goto("https://www.google.com")
    time.sleep(5)