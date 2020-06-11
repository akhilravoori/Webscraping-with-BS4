#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:11:13 2020

@author: akhil
"""
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen as ureq
from urllib.request import Request as Req
from bs4 import BeautifulSoup as soup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

url='https://ce.mayo.edu/courses/published?field_course_event_date_value%5Bmin%5D%5Bdate%5D=05%2F01%2F2020&field_course_event_date_value%5Bmax%5D%5Bdate%5D=12%2F31%2F2020&field_course_live_value%5B%5D=1&field_course_format_tid=All&field_region_value=All&field_custom_target_value=All&credits%5Bmin%5D=&credits%5Bmax%5D=&type=All'
driver=webdriver.Firefox()
driver.get(url)


# driver.find_element_by_xpath('//*[@id="footable"]/tbody/tr[1]/td[1]/a')
# c=1
# while(True):
#     try:
#         driver.find_element_by_xpath('//*[@id="footable"]/tbody/tr['+str(c)+']/td[1]/a')
#         c+=1
#     except NoSuchElementException :
#         break
names=[]
dates=[]

for n in range(4):
    for i in range(1,c):
        x=driver.find_element_by_xpath('//*[@id="footable"]/tbody/tr['+str(i)+']/td[1]/a')
        print(x.text)
        names.append(x.text)
        y=driver.find_element_by_xpath('//*[@id="footable"]/tbody/tr['+str(i)+']/td[5]/span')
        print(y.text)
        dates.append(y.text)
    next_page=driver.find_element_by_xpath('//*[@id="content-area"]/div/div[3]/ul/li[5]').find_element_by_tag_name("a").get_attribute('href') 
    driver.get(next_month)   
df=pd.DataFrame({'Events':names,'Dates-US format':dates})    
print(df)   
df.to_csv('Mayo.csv')
    
    
    