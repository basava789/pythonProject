from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC

def abhi():
    with open("raju.csv", mode="r")as file:
        date=csv.reader(file)
        date1=[]
        for line in date:
            date1.append(line)
        return date1
list=abhi()
print(list)

@pytest.mark.parametrize('user_name,password', list)
def test_login(user_name, password):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.skillshoppy.com/account/login")
    time.sleep(4)
    driver.find_element(By.NAME, "phps_usern").send_keys(user_name)
    driver.find_element(By.NAME, "phps_passwd").send_keys(password)
    time.sleep(3)
    driver.find_element(By.NAME, 'phps_login').click()
    try:
        mes=driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div")
        print("error12=", mes.text)
    except Exception as a:
        print("error=", a)
    try:
       mes1= driver.find_element(By.XPATH, "//*[text()='Your password must be at least 6 characters']")
       print(mes1.text)
    except Exception as e:
         print("error 1 =", e)
    link=driver.find_elements(By.TAG_NAME, "a")
    print("Total num of links is :-",len(link))
    for links in link:
        print(links.text,"=",links.get_attribute('href'))
    time.sleep(4)
    driver.close()