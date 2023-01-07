import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_verify():
    driver = webdriver.Chrome()
    driver.get("http://www.fratelloinnotech.com/")
    driver.maximize_window()
    print(driver.title)

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Internships').click()
    time.sleep(5)
    driver.find_element(By.ID, 'name').send_keys('basavaraja')
    time.sleep(2)

    driver.find_element(By.ID, 'rmail').send_keys("basava.raju949@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, 'phone').send_keys("7893420283")
    time.sleep(2)
    driver.find_element(By.ID, 'address').send_keys('hyderabad')
    time.sleep(2)
    driver.find_element(By.ID, 'college').send_keys('jntu')
    degree = Select(driver.find_element(By.ID, 'stream'))
    degree.select_by_visible_text("Mca")

    technology = Select(driver.find_element(By.ID, 'technology'))
    technology.select_by_visible_text("Python")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    domain = Select(driver.find_element(By.NAME, 'domain'))
    domain.select_by_visible_text("IOT")
    driver.find_element(By.ID, 'skills').send_keys("java")
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[@id='ol-faq']/div/div/div/div/div[2]/div/div[2]/div/form/input").click()
    time.sleep(5)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(4)
    driver.close()




