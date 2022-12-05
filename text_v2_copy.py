from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
from socket import timeout
from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.service import Service
import asyncio
import time
import aiohttp
import mysql.connector
from bs4 import BeautifulSoup
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from multiprocessing import Process

def remove_non_ascii_1(data):
    return ''.join([i if ord(i) < 128 else ' ' for i in data])


def check_exists_by_xpath(xpath,driver):
    try:
        #driver.find_element_by_xpath(xpath)
        driver.find_element(by=By.XPATH, value=xpath)
    except:
        return False
    return True

def quill_login(driver):
    wp_user = "gh1YcBHVrq"
    wp_pwd = "zd2eW0Aj6F"
    #driver.get("https://quillbot.com")
    driver.get("https://quillbot.com/login")
    quill_user = "rajan@grimbyte.com"
    quill_pwd = "Grimbyte123."
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[3]/div/div/input')))
        #print("Page is ready!")
    except TimeoutException:
        print("1Loading took too much time!")
    #username = driver.find_element_by_xpath("//*[@id='mui-3']")
    username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[3]/div/div/input")
    username.clear()
    username.send_keys(quill_user)
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[4]/div/div/input')))
        #print("Page is ready!")
    except TimeoutException:
        print("2Loading took too much time!")
    #password = driver.find_element_by_xpath("//*[@id='mui-4']")
    password = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[4]/div/div/input")
    password.clear()
    password.send_keys(quill_pwd)
    #driver.find_element_by_xpath("//*[@id='loginContainer']/div/div[6]/button").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[5]/button").click()
    #time.sleep(5)
    status = check_exists_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button')
    if(status):
        #element=driver.find_element_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button')
        element=driver.find_element(by=By.XPATH, value='//div[contains(@class,"MuiDialogContent-root")]/button')
        print(status)
        driver.execute_script("arguments[0].click();", element) 

    time.sleep(30)  
    print("done")
    driver.quit()         

chrome_options = Options()
chrome_options.add_argument("--user-agent={customUserAgent}")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')

driver_path ="/usr/bin/chromedriver"
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
s = Service(driver_path)
options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(options=chrome_options, executable_path = driver_path)

quill_login(driver)