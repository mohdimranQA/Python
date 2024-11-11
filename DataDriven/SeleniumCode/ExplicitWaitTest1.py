from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://www.careers360.com")
driver.maximize_window()

wait = WebDriverWait(driver,10)
wait.until()
driver.find_element(By.CSS_SELECTOR,".searchBox").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Colleges, Exams, Schools & more']").send_keys("IIT Delhi")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Colleges, Exams, Schools & more']").send_keys("IIT Delhi")



sleep(2)