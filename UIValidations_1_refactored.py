from playwright.sync_api import Page, expect

BASE_URL = "https://rahulshettyacademy.com/loginpagePractise/"
USERNAME = "rahulshettyacademy"
PASSWORD = "Learning@830$3mK2"
ROLE_OPTION = "teach"
PRODUCTS = ("iphone X", "Nokia Edge")


def _login(page: Page) -> None:
    page.goto(BASE_URL)
    page.get_by_label("Username:").fill(USERNAME)
    page.get_by_label("Password:").fill(PASSWORD)
    page.get_by_role("combobox").select_option(ROLE_OPTION)
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()


def _add_product_to_cart(page: Page, product_name: str) -> None:
    product_card = page.locator("app-card").filter(has_text=product_name)
    product_card.get_by_role("button").click()


def _extract_email(text: str) -> str:
    parts = text.split("at", 1)
    if len(parts) < 2:
        raise ValueError("Expected email text to contain 'at'.")
    return parts[1].strip().split(" ")[0]


def _open_child_page_and_get_email(page: Page) -> str:
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
    child_page = new_page_info.value
    text = child_page.locator(".red").text_content() or ""
    return _extract_email(text)


def test_ui_validation_dynamic_script(page: Page) -> None:
    _login(page)
    for product in PRODUCTS:
        _add_product_to_cart(page, product)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(len(PRODUCTS))


def test_add_val(page: Page) -> None:
    page.goto(BASE_URL)
    email = _open_child_page_and_get_email(page)
    print(email)
