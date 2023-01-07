
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_facebook():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")
    driver.maximize_window()
    actual_subtitle = driver.title
    expectedresult = "Log in to Facebook"
    assert actual_subtitle == expectedresult, " did not showing the log in page"
    print(driver.title)
    time.sleep(2)
    email = driver.find_element(By.ID, "email")
    email.send_keys("basava.raju949@gmail.com")

    password = driver.find_element(By.NAME, "pass")
    password.send_keys("basava@949")

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    time.sleep(5)

    # msg=driver.find_element(By.XPATH,"//*[@id='login-button']")
    # print("Error=", msg.text)

    time.sleep(6)
    driver.close()

def test_amazon():
    drive = webdriver.Chrome()
    drive.get("https://www.amazon.in")
    drive.maximize_window()
    print(drive.title)

    time.sleep(4)
    sing_btn = drive.find_element(By.XPATH, "//*[@id='nav-link-accountList']")
    sing_btn.click()
    time.sleep(3)
    email = drive.find_element(By.ID, "ap_email")
    email.send_keys("basava.raju949@gmail.com")
    continou_btn = drive.find_element(By.XPATH, "//*[@id='continue']")
    continou_btn.click()
    time.sleep(6)
    password = drive.find_element(By.ID, "ap_password")
    password.send_keys("Basava@949")
    time.sleep(2)
    sign_in = drive.find_element(By.XPATH, "//*[@id='signInSubmit']")
    sign_in.click()
    time.sleep(10)
    drive.close()

def test_instagram():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.instagram.com/')
    print(driver.title)
    time.sleep(4)
    email = driver.find_element(By.NAME, "username")
    email.send_keys("basava.raju949@gmail.com")
    time.sleep(2)
    password = driver.find_element(By.NAME, "password")
    password.send_keys("basava@949")
    time.sleep(2)
    login_btn = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
    login_btn.click()
    time.sleep(10)
    driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_flipkart():
    drive = webdriver.Chrome()
    drive.maximize_window()
    drive.get('https://www.flipkart.com/')
    actualresult= drive.title
    drive.implicitly_wait(5)
    expetedresult='Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best ' \
                  'Offers! '
    if actualresult==expetedresult:
        print("home page test pass")
    else:
        print("home page test failed")
    print(drive.title)
    time.sleep(5)
    drive.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(
        "7893420283")
    time.sleep(2)
    drive.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(
        "basava@949")
    time.sleep(5)
    try:
        elment= WebDriverWait(drive, 10).until(EC.presence_of_element_located( (By.XPATH,"/html/body/div["
                                                "2]/div/div/div/div/div[""2]/div/form/div[4]/button")))
        elment.click()
    except Exception as e:

        print("ty", e)
    time.sleep(10)
    drive.quit()

