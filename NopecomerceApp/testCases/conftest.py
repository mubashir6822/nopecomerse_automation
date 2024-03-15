import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        print("Launching Chrome Browser.............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        print("Launching FireFox Browser............")
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.implicitly_wait(30)
        print("Launching Edge Browser...............")
    else:
        driver = webdriver.Ie()
        driver.implicitly_wait(30)

    return driver

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")
