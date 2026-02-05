import pytest



def pytest_addoption(parser):
    parser.addoption(
        "--browser_instance", action="store", default="chrome", help="select browser instance"
    )
@pytest.fixture(scope="session")
def preSetupWork():
    print("I setup browser instance")

@pytest.fixture(scope="session")
def creds(request):
    return request.param

@pytest.fixture
def browser_instance(playwright,request):
    browser_instance = request.config.getoption("browser_instance")
    if browser_instance == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_instance == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()





