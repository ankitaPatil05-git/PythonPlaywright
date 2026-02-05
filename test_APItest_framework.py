# https://rahulshettyacademy.com/client
import json

import pytest
from playwright.sync_api import Playwright
from APIUtils.APIBaseClassFramework import APIUtils
from pageObject.Login import Login

with open("data/creds.json") as f:
    creds = json.load(f)
    creds_list = creds['credentials']

@pytest.mark.parametrize("creds", creds_list)
def test_API_test(playwright:Playwright, creds, browser_instance):

    email = creds['userEmail']
    password = creds['userPassword']


    login = Login(browser_instance)
    login.navigate()

    #Logintest_APItest.py
    dashboardPage = login.login(email,password)

    #Create order
    apiObj = APIUtils()
    orderID = apiObj.createOrder(playwright, creds)

    orderhistory = dashboardPage.orderNavigation()

    orderdetails =orderhistory.selectOrder(orderID)

    orderdetails.verifyDetails()


