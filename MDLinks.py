#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 02:34:50 2020

@author: akhil
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url='https://www.mdlinx.com/internal-medicine/conference.cfm'
driver=webdriver.Firefox()
driver.get(url)

# //*[@id="the_spec"]
specialities=driver.find_element_by_xpath('//*[@id="the_spec"]').text.lower().replace(' ','-').split('\n')
specialities_proc=[]
for i in specialities:
    x=i.replace('-&-','-').replace('/','-')
    specialities_proc.append(x)
del specialities_proc[0]
specialities_proc
# //*[@id="conf-summary"]/div[4]/div[1]/ul/li[2]/a
# //*[@id="conf-summary"]/div[4]/div[1]/ul/li[1]/a
# //*[@id="conf-summary"]/div[4]/div[1]/ul/li[6]/a
# x=driver.find_element_by_xpath(' //*[@id="conf-summary"]/div[4]/div[1]/ul/li[2]/a')
# x.click()
# email=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]/a').text
# website=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[6]/a').text
# location=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[4]').text
driver.back()

def check_exists_by_xpath(xpath):
    
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        # webdriver.Firefox().close()
        return False
    # webdriver.Firefox().close()
    return True

i=1
j=2
names=[]
dates=[]
emails=[]
websites=[]
locations=[]
while(True):
    if(check_exists_by_xpath('//*[@id="conf-summary"]/div[4]/div[1]/ul/li['+str(i)+']/a')):
        x=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[4]/div[1]/ul/li['+str(i)+']/a')
        x.click()
        if(check_exists_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[6]/a')):
            email=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]').text
            website=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[6]').text
            location=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[4]').text
            emails.append(email)
            websites.append(website)
            locations.append(location)
            driver.back()
        else:
            email=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[4]').text
            website=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]').text
            location=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[3]').text
            emails.append(email)
            websites.append(website)
            locations.append(location)
            driver.back()
                
        x=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[4]/div[1]/ul/li['+str(i)+']/a')
        date=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[4]/div[1]/ul/li['+str(i)+']/p')
        dates.append(date.text)
        names.append(x.text)
        i+=1
    else:
        i=1
        y=driver.find_element_by_link_text(str(j))
        y.click()
        while(True):
            if(check_exists_by_xpath('//*[@id="conf-summary"]/div[3]/div[1]/ul/li['+str(i)+']/a')):
    
                x=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[3]/div[1]/ul/li['+str(i)+']/a')
                names.append(x.text)
                date=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[3]/div[1]/ul/li['+str(i)+']/p')
                dates.append(date.text)
                x.click()
                
                if(check_exists_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[6]/a')):
                    email=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]').text
                    website=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[6]').text
                    location=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[4]').text
                    emails.append(email)
                    websites.append(website)
                    locations.append(location)
                    driver.back()
                else:
                    email=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[4]').text
                    website=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]').text
                    location=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[3]').text
                    emails.append(email)
                    websites.append(website)
                    locations.append(location)
                    driver.back()
                
                # x=driver.find_element_by_xpath('//*[@id="conf-summary"]/div[4]/div[1]/ul/li['+str(i)+']/a')
                
                i+=1
            else:
                j+=1
                y=driver.find_element_by_link_text(str(j))
                y.click()
                break
            
        
        
        continue
    # /html/body/div[2]/div/div[1]/div[1]/div[3]/p[3]
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[3]/p[5]').text
    # //*[@id="conf-summary"]/div[3]/div[1]/ul/li[2]/a
df=pd.DataFrame({'events':names,
                 'dates':dates,
                 'emails':emails,
                 'websites':websites,
                 'locations':locations
                 })
df.to_csv('MD_Links.csv')

        
        
        