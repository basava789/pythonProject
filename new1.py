from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def test_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    print(driver.current_url)
    time.sleep(4)
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5').click()
    time.sleep(6)

    driver.find_element(By.XPATH, '//*[@id="item-0"]/span').click()
    time.sleep(3)
    driver.find_element(By.ID, 'userName').send_keys('basava')

    driver.find_element(By.ID, 'userEmail').send_keys('basava.raju949@gamil.com')
    driver.find_element(By.ID, 'currentAddress').send_keys('hyderabad')
    driver.find_element(By.ID, 'permanentAddress').send_keys('hyderabad')
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()

    driver.find_element(By.XPATH, '//*[@id="item-1"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]').click()
    time.sleep(2)
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[3]').click()
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[3]').click()
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="item-2"]/span').click()
    time.sleep(4)

    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="item-3"]/span').click()
    time.sleep(4)
    #driver.find_element(By.ID, 'addNewRecordButton').click()
    #time.sleep(10)
    # mainwindow = driver.current_window_handle
    # windowlist = driver.window_handles
    # for window in windowlist:
    #     if window != mainwindow:
    #         driver.switch_to.window(window)
    #         print("sud", driver.title)
    #         time.sleep(4)
    #         driver.find_element(By.ID, 'firstName').send_keys('basava')
    #         time.sleep(4)
    #         driver.find_element(By.ID, 'lastName').send_keys('raja')
    #         time.sleep(4)
    #         driver.find_element(By.ID, 'userEmail').send_keys('basava.ra@gmail.com')
    #         time.sleep(3)
    #         driver.find_element(By.ID, 'age').send_keys("26")
    #         time.sleep(3)
    #         driver.find_element(By.ID, 'salary').send_keys("40000")
    #         time.sleep(3)
    #         driver.find_element(By.ID, 'department').send_keys('IT')
    #         driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    #         time.sleep(10)



