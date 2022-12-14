from genericpath import isdir
from socket import timeout
from selenium import webdriver
import time
import re
import sys
import requests
import json
import base64
import time
import asyncio
import shutil
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
# from fake_headers import Headers
from os import listdir
from os.path import isfile, join
from sys import exit
from bs4 import BeautifulSoup
import codecs
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import mysql.connector

def remove_non_ascii_1(data):
    return ''.join([i if ord(i) < 128 else ' ' for i in data])


def check_exists_by_xpath(xpath):
    try:
        #driver.find_element_by_xpath(xpath)
        driver.find_element(by=By.XPATH, value=xpath)
    except:
        return False
    return True


def process_soup(soup):
    for tag in soup.findAll():
        if(tag.name=="img"):
            tag.decompose()
    #     if(tag.name=="a" and tag.has_attr('href')):
    #         value_list.append(str(tag))           
    #         key_list.append(tag.text)
    # out_tag.clear()
    # for key, value in zip(key_list, value_list):
    #     out_tag[key] = value
        # if(tag.name=="img"):
        #     tag.decompose()
        # if(tag.name=="a" and tag.has_attr('href')):
        #     if('twitter' in tag['href'] or 'instagram' in tag['href'] or 't.co' in tag['href']):
        #         continue
        #     tag.parent.a.unwrap()
        # if(tag.name=='li'):
        #     if(len(tag.findChildren('a'))>0):
        #         tag.decompose()
    p=soup.findAll()
    newtext=[None]*len(p)
    i=-1
    for tag in p:
        i+=1
        if(tag.name=='p'):
            if(tag.findParent().name=='blockquote'):
                continue
            if(len(tag.findChildren('p'))>0):
                continue
            if(tag.text=='' or tag.get_text(strip=True)==''):
                continue
            #newtext=newtext + tag.text + "\n\n\n"
            #newtext[i]=tag.find(text=True, recursive=False)
            newtext[i]=tag.get_text(strip=True)
        
    #list=[str(newtext.index(x))+"."+x for x in newtext if x is not None and x is not '']
    list=[x for x in newtext if x != None and x != '']
    print("quilling p count:",len(list))
    str1=""
    for ele in list: 
        str1 += ele + "\n\n\n"
    print("word count:-",len(str1.split()))
    return str1 

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

    time.sleep(4)           


if __name__ == "__main__":

    ############## DataBase #####################

    mydb = mysql.connector.connect (
            host="64.227.176.243",
            user="phpmyadmin",
            password="Possibilities123.@",
            database="aman"
        )


    # Initialize connection pool
    # conn = aiohttp.TCPConnector(limit_per_host=100, limit=0, ttl_dns_cache=300)
    PARALLEL_REQUESTS = 100
    results = []

    start_time = time.time()


    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM destination_website where status = 1 ")
    myresult = mycursor.fetchall()

    listt=[]
    for des_id in myresult:
        listt.append(des_id[0])
    # print(listt)
    bfw_li=[]
    for des in listt:
        mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (des))
        websites = mycursor.fetchall()
        bfw_li.extend(websites)

    alll=[]
    for bfw_idd in bfw_li:
        mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status is Null " % (bfw_idd[0]) )
        webs = mycursor.fetchall()
        alll.extend(webs)


    containt_list = []
    print(mycursor.rowcount, "record fetched.")
    for x in alll:
        
        newdata=remove_non_ascii_1(x[4] + str(x[0]))
        soup = BeautifulSoup(newdata, 'html.parser')
        
        #soup.find_all('p')[-1].decompose()
        ### <figure> Tags

        str1=process_soup(soup)
        containt_list.append(str1 + str(x[0]))   

    driver_path="/usr/bin/chromedriver"
#sitepath="D:\\work\\python\\webscrape\\"
    # header = Headers(     comment
    # driver_path=r'/usr/bin/chromedriver'
    # driver_path=r'/home/ubuntu/chromedriver'
#sitepath="D:\\work\\python\\webscrape\\"
    # header = Headers(             ++++++++++++++++++++++++++++comment 
    #     browser="chrome",  # Generate only Chrome UA
    #     os="win",  # Generate only Windows platform
    #     headers=False # generate misc headers
    # )
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
    #driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    s = Service(driver_path)
    options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s)
    # driver = webdriver.Chrome(options=chrome_options, executable_path = driver_path)

    quill_login(driver)

    async def gather_with_concurrency():

        async def geta(url,driver):
            all_words = url.split()
            first_word= all_words[-1]
            print(first_word)
            driver.execute_script(f'''window.open('https://quillbot.com/','{first_word}');''')
            await asyncio.sleep(3)

            driver.switch_to.window(f"{first_word}")
            # time.sleep(1.5)
            # try:
            #     driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[1]/button').click()
            # except:
            #     pass 
            driver.find_element(By.XPATH,'//*[@id="inputText"]').clear()
            # time.sleep(1.5)
            # try:
            #     driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[1]/button').click()
            # except:
            #     pass 
            driver.find_element(By.XPATH,'//*[@id="inputText"]').send_keys(url)
            # time.sleep(1.5)
            # try:
            #     driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[1]/button').click()
            # except:
            #     pass 
            
            driver.find_element(By.XPATH,'//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button').click()
            # time.sleep(1.5)
            # try:
            #     driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[1]/button').click()
            # except:
            #     pass 
            delay = 30
            await asyncio.sleep(2)
            myElem = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button/div[text()="Rephrase"]')))
            if myElem:
                print("yes")
            #     quil_content = driver.find_element(By.XPATH,'//*[@id="editable-content-within-article"]')
            #     quil_file = open("results"+str(first_word)+".csv",'w')
            #     quil_file.write(quil_content.text)
            #     time.sleep(3)
            # await asyncio.sleep(2)    

        await asyncio.gather(*(geta(url,driver) for url in containt_list))

        for ee in containt_list:
            all_words = ee.split()
            first_word= all_words[-1]
            driver.switch_to.window(f"{first_word}")
            quil_content = driver.find_element(By.XPATH,'//*[@id="editable-content-within-article"]')
            quil_file = open(r"/results"+str(first_word)+".csv",'w')
            quil_file.write(quil_content.text)

        time.sleep(12)
        driver.quit()

    # asyncio.run(gather_with_concurrency())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_with_concurrency())
    # conn.close()

    duration = time.time() - start_time

    print(f"Completed {len(containt_list)} requests with {len(results)} results")

    print(f"finish within = {duration} seconds" )

