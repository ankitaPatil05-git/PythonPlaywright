from pageObject.orderHistory import OrderHistory


class Dashboard:

    def __init__(self, page):
        self.page = page

    def orderNavigation(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderhistory = OrderHistory(self.page)
        return orderhistory


