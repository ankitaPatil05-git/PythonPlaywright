from http.client import responses

from playwright.sync_api import Playwright


class APIUtils:

    def get_token(self,playwright:Playwright):
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        # email = creds['userEmail']
        # password = creds['userPassword']
        response = api_context.post(url="/api/ecom/auth/login",
                         data={"userEmail": "xorise8767@1200b.com","userPassword": "Aa@12345678"})
        #assert response.json().ok
        res_body = response.json()
        token = res_body["token"]
        return token

    def createOrder(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post(url="/api/ecom/order/create-order",
                         data={"orders":[{"country":"India","productOrderedId":"6964af52c941646b7a919472"}]},
                         headers={"Authorization": token})
        #assert  response.json().ok
        responseBody = response.json()
        orderID = responseBody["orders"][0]
        return orderID

