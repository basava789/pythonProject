# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# webdriver.ChromeOptions()
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# def test_load():
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     mywait=WebDriverWait(driver, 10, ignored_exceptions=[Exception])
#     driver.get("https://www.flipkart.com/")
#     time.sleep(3)
#
#     mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='container']/div/div[3]/div[3]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/a/div[1]/div/img"))).click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]').click()
#     time.sleep(4)
#     mainwindow=driver.current_window_handle
#     windowlist=driver.window_handles
#     for window in windowlist:
#         if window != mainwindow:
#             driver.switch_to.window(window)
#             driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button').click()
#             time.sleep(4)
#
#             driver.switch_to.default_content()
#
#     time.sleep(6)
#     driver.close()
#
# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable-notification")
# def test_my():
#     driver=webdriver.Chrome(options=ops)
#     driver.maximize_window()
#     driver.get("https://www.gps-coordinates.net")
#     driver.back()
#     time.sleep(5)
#     driver.forward()
#     time.sleep(5)

# def Program(func):
#     def test(*args,**kwargs):
#         value=func(*args,**kwargs)
#         return value
#     return test
# @Programe
# def Cal(x, y):
#     return x+y
# x,y=2,3
# print(x,y)


# def Task(p,i):
#     i=iter(i)
#     for x in i:
#         if not p(x):
#             yield x
#             break
def Rectangler(object):
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def area(self):
        return self.width*self.height

