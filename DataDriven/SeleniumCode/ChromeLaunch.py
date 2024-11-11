# Launch Type 1
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# Launch Type 2
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
# print(driver.title)

# Launch Type 3
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")   # Run Chrome in headless mode
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
# print(driver.title)


# Launch Type 4  Launch Chrome remotely
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# grid_url = "http://your-selenium-grid-server/wd/hub"  # URL of the Selenium Grid or Remote WebDriver
# capabilities = DesiredCapabilities.CHROME   # Desired capabilities for Chrome
# driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)  # Launch Chrome remotely
# driver.get("https://www.google.com")


