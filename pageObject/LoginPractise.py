from pageObject.Shop import Shop


class LoginPractise:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username, password):
        self.page.get_by_label("Username:").fill(username)
        self.page.get_by_label("Password:").fill(password)
        self.page.get_by_role("combobox").select_option("teach")
        self.page.locator("#terms").check()
        self.page.get_by_role("button", name="Sign In").click()
        shop = Shop(self.page)
        return shop
