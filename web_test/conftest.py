import pytest
from selenium import webdriver
from web_app_test.app_test import data



@pytest.fixture(scope="function", params=data.get_browsers(), autouse=True)
def driver(request):
    browser = request.param["name"]
    options = request.param["options"]

    if browser == "Chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        driver = webdriver.Firefox(options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()
