import pytest
from selenium import webdriver


def demo_fixture():
    print("\nThis is demo fixture, it will run first, before testcase")
    yield
    print("\nThis is demo fixture, this will run after test cases")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope = "class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "edge":
        print("launching edge vrowser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    print("\nbrowser closed")
    driver.quit()

def pytest_metadata(metadata):
    # To add metadata
    metadata["Project Name"] = "CredKart"
    metadata["Module Name"] = "Login"
    metadata["Tester Name"] = "Credence"
    metadata["URL"] = "https://apps.credence.in/"
    # To remove metadata
    del metadata["Platform"]

    # edit summary in html report --> your task

@pytest.fixture(params=[
    ("credencejune01@credence.in", "Credence@123", "Pass"),
    ("credencejune01@credence.in1", "Credence@123", "Fail"),
    ("credencejune01@credence.in", "Credence@1231", "Fail"),
    ("credencejune01@credence.in1", "Credence@1231", "Fail")
])
def get_data_for_login(request): # function with parameter
    return request.param


