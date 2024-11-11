import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import XLUtils
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://www.careers360.com/user/register?destination=https://www.careers360.com/?&click_location=header")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
time.sleep(5)
path="/home/imran/Documents/Python/DataDriven/TestData.xlsx"
time.sleep(5)
rows = XLUtils.getRowsCount(path,"Sheet1")
