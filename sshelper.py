from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import csv
import ssloceter
def abhi():
    with open('raju.csv', mode="r")as file:
        date=csv.reader(file)
        date1=[]
        for line in date:
            date1.append(line)
        return date1
list=abhi()
print(list)

@pytest.mark.parametrize("username,password", list)
def test_valid_login(username, password):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.skillshoppy.com/account/login")
    time.sleep(2)
    driver.find_element(By.NAME, ssloceter.login_username_locetor).send_keys(username)
    driver.find_element(By.NAME, ssloceter.login_password_locetor).send_keys(password)
    driver.find_element(By.NAME, ssloceter.login_button_locetor).click()
    try:
        mssge1=driver.find_element(By.XPATH, ssloceter.ms_expection)
        print(mssge1.text)
    except Exception as a:
        print("Error1 =", a)
    try:
        mssge2=driver.find_element(By.XPATH, ssloceter.ms1_expection)
        print(mssge2.text)
    except Exception as a:
        print("Error2 = ", a)
    time.sleep(6)
    driver.close()


