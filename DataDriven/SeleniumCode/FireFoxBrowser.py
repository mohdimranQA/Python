from selenium import webdriver

# Optional: specify the path to geckodriver if it's not in PATH
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# Launch Firefox browser
driver = webdriver.Firefox()

# Open a website
driver.get("https://www.google.com")

# Optional: Perform actions on the page (e.g., search)
# search_box = driver.find_element("name", "q")
# search_box.send_keys("Selenium with Python")

# Keep the browser open for 5 seconds
import time
time.sleep(5)

# Close the browser
driver.quit()
