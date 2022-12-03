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
    driver.quit()


links = ["https://www.amazon.com", "https://www.google.com","https://www.articulatesolution.com","https://www.flipkart.com", "https://www.yahoo.com", "https://www.godaddy.com"]
with futures.ThreadPoolExecutor() as executor: # default/optimized number of threads
  titles = list(executor.map(selenium_title, links))