#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:21:13 2020

@author: akhil
"""


from urllib.request import urlopen as ureq
from urllib.request import Request as Req
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url='https://en.wikipedia.org/wiki/List_of_medical_schools_in_the_United_States' 
req=Req(url, headers={'User-Agent': 'Chrome/80.0'})
x=ureq(req)
y=x.read()
x.close()
page_soup=soup(y,'html.parser')
y
driver=webdriver.Firefox()
driver.get(url)
# x=driver.find_elements_by_tag_name('td')
# x=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td[2]')
# //*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td[7]
# # c=0
colleges=[]
wiki=[]

for i in range(1,159):
    try:
        x=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr['+str(i)+']/td[2]')
        c=driver.find_element_by_link_text(x.text)
        wiki.append(c.get_attribute('href'))
        colleges.append(x.text)
    except NoSuchElementException:
        colleges.append(x.text)
        wiki.append('')
        # collegelinks[i]=c.get_attribute('href')
        continue
    # c+=1
# if 'ca' in 'cat':
#     print('cat')
collegelinks=[]
for i in range(len(colleges)):
    try:
        if(len(wiki[i])>0) and ('wiki' in wiki[i]):
            driver.get(wiki[i])
            t=driver.find_element_by_xpath("//*[contains(text(), 'Website')]/following-sibling::td")
            print(t.find_element_by_tag_name("a").get_attribute('href'))
            collegelinks.append(t.find_element_by_tag_name("a").get_attribute('href'))
        else:
            collegelinks.append('')
            continue
    except NoSuchElementException:
        collegelinks.append('')
        continue
df=pd.DataFrame(
        {'collegenames':colleges,
         'wikilinks/some_are_mainlinks':wiki,
         'collegemainlinks':collegelinks
         }
     )           
df.to_csv('wikicolleges.csv')      


# t=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table')
# t=driver.find_elements_by_xpath("//*[contains(text(), 'Website')]/following-sibling::td")
# for i in t:
#     print(i.find_element_by_tag_name("a").get_attribute('href'))
# for i in t:
#     print(i.text)


# //*[@id="mw-content-text"]/div/table  
# /html/body/div[3]/div[3]/div[4]/div/table/tbody/tr[14]
# //*[@id="mw-content-text"]/div/table/tbody/tr[7]
# for i in x:
#     if len(i.text)>20 and len(i.text)<40 :
#         print(i.text)
        
# //*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td[2]
# a=page_soup.find('table',{'class':'wikitable sortable jquery-tablesorter'})
# a.strings
# c=0
# for i in a:
#     if c=1:
#         print(i)
        
# page_soup
    
