from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_shop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("http://demo.skillshoppy.com/")
    # print(driver.title)
    # print(driver.current_url)
    # time.sleep(4)
    # driver.find_element(By.XPATH, '//*[@title="Register"]').click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//input[@name="usern"]').send_keys('Basava')
    # time.sleep(4)
    # driver.find_element(By.XPATH, '//*[@type="email"]').send_keys("rajabasava408@gmail.com")
    # time.sleep(4)
    # driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("basava@949")
    # time.sleep(4)
    # driver.find_element(By.XPATH, '//*[@name="cpasswd"]').send_keys('basava@949')
    # time.sleep(4)
    # driver.find_element(By.XPATH, '//*[text()="Sign up"]').click()
    # time.sleep(10)
    driver.get('http://demo.skillshoppy.com/account/login')
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@type='text']").send_keys('basavaraja')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys('basava@949')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[text()="Login"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/i[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div[1]/a[2]').click()
    time.sleep(6)
    driver.find_element(By.XPATH, '/html/body/header/div[2]/div[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/div[2]/div[2]/div/a[5]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/center/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div[2]/a').click()
    time.sleep(3)
    driver.execute_script('window.scrollBy(0,500);')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pname"]').send_keys('basavaraja')
    time.sleep(4)
    driver.close()