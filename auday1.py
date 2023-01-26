from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_load():
    for i in range(1,11):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://mathup.com/games/crossbit")
        btn =driver.find_element(By.XPATH,"//div[text()='Play']")
        btn.click()
        time.sleep(5)
        diff_level = driver.find_element(By.XPATH,"(//*[@class='GamePostStart_value__zH0b9'])[5]")
        print("difficulty level is", diff_level.text)
        time.sleep(4)
        driver.close()
def test_loadtime():
    total_time=0
    for i in range(1, 11):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://mathup.com/games/crossbit")
        btn =driver.find_element(By.XPATH, "//div[text()='Play']")
        t1 = datetime.now()
        btn.click()
        t2 = datetime.now()
        d = t2-t1
        total_time+=d.total_seconds()*1000
        driver.close()
    print("avg time in milli seconds ", total_time/10)
