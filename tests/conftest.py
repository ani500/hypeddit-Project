import pytest

from base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="class")
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, baseUrl):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser,baseUrl)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.baseUrl = baseUrl
    yield driver,baseUrl
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="Browser to use: chrome or firefox")
    parser.addoption("--baseUrl", default="https://hypeddit.com/", help="Base URL of the application under test")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def baseUrl(request):
    return request.config.getoption("--baseUrl")
