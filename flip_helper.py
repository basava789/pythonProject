from selenium import webdriver
from selenium.webdriver.common.by import By
import date_flip
import locate_flip
import time

def load_broswer():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(4)

def load_website():
    driver.get(date_flip.url)
    print(driver.title)
    time.sleep(4)

def load_search():
    driver.find_element(By.XPATH, locate_flip.test_locter_xpath).click()
    time.sleep(3)
    driver.find_element(By.XPATH, locate_flip.serch_locter_xpath).send_keys(date_flip.name)
    time.sleep(4)
    driver.find_element(By.XPATH, locate_flip.serchicon_locter_xpath).click()
    time.sleep(10)
    driver.find_element(By.XPATH, locate_flip.moblie_loceter_xpath).click()
    time.sleep(4)
def load_mobile():
    mainwindow=driver.current_window_handle
    windowlist = driver.window_handles
    for window in windowlist:
        if window != mainwindow:
            driver.switch_to.window(window)
            driver.find_element(By.XPATH, locate_flip.addcart_loctore_xpath).click()
            time.sleep(3)
            tag=driver.find_element(By.LINK_TEXT, "REDMI 9i Sport (Carbon Black, 64 GB)")
            print("tag name = ", tag.text)
            driver.close()
    driver.switch_to.window(mainwindow)
    time.sleep(4)
    mesg1=driver.find_element(By.XPATH, locate_flip.moblie_loceter_xpath)
    print(mesg1.text)
def close_browser():
    time.sleep(4)
    driver.close()
