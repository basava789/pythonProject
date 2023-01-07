from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


import time
from selenium.webdriver import ChromeOptions

ops = webdriver.ChromeOptions()
ops.add_argument("--disable notification")

def test_mylocation():
    driver = webdriver.Chrome(options=ops)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(4)
    driver.find_element(By.XPATH, "//div[@class='_331-kn _2tvxW']//div[7]//a[1]").click()
    time.sleep(10)
    driver.find_element(By.NAME, "0-departcity").send_keys("Hyderabad")
    driver.find_element(By.NAME, "0-arrivalcity").send_keys("Mumbai")
    time.sleep(3)
    driver.find_element(By.NAME, "0-datefrom").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//div[@class='_1psGvi _2DkHXl']//div").click()
    driver.find_element(By.NAME, "0-dateto")

    time.sleep(10)

