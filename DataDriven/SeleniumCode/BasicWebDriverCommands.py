from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import  By
options = Options()
driver = webdriver.Chrome(options=options)    # Launch the Browse
driver.get("https://www.careers360.com")  #   Open a URL
driver.maximize_window()
print(driver.current_url)   #  Get Current URL
driver.refresh()   # Page refresh
print(driver.title)    # page title
driver.find_element(By.CSS_SELECTOR,".login").click()
driver.back()   # Go back one page
driver.forward()  # Go forward one page