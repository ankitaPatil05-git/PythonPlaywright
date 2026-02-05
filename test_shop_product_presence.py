from playwright.sync_api import Page

from pageObject.LoginPractise import LoginPractise


def test_iphone_x_present_on_shop_page(page: Page):
    login = LoginPractise(page)
    login.navigate()
    shop = login.login("rahulshettyacademy", "Learning@830$3mK2")
    shop.wait_for_shop_page()
    shop.verify_product_present("iphone X")
