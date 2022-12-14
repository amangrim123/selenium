from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
from socket import timeout
from selenium import webdriver
from concurrent.futures.thread import ThreadPoolExecutor
import time
import json
import asyncio
import re
import multiprocessing
import threading
import time
import re
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
from selenium.webdriver.chrome.service import Service

def remove_non_ascii_1(data):
    return ''.join([i if ord(i) < 128 else ' ' for i in data])

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

def all_process(containt,db):

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
        time.sleep(3)
        password = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[4]/div/div/input")
        password.clear()
        password.send_keys(quill_pwd)
        #driver.find_element_by_xpath("//*[@id='loginContainer']/div/div[6]/button").click()
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[5]/button").click()
        #time.sleep(5)
        status = check_exists_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button',driver)
        if(status):
            #element=driver.find_element_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button')
            element=driver.find_element(by=By.XPATH, value='//div[contains(@class,"MuiDialogContent-root")]/button')
            print(status)
            driver.execute_script("arguments[0].click();", element) 

        time.sleep(4)


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
    driver_path ="/usr/bin/chromedriver"
    s = Service(driver_path)
    options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s,options=chrome_options) 
    # driver = webdriver.Chrome(executable_path = 'chromedriver.exe')   

    quill_login(driver)

    async def gather_with_concurrency():

        def remove_non_ascii_2(data):
            return ''.join([i if ord(i) < 128 else ' ' for i in data])


        # async def check_exists_by_xpath(xpath,driver):
        #     try:
        #         #driver.find_element_by_xpath(xpath)
        #         driver.find_element(by=By.XPATH, value=xpath)
        #     except:
        #         return False
        #     return True

        # async def find_replacement(m):
        #     return out_tagaaa[m.group(1)]

        async def geta(acontaint,driver):
            all_words = acontaint.split()
            first_word= all_words[-1]
            print(first_word)
            acontaint = acontaint.replace(first_word,' ')
            driver.execute_script(f'''window.open('https://quillbot.com/','{first_word}');''')
            await asyncio.sleep(5)

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
            driver.find_element(By.XPATH,'//*[@id="inputText"]').send_keys(acontaint)
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
            await asyncio.sleep(5)
            myElem = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button/div[text()="Rephrase"]')))
            if myElem:
                print("yes")
            #     quil_content = driver.find_element(By.XPATH,'//*[@id="editable-content-within-article"]')
            #     quil_file = open("results"+str(first_word)+".csv",'w')
            #     quil_file.write(quil_content.text)
            #     time.sleep(3)
            # await asyncio.sleep(2)    

        await asyncio.gather(*(geta(url,driver) for url in containt))
        mycursor2 = db.cursor()
        for ee in containt:
            all_words = ee.split()
            first_word= all_words[-1]
            driver.switch_to.window(f"{first_word}")
            quil_content = driver.find_element(By.XPATH,'//*[@id="editable-content-within-article"]').text

            mycursor2.execute(f"SELECT content FROM bulk_feed_content where bfc_id={first_word} and status is Null")
            
            webs = mycursor2.fetchall()
            # print("containt = ",webs[0])
            newdata1=remove_non_ascii_2(webs[0][0])
            # print("news = ",newdata1)
            soup1 = BeautifulSoup(newdata1, 'html.parser')
            quilled_text=quil_content.split('\n\n\n')
            # print("quilled p count:",len(quilled_text))
            # print("quilled_text   ===",quilled_text)
            # print(type(quilled_text))
            #print("p count:",len(soup.find_all('p',recursive=False)))
            #for x in quilled_text:
            #    i=int(x.split(".",1)[0])
            #    p[i].string=x.split(".",1)[1]
            out_tagaaa = {}
            key_list=[]
            value_list=[]
            p=soup1.findAll()
            # print(p)
            # jq +=1
            for tag in p:
                if(tag.name=="a" and tag.has_attr('href')):
                    value_list.append(str(tag))           
                    key_list.append(tag.text)
            out_tagaaa.clear()
            for key, value in zip(key_list, value_list):
                if key=="":
                    continue
                else:
                    out_tagaaa[key] = value
            # print(out_tagaaa)
            ia=-1
            ja=0
            flag=1
            for tag in p:
                ia+=1
                if(tag.name=='p'):
                    if(tag.findParent().name=='blockquote'):
                        continue
                    if(len(tag.findChildren('p'))>0):
                        continue
                    if(tag.text=='' or tag.get_text(strip=True)==''):
                        continue
                    #newtext=newtext + tag.text + "\n\n\n"
                    #newtext[i]=tag.find(text=True, recursive=False)
                    try:
                        p[ia].string=quilled_text[ja]
                        ja+=1
                        
                        
                    except IndexError:
                        mycursor2.execute("update bulk_feed_content set content_modify=%s,status=0 where bfc_id=%s", (str(soup1),first_word))
                        db.commit()
                        print("exception")
                        flag=0
                        break

            #f = open(spinned,"w",encoding='utf-8')
            #with codecs.open(spinned, 'w',encoding="utf-8") as f:
            #f.write(str(soup)) 
            # print("soup   ===",str(soup))
            print("The End")
            # regex = r'({})'.format(r'|'.join(re.escape(w) for w in out_tagaaa))
            # rt = re.sub(regex, find_replacement,(str(soup1))) 
            # res = str(rt)[1:-1]
            # print("resss   ===",str(res))
            if flag==1:
                mycursor2.execute("update bulk_feed_content set content_modify=%s,status=1 where bfc_id=%s", (str(soup1),first_word))
                db.commit()
                print(f"Updata quil data in {first_word}")
            driver.quit()
            # quil_file = open(r"a/results"+str(first_word)+".csv",'w')
            # quil_file.write(quil_content.text)



        time.sleep(12)
    driver.quit()

    # asyncio.run(gather_with_concurrency())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_with_concurrency())
    # conn.close()        


if __name__ == "__main__":

    ############## DataBase #####################

    mydb = mysql.connector.connect (
            host="64.227.176.243",
            user="phpmyadmin",
            password="Possibilities123.@",
            database="aman"
        )


    # Initialize connection pool
    conn = aiohttp.TCPConnector(limit_per_host=100, limit=0, ttl_dns_cache=300)
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

    without_quil_containt = []
    containt_list = []
    large_containt_list =[]
    print(mycursor.rowcount, "record fetched.")
    for x in alll:
        newdata=remove_non_ascii_1(x[4] + str(x[0]))
        soup = BeautifulSoup(newdata, 'html.parser')
        
        
        #soup.find_all('p')[-1].decompose()
        ### <figure> Tags
        
        
        str1=process_soup(soup)
        if (len(str1.split())) < 1000 :            
            containt_list.append(str1 + str(x[0]))
        # else:
        #     large_containt_list.append(str1 + str(x[0]))

    # all_process(containt_list)

    a12 = len(containt_list)/4
    b12 = len(containt_list)%4

    large_a12 = len(large_containt_list)/2
    large_b12 = len(large_containt_list)%2


    if  b12 != 0:
        c12 = a12 + 1
    else:
        c12 = a12

    if  large_b12 != 0:
        large_c12 = large_a12 + 1
    else:
        large_c12 = large_a12    

    # pool = multiprocessing.Pool()

    for i12 in range(int(c12)):
        start_google = (i12*4)
        end_google = (i12+1)*4
        print(start_google ,"==",end_google)
        i12 = threading.Thread(target=all_process,args=(containt_list[start_google:end_google],mydb,)).start()
        time.sleep(3)

    ###################### For large Containt #############################
    # for ii12 in range(int(large_c12)):
    #     start_index = (ii12*2)
    #     end_index = (ii12+1)*2
    #     print(start_google ,"==",end_google)
    #     ii12 = multiprocessing.Process(target=all_process,args=(large_containt_list[start_index:end_index],)).start()
    #     time.sleep(1)    

    # pool.close()    
    # p3.join()
    # p4.join()

    # executor = ThreadPoolExecutor(10)
    # def scrape(url, *, loop):
    #     loop.run_in_executor(executor, all_process, url)
    # loop = asyncio.get_event_loop()

    # for url in range(3):
    #     scrape(containt_list, loop=loop)
    # loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
 

    duration = time.time() - start_time

    print(f"Completed {len(containt_list)} requests with {len(results)} results")

    print(f"finish within = {duration} seconds" )

