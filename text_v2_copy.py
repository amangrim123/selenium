from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from selenium import webdriver
executor = ThreadPoolExecutor(1000)
n=1
def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)
def scraper(url):
    options = Options()

    options.headless = True

    driver_path ="/usr/bin/chromedriver"

    s = Service(driver_path)

    driver = webdriver.Chrome(options=options,service=s)

    driver.get(url)
    n=n+1
    print(n)
    print(driver.title)
    driver.quit()

loop = asyncio.get_event_loop()
for url in ["https://www.google.com/search?q=godaddy"] * 120000:
    scrape(url, loop=loop)
loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))