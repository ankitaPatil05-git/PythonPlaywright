from pageObject.orderDetails import OrderDetails


class OrderHistory:

    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderID):
        row = self.page.locator("tr").filter(has_text=orderID)
        row.get_by_role("button", name="View").click()
        ordedetails = OrderDetails(self.page)
        return  ordedetails