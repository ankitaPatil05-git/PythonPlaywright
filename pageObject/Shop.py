from playwright.sync_api import expect


class Shop:

    def __init__(self, page):
        self.page = page

    def wait_for_shop_page(self):
        expect(self.page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")

    def verify_product_present(self, product_name):
        product_card = self.page.locator("app-card").filter(has_text=product_name)
        expect(product_card).to_have_count(1)
