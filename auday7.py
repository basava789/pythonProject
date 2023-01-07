from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_dummy():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.dummypoint.com/")
    autualresult = driver.title
    expetedresult = "General Dashboard — DummyPoint"
    assert autualresult == expetedresult
    print(driver.title)
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[5]/a/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[5]/ul/li[5]/a').click()
    time.sleep(4)
    driver.find_element(By.NAME, 'alertbutton').click()
    time.sleep(3)
    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(6)
    alert.accept()
    time.sleep(4)
    driver.save_screenshot("dummy.png")
    time.sleep(6)
    driver.close()


def test_nikhil():
    driver = webdriver.Chrome()
    driver.get('http://www.dummypoint.com/')
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)
    try:
        elment= WebDriverWait(driver,10).until\
            (EC.presence_of_element_located
             ((By.XPATH, '//*[@id="app"]/div/div[3]/section/div[1]/div/div[5]/a')))
        elment.click()
    finally:
        driver.close()
   # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[1]/div/div[5]/a').click()
    time.sleep(5)
    driver.save_screenshot("dummy1.png")
    driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[5]/ul/li[5]/a').click()
    driver.find_element(By.NAME, 'alertbutton').click()
    time.sleep(4)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)
    driver.close()
