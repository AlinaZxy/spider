from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import platform
import time
import os
import re
from lxml import etree


chrome_driver_path = ""
driver = None
main_page_url='https://piyao.sina.cn/'
headers={'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

if platform.system()=='Windows':
    chrome_driver_path = "chromedriver.exe"
elif platform.system()=='Linux' or platform.system()=='Darwin':
    chrome_driver_path = "./chromedriver"
else:
    print('Unknown System Type. quit...')

requests.headers = headers
chrome_options = Options()

chrome_options.add_argument('--disable-gou')
driver = webdriver.Chrome(chrome_options=chrome_options,
                                executable_path=chrome_driver_path)


driver.get(main_page_url)
time.sleep(1)


dates=driver.find_elements_by_xpath('//div[@class="day_date"]')
for date in dates:
    print(date.text)
    titles=driver.find_elements_by_xpath('//div[@class="left_title"]')
    nums=driver.find_elements_by_xpath('//div[@class="comment_text"]')
    for t in titles:
        print(t.text)
    for i in nums:
        print(i.text)


quit()