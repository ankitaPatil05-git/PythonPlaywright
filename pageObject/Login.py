from pageObject.Dashboard import Dashboard


class Login:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,login, password):
        self.page.get_by_placeholder("email@example.com").fill(login)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = Dashboard(self.page)
        return dashboardPage

