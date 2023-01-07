from selenium import webdriver
from selenium.webdriver.common.by import By
import test_datenop
import test_pomnop
import time

def load_browcer():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)

def load_website(url):
    driver.get(url)
    print(driver.title)
    time.sleep(4)

def login_verfiy():
    driver.find_element(By.XPATH,test_pomnop.login_locetor_xpath).click()
    time.sleep(3)
    driver.find_element(By.ID,test_pomnop.email_locetore_id).send_keys(test_datenop.Email)
    time.sleep(3)
    driver.find_element(By.ID, test_pomnop.password_locetore_id).send_keys(test_datenop.password)
    time.sleep(3)
    driver.find_element(By.XPATH, test_pomnop.log_btn_locetore_xpath).click()
    time.sleep(20)
    print(driver.title)
    actulresult = driver.title
    expetedresult ="nopCommerce demo store. Login"
    assert actulresult == expetedresult, "did not showing the log in page"
    time.sleep(3)
    msg=driver.find_element(By.XPATH, test_pomnop.mesg_locetore_xpat)
    print("error = ", msg.text)

def close_browcer():
    time.sleep(4)
    driver.close()