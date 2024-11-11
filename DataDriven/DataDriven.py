import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import XLUtils
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
path="/home/imran/Documents/Python/DataDriven/TestData.xlsx"

rows = XLUtils.getRowsCount(path,"Sheet1")
for r in range(1,rows+1):
        username = XLUtils.readData(path,"Sheet1", r, 1)
        password = XLUtils.readData(path,"Sheet1", r, 2)

        driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']").send_keys(username)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys(password)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        time.sleep(3)
        if driver.title==driver.title:
            print("Log is success")
            XLUtils.writeData(path,"Sheet1",r,3,"Pass")
        else:
            print("login is failed")
            XLUtils.writeData(path, "Sheet1", r, 3, "Failed")
