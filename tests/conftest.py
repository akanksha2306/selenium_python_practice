import pytest

from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import Login_page
from pages.courses.register_courses_page import Register_courses_page


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType, baseUrl):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, osType, baseUrl)

    driver = wdf.getWebDriverInstance()
    lp = Login_page(driver)
    lp.login("akankshakanjolia@gmail.com" , "helloworld")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser", help="Target browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--baseUrl", help = "baseUrl of website to test")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="session")
def baseUrl(request):
    return request.config.getoption("--baseUrl")