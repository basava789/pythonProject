from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By


@pytest.mark.parametrize("flipkart", ["chrome", "edge"])
def test_flipverfiy(flipkart):
    global driver
    if flipkart == "chrome":
        driver=webdriver.Chrome()
    elif flipkart == "edge":
        driver=webdriver.Edge()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.close()


def test_rrr():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://itera-qa.azurewebsites.net/home/automation")
    print(driver.title)
    check=driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id,"day")]')
    print(len(check))
    #for i in range(len(check)):
       # check[i].click()
    # for checks in check:
    #     weakname=checks.get_attribute("id")
    #     if weakname == 'monday' or weakname == "sunday" or weakname == "friday":
    #         checks.click()
    # for i in range(len(check)-3, len(check)):
    #     check[i].click()
    for i in range(len(check)):
        if i<3:
            check[i].click()
    link=driver.find_elements(By.TAG_NAME, 'a')
    print('Total num links :-', link)
    time.sleep(4)