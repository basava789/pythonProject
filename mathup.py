# from datetime import datetime
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# def test_loadtime():
#     total_time=0
#     for i in range(1, 11):
#         driver=webdriver.Chrome(ChromeDriverManager().install())
#         driver.maximize_window()
#         t1 = datetime.now()
#         driver.get("https://mathup.com/games/crossbit")
#         t2 = datetime.now()
#         t2 = datetime.now()
#         d = t2-t1
#         total_time+=d.total_seconds()
#         driver.close()
#     print("avg time in seconds ", total_time//10)
import time

from selenium.webdriver.common.by import By


class car:
    def __init__(self,speed,clore, year):
        self.speed = speed
        self.clore = clore
        self.year = year
    def getbmw(self):
        print("BMW maximum speed is = ", self.speed)
        print("BMW clore of car = ", self.clore)
        print("BMW year of lunch = ", self.year)
    def getford(self):
        print("ford maximum speed is = ", self.speed)
        print("ford clore of car = ", self.clore)
        print("ford year of lunch = ", self.year)

BMW = car(155, 'RED', 2010)
ford = car(140, "YELLOW", 2015)

BMW.getbmw()
ford.getford()


from selenium import webdriver
from time import sleep
def test_lambdatest_google():
   chrome_driver = webdriver.Chrome()
   chrome_driver.get('https://www.google.com')
   chrome_driver.maximize_window()
   if not "Google" in chrome_driver.title:
       raise Exception("Could not load page")
   print(chrome_driver.title)
   time.sleep(6)
   element = chrome_driver.find_element(By.NAME, "q")
   element.send_keys("LambdaTest")
   element.submit()
   time.sleep(6)
   title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
   time.sleep(5)
   lt_link = chrome_driver.find_element(By.XPATH, "//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
   lt_link.click()
   time.sleep(5)
   sleep(5)
   assert title == chrome_driver.title
   sleep(2)
   chrome_driver.quit()

def test_youtube():
    driver=webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    serch = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    serch.send_keys('Songs')
    serch.submit()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="video-title"]').click()
    time.sleep(2)
    ttt=driver.find_element(By.XPATH,'//*[@id="video-title"]')
    print(ttt.text)





