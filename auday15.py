from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_the():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()
    alt=driver.switch_to.alert
    print("alerts =", alt.text)
    alt.dismiss()
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
    altr2=driver.switch_to.alert
    time.sleep(3)
    altr2.send_keys("raju")
    time.sleep(5)
    altr2.accept()
    time.sleep(4)
    driver.close()