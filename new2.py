from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def test_orange():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.orangehrm.com/")
    print(driver.current_url)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='myText']").send_keys('basava.raju949@gmail.com')
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@id='linkadd']").click()
    time.sleep(6)
    driver.execute_script('window.scrollBy(0,470);')
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='Form_getForm_subdomain']").send_keys('baass')
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='Form_getForm_Name']").send_keys('basavaraja')
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='Form_getForm_Contact']").send_keys("7893420283")
    time.sleep(5)
    Select(driver.find_element(By.XPATH, "//select[@id='Form_getForm_Country']")).select_by_visible_text("India")
    time.sleep(5)
    driver.execute_script('window.scrollBy(0,300);')
    #driver.find_element(By.XPATH, "//div[@class='btn-toolbar']").click()
    #time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='Form_getForm_action_submitForm']").click()
    time.sleep(5)
    driver.close()
