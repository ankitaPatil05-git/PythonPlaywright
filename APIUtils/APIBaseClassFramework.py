from http.client import responses

from playwright.sync_api import Playwright


class APIUtils:

    def get_token(self,playwright:Playwright, creds):
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        email = creds['userEmail']
        password = creds['userPassword']
        response = api_context.post(url="/api/ecom/auth/login",
                         data={"userEmail": email,"userPassword": password})
        #assert response.json().ok
        res_body = response.json()
        token = res_body["token"]
        return token

    def createOrder(self,playwright:Playwright,creds):
        token = self.get_token(playwright, creds)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post(url="/api/ecom/order/create-order",
                         data={"orders":[{"country":"India","productOrderedId":"6964af52c941646b7a919472"}]},
                         headers={"Authorization": token})
        #assert  response.json().ok
        responseBody = response.json()
        orderID = responseBody["orders"][0]
        return orderID