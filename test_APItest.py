# https://rahulshettyacademy.com/client
from playwright.sync_api import expect
from playwright.sync_api import Playwright
from APIUtils.APIBaseClass import APIUtils


def test_API_test(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #Logintest_APItest.py
    page.get_by_placeholder("email@example.com").fill("xorise8767@1200b.com")
    page.get_by_placeholder("enter your passsword").fill("Aa@12345678")
    page.get_by_role("button",name="Login").click()

    #Create Order
    apiObj = APIUtils()
    orderID = apiObj.createOrder(playwright)
    page.get_by_role("button",name="ORDERS").click()

    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button",name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")


