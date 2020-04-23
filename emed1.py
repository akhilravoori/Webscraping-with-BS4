#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:32:15 2020

@author: akhil
"""

from urllib.request import urlopen as ureq
from urllib.request import Request as Req
from bs4 import BeautifulSoup as soup
import pandas as pd
id=input()

url='https://www.google.com/search?sxsrf=ACYBGNQZ3nlikyuMAvf9JoXBw7Q0wGeBLg:1574927301817&source=hp&ei=xXvfXdvcL-Hez7sPuuGogAw&q=usa+cme+conference+2020+january+list&oq=usa+cme+conference+&gs_l=psy-ab.3.0.35i39j0i8i7i30l4.2925.6988..8004...0.0..2.439.3183.4j9j2j1j2......0....1..gws-wiz.......0i7i30j0j0i13j0i8i7i10i30j0i13i30j35i304i39.pzo-PyL_rZk&ibp=htl;events&rciv=evn&sa=X&ved=2ahUKEwi60OO8tYzmAhXTH7cAHbKqB7wQ5rwDKAF6BAgPEAs#fpstate=tldetail&htivrt=events&htidocid=h1mbel3iArRTmD2CJpA8-A%3D%3D'
url2='https://www.jssuni.edu.in/JSSWeb/WebShowFromDB.aspx?MODE=SSMD&PID=10002&CID=5&DID=97&MID=0&SMID=10402'
req=Req(url2, headers={'User-Agent': 'Chrome/80.0'})
x= ureq(url2) 
page_html=x.read()
x.close()
page_html
page_soup=soup(page_html,"html.parser")
cont=page_soup.findAll('div',{'id':'faq-cat-'+'1'})
x=cont[0].find('div',{'class':'col-sm-9'})
x
x=[]
for i in range(1,8):
    cont=page_soup.findAll('div',{'id':'faq-cat-'+str(i)})
    x.append(cont[0].find('div',{'class':'col-sm-9'}))
name=[]
designation=[]
email_id=[]
qualification=[]
publications=[]
for i in range(len(x)):
    print(x[i])    
    print("\n")
y=x[0].strings
z=[]
for string in y:
    z.append(repr(string))
c=0    

y=[]
for i in range(len(x)):
    z=[]
    for string in x[i].strings:
        if(c%2==0):
            z.append(string)
        c+=1
    y.append(z)
    c=0
y    
d={'[Name':[],'Position':[],'Email':[],'Qualifications':[],'Publications':[]}
for i in range(len(y)):
    d['Name'].append(y[i][0])
    d['Position'].append(y[i][1])
    d['Email'].append(y[i][2])
    d['Qualifications'].append(y[i][3])
    d['Publications'].append(y[i][4])
d    
df=pd.DataFrame(d)  
df.to_csv("data.csv")

    