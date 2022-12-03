from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()

options.headless = True

driver_path ="/usr/bin/chromedriver"

s = Service(driver_path)

driver = webdriver.Chrome(options=options,service=s)

driver.get("https://google.com/")
print(driver.title)
driver.quit()