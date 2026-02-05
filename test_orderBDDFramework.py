import playwright
import pytest
from pytest_bdd import given, parser, when, then, scenarios, parsers

from APIUtils.APIBaseClassFramework import APIUtils
from pageObject.Login import Login


scenarios('features/orderTransaction.feature')

@pytest.fixture
def sharedData():
    return {}

@given(parsers.parse("place the item order with {username} and {password}"))
def placeOrder(playwright,username, password, sharedData):
    creds = {}
    creds['userEmail'] = username
    creds['userPassword'] = password
    apiObj = APIUtils()
    orderId = apiObj.createOrder(playwright, creds)
    sharedData['order_id'] = orderId

@given('the user is on landing page')
def userOnLandingPage(playwright, browser_instance, sharedData):
    login = Login(browser_instance)
    login.navigate()
    sharedData['login_page'] = login

@when(parsers.parse('I login to portal with {username} and {password}'))
def loginPage(username, password, sharedData):
    login = sharedData['login_page']
    dashboardPage = login.login(username, password)
    sharedData['dashboard_page'] = dashboardPage

@when('navigate to orders page')
def ordersPage(sharedData):
    dashboardPage = sharedData['dashboard_page']
    orderhistory = dashboardPage.orderNavigation()
    sharedData['orderhistory_page'] = orderhistory

@when('select the orderId')
def select_order_id(sharedData):
    orderhistory = sharedData['orderhistory_page']
    orderId = sharedData['order_id']
    orderdetails = orderhistory.selectOrder(orderId)
    sharedData['orderDetails_page'] = orderdetails

@then('order message is successfully displayed')
def order_message_successfully_displayed(sharedData):
    orderdetails = sharedData['orderDetails_page']
    orderdetails.verifyDetails()