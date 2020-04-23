#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:47:10 2020

@author: akhil
"""

from urllib.request import urlopen as ureq
from urllib.request import Request as Req
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


url= 'https://www.lviglobal.com/course-schedule/'
req=Req(url, headers={'User-Agent': 'Chrome/80.0'})
x=ureq(req)
y=x.read()
x.close()
page_soup=soup(y,'html.parser')
y

a=page_soup.findAll('div',{'class':'event-desc'})
print(a[0].a['href'])
t=a[0].strings

for string in a[0].strings:
    print(string)

course_names=[]
for i in range(len(a)):
    for string in a[i].strings:
        if string not in course_names:
            course_names.append(string)
print(course_names)            

urls=[]
for i in range(len(a)):
    # print(a[i].a['href'])
    if(a[i].a['href']) not in urls:
        urls.append(a[i].a['href'])
#The following section of code that's been commented is a test run.
# driver=webdriver.Firefox()
# driver.get(url)
# driver.find_element_by_class_name('spu-icon spu-icon-close').click()
# driver.find_element_by_class_name('event-desc').click()
# req=Req(urls[1],headers={'User-Agent':'Chrome/80.0'}) 
# x=ureq(req)
# y=x.read()
# x.close()
# urls_soup=soup(y,'html.parser')
# urls_soup.h1.string 
# about=urls_soup.findAll('div',{'class':'wpb_wrapper'})
# len(about)

# about_actual=about[4].p.string
# about_list.append(about_actual)


# pricing=urls_soup.findAll('table',{'class':'table table-bordered'})
# table_contents=pricing[0].findAll('td')
# about_list=[]
# doc_tuition=[]
# team_tuition=[]
# CE_creds=[]
# AGD_Codes=[]
# campus=[]

# doc_tuition.append(table_contents[0].contents)
# team_tuition.append(table_contents[2].contents)
# CE_creds.append(table_contents[3].contents)    
# AGD_Codes.append(table_contents[4].contents)        
# campus.append(table_contents[5].contents)
about_list=[]
doc_tuition=[]
team_tuition=[]
CE_creds=[]
AGD_Codes=[]
campus=[]
c=0
for i in urls:
    req=Req(i,headers={'User-Agent':'Chrome/80.0'}) 
    x=ureq(req)
    y=x.read()
    x.close()
    urls_soup=soup(y,'html.parser')
    urls_soup.h1.string 
    about=urls_soup.findAll('div',{'class':'wpb_wrapper'})
    about_actual=about[4].p.string
    len(about)
    
    about_list.append(about_actual)
    if(c==0):
        pricing=urls_soup.findAll('table',{'class':'cInfo table table-bordered'})
       
    else:
        pricing=urls_soup.findAll('table',{'class':'table table-bordered'})
    
    table_contents=pricing[0].findAll('td')
    doc_tuition.append(table_contents[0].contents[1])
    team_tuition.append(table_contents[2].contents[1])
    CE_creds.append(table_contents[3].contents[1])    
    AGD_Codes.append(table_contents[4].contents)
    campus.append(table_contents[5].contents[1])
    c+=1
print(doc_tuition)
d_tuition=[]
for i in about_list:
    print(i)
    print('\n')
d={'Name':course_names
   ,'Doc-tuition':doc_tuition
   ,'Team-tuition':team_tuition
   ,'CE_creds':CE_creds
   ,'AGD_Codes':AGD_Codes
   ,'Campus/Duration':campus}
df=pd.DataFrame(d)    
df.to_csv('calendar.csv')

    
    
    
    
    
    
    
    
