import time
from time import sleep

from playwright.sync_api import Playwright, expect

from APIUtils.APIBaseClass import APIUtils

fakepayload = {"data":[],"message":"No Orders"}

def decrepit(route):
    route.fulfill(
        json= fakepayload
    )
def call2(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_network1(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", decrepit)

    #Login
    page.get_by_placeholder("email@example.com").fill("xorise8767@1200b.com")
    page.get_by_placeholder("enter your passsword").fill("Aa@12345678")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    time.sleep(5)

def test_network2(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", call2)
    #Login
    page.get_by_placeholder("email@example.com").fill("xorise8767@1200b.com")
    page.get_by_placeholder("enter your passsword").fill("Aa@12345678")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    message = page.locator(".blink_me").text_content()
    print(message)

def test_session_skip(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    apiobj = APIUtils()
    token = apiobj.get_token(playwright)
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()


