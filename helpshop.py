from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import test_p
import test_data1

def load_broweser():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)

def load_website(url):
    driver.get(url)
    print(driver.title)
    time.sleep(4)

def login_verify():
    loginbtn = driver.find_element(By.XPATH, test_p.login_locater_xpath)
    loginbtn.click()
    uname = driver.find_element(By.NAME, test_p.username_locator_name)
    uname.send_keys(test_data1.username)
    password = driver.find_element(By.NAME, test_p.password_locator_name)
    password.send_keys(test_data1.password)
    login = driver.find_element(By.XPATH, test_p.login_btn_locater_xpath)
    login.click()
def close_browser():
    time.sleep(5)
    driver.close()