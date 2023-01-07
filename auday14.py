
# list2= [10, 200, 4, 45, 45, 201, 200, 201, 99]
# list1=set(list2)
# print(list1)
# list3=list(list1)
# list3.sort()
# print("second hightest num in list :-", list3[-2])

#
# list1=[12, 23, "python", 13, 23, 45, 67, 89, "ravi", 87, 89]
# print([[i, list1.count(i)] for i in list(list1)])

# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1, 2, -8]))

import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.support.select import Select

location = os.getcwd()
#
# def test_download():
#
#     perforance = {"download.default_directory":location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", perforance)
#     driver = webdriver.Chrome(options=ops)
#     driver.maximize_window()
#     driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download")
#     time.sleep(4)
#     driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
#     time.sleep(30)
#     driver.close()
# #
# def test_loadedge():
#
#     perforance = {"download.default_directory":location}
#     ops = webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs", perforance)
#     driver = webdriver.Edge(options=ops)
#     driver.maximize_window()
#     driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download")
#     time.sleep(4)
#     driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
#     time.sleep(30)
#     driver.close()

# def test_upload():
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.foundit.in/")
#     time.sleep(4)
#     driver.find_element(By.XPATH, "//*[@id='heroSection-container']/div[3]/div[2]/div[2]" ).click()
#     driver.find_element(By.XPATH, "//*[@id='file-upload']").send_keys("C:\ECQNIO\Documents\manual testing ppt\manual chapter-10")
#     time.sleep(19)

def test_boostrap():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.save_screenshot("aaa.png")

    driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()
    time.sleep(5)
    cutlist = driver.find_elements(By.XPATH, "//*[@id='select2-billing_country-results']/li")
    print(len(cutlist))
    for country in cutlist:
        if country.text == "India":
            country.click()
            break

    time.sleep(10)
    driver.close()

from selenium.webdriver import Keys
def test_windowtab():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    driver.implicitly_wait(10)
    regdtn=Keys.CONTROL+Keys.ENTER
    driver.find_element(By.LINK_TEXT, "Register").send_keys(regdtn)
    time.sleep(5)
    driver.close()

def test_newtab():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.switch_to.new_window("tab")
    driver.get("https://www.facebook.com/")
    time.sleep(6)

def test_Headless():
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(options=ops)
    driver.get("https://www.facebook.com/")
    driver.switch_to.new_window("window")
    driver.get("https://www.facebook.com/")
    time.sleep(6)

def test_datahanding():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[@id='principal']").send_keys("10000")
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys("12")
    set=Select(driver.find_element(By.XPATH, '//*[@id="tenurePeriod"]'))
    set.select_by_visible_text("month(s)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys('10')
    tim=Select(driver.find_element(By.XPATH, '//*[@id="frequency"]'))
    tim.select_by_visible_text("Compounded Monthly")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]').click()
    time.sleep(20)
    driver.close()


