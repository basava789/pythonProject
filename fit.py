from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


def test_fit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://fratelloinnotech.com/")
    print(driver.title)
    time.sleep(4)
    driver.find_element(By.LINK_TEXT, "Internships").click()
    time.sleep(3)
    driver.find_element(By.ID, 'name').send_keys('Basavaraja')
    driver.find_element(By.ID, "rmail").send_keys("basava.raju949@gmail.com")
    driver.find_element(By.ID, 'phone').send_keys("7893420283")
    driver.find_element(By.ID, 'address').send_keys('hyderabad')
    driver.find_element(By.ID, 'college').send_keys('jntu')
    Select(driver.find_element(By.ID, 'stream')).select_by_visible_text("Bca")
    Select(driver.find_element(By.ID, 'technology')).select_by_visible_text('Java')
    time.sleep(5)
    driver.execute_script('window.scrollBy(0,70)')
    time.sleep(4)
    Select(driver.find_element(By.ID, 'domain')).select_by_visible_text("IOT")
    driver.find_element(By.ID, 'skills').send_keys("python")
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="ol-faq"]/div/div/div/div/div[2]/div/div[2]/div/form/input').click()
    time.sleep(4)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)


def test_dummypoint():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.dummypoint.com/Windows.html")
    print(driver.title)
    time.sleep(5)

    openpopup=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[2]/div/form/input[1]' )
    openpopup.click()
    time.sleep(6)


    mainwindow=driver.current_window_handle
    windowlist=driver.window_handles
    for window in windowlist:
        if window != mainwindow:
            driver.switch_to.window(window)
            print("sud", driver.title)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[1]/div/div[1]/a').click()
            time.sleep(4)
            driver.find_element(By.ID, 'user_input').send_keys("basavaraja")
            time.sleep(5)

    time.sleep(5)
    link=driver.find_elements(By.TAG_NAME, 'a')
    print('total links', len(link))
    driver.switch_to.window(mainwindow)
    print(driver.title)
    driver.close()

def test_farmhand():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.dummypoint.com/Frame.html")
    print(driver.current_url)
    time.sleep(4)

    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/section/div[1]/div/div[4]/a').click()
    time.sleep(3)

    driver.switch_to.frame(0)
    time.sleep(3)
    driver.find_element(By.NAME, 'promtalert').click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(2)

    driver.switch_to.frame(1)
    time.sleep(3)
    driver.find_element(By.NAME, 'promtalert').click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(3)
    driver.switch_to.default_content()

    driver.switch_to.frame(2)
    time.sleep(3)
    driver.find_element(By.NAME, 'promtalert').click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(3)
    driver.save_screenshot("dummy2.png")
    driver.switch_to.default_content()
    time.sleep(4)
    driver.close()
