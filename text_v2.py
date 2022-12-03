from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


start_time = time.time()
options = Options()

options.headless = True

driver_path ="/usr/bin/chromedriver"

s = Service(driver_path)

driver = webdriver.Chrome(options=options,service=s)

driver.get("https://google.com/")
print(driver.title)
driver.quit()


from selenium import webdriver
from concurrent import futures


def selenium_title(url):
    options = Options()

    options.headless = True

    driver_path ="/usr/bin/chromedriver"

    s = Service(driver_path)

    driver = webdriver.Chrome(options=options,service=s)

    driver.get(url)
    print(driver.title)
    time.sleep(60)
    driver.quit()


links = ["https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/","https://google.com/"]
with futures.ThreadPoolExecutor() as executor: # default/optimized number of threads
  titles = list(executor.map(selenium_title, links))

print(len(links))

duration = time.time() - start_time

print("time - " ,duration)