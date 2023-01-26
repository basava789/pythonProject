from selenium import webdriver
import pytest
@pytest.fixture()
def driver1():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver