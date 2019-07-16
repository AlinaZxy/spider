from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import platform
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

for i in range(7):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    time.sleep(2)

d=[]
ti=[]
com=[]

dates=driver.find_elements_by_xpath('//div[@class="day_date"]')
for i,date in enumerate(dates):
    titles=driver.find_elements_by_xpath('//div[@class="zy_day" and position()= %d]/div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]'%(i+1))
    nums=driver.find_elements_by_xpath('//div[@class="zy_day" and position()= %d]/div[@class="day_date"]/following-sibling::ul//div[@class="comment_text"]'%(i+1))
    for t in titles:
        d.append(date.text)
        ti.append(t.text)
        #print(date.text,t.text)
    for i in nums:
        com.append(i.text)
        #print(i.text)

coms = [int(x)for x in com]

list = zip(d,ti,coms)
newlist = sorted(list, key=lambda x : x[2])
# print("按照谣言评论数排序：")
# for i in newlist:
#     print(i)
print("捉谣记十大谣言：")
for x in newlist[-1:-11:-1]:
    print("日期：",x[0],'\t',"事件:",x[1],'\t',"评论数:",x[2],'\t')
quit()