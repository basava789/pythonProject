from selenium import webdriver
import pytest
@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    return driver