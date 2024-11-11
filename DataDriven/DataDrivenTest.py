import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import XLUtils

options= Options()
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(5)
path="/home/imran/Documents/Python/DataDriven/TestData.xlsx"

rows = XLUtils.getRowsCount(path,'Sheet1')

for r in range(2,rows+1):
    username = XLUtils.readData(path,"Sheet1",r,1)
    Password = XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element(By.CSS_SELECTOR,"#username").send_keys(username)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys(Password)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#submit").click()
    time.sleep(3)

    if driver.title=="Logged In Successfully | Practice Test Automation":
        print("Login is Successfully")
        XLUtils.writeData(path,"Sheet1",r,3,"Test Passed")
    else:
        print("Login not Successfully")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")
