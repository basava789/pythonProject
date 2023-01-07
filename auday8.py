

def test_JQure():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/droppable/')
    print(driver.title)
    print(driver.current_url)
    time.sleep(5)
    lis = driver.find_elements(By.TAG_NAME, 'a')
    for link in lis:
        print(link.text, '=', link.get_attribute('href'))
    driver.switch_to.frame(0)
    s = driver.find_element(By.ID, 'draggable')
    t = driver.find_element(By.ID, 'droppable')
    action = ActionChains(driver)
    action.drag_and_drop(s, t).perform()
    time.sleep(5)
    driver.close()


import time

def test_rest():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/droppable/#photo-manager')
    print(driver.title)
    print(driver.current_url)
    time.sleep(5)
    A = driver.find_elements(By.TAG_NAME, 'a')
    print(len(A))
    for B in A:
        print(B.text, '=', B.get_attribute('href'))
    driver.switch_to.frame(0)
    s1 = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')

    s2 = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[2]/img')
    s3 = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[3]/img')

    s4 = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[4]/img')
    T = driver.find_element(By.XPATH, '//*[@id="tr'
                                      'ash"]')
    ab = ActionChains(driver)
    ab.drag_and_drop(s1, T).perform()
    time.sleep(3)
    ab.drag_and_drop(s2, T).perform()
    time.sleep(4)
    ab.drag_and_drop(s3, T).perform()
    time.sleep(4)
    ab.drag_and_drop(s4, T).perform()
    driver.switch_to.default_content()

    time.sleep(5)
    driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_Qjery1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/droppable/#visual-feedback')
    print(driver.title)
    print(driver.current_url)
    time.sleep(4)
    c=driver.find_elements(By.TAG_NAME, 'a')
    print(len(c))
    for i in c:
        print(i.text, '=', i.get_attribute('href'))

    driver.switch_to.frame(0)
    s01=driver.find_element(By.ID, 'draggable')
    T1=driver.find_element(By.ID, 'droppable')
    s02 = driver.find_element(By.ID, 'draggable2')
    T2 = driver.find_element(By.ID, 'droppable2')
    a1=ActionChains(driver)
    a1.drag_and_drop(s01, T1).perform()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    a1.drag_and_drop(s02, T2).perform()
    time.sleep(4)
    driver.switch_to.default_content()
    time.sleep(2)
    driver.close()
