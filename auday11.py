from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_flipkart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    print(driver.title)
    time.sleep(4)
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("basava.raju949@gmail.com")
    # time.sleep(2)
    # driver.find_element(By.XPATH, "//*[@type='password']").send_keys('basava949')
    # time.sleep(4)
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys('7893420283')
    # time.sleep(4)
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "//*[@type='password']").send_keys("basava@949")
    # time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[2]/a/div[2]").click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[2]/div[9]/div/div[2]/div[1]/div[2]/a/div[1]/div').click()
    time.sleep(4)
    mainwindow=driver.current_window_handle
    windowlist=driver.window_handles
    for window in windowlist:
        if window != mainwindow:
            driver.switch_to.window(window)
            print(driver.title)
            driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div/div[2]/div/ul/li/button').click()
            time.sleep(4)
            driver.close()
    time.sleep(10)
    driver.quit()

