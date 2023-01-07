from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

def test_load():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    print(driver.title)

    time.sleep(4)
    driver.close()
# from selenium import webdriver
# from webdriver_manager .chrome import ChromeDriverManager
# import time
# import pytest
#
# def test_ravi():
#     drive=webdriver.Chrome(ChromeDriverManager().install())
#     drive.maximize_window()
#     drive.get("https://www.facebook.com")
#     print(drive.title)
#     time.sleep(6)
#     drive.close()
#
# from selenium import webdriver
# from webdriver_manager .microsoft import EdgeChromiumDriverManager
#
# import time
# import pytest
#
# def test_raju():
#     why=webdriver.Edge(EdgeChromiumDriverManager().install())
#     why.get("https://youtude.com")
#     why.maximize_window()
#     print(why.title)
#     time.sleep(10)
#     why.close()

#
# from selenium import webdriver
# import time
#
#
# def test_youtube():
#     drive=webdriver.Chrome()
#     drive.get("https://www.google.com")
#     drive.maximize_window()
#     print(drive.title)
#     time.sleep(5)
#     drive.close()