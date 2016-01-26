#coding=utf-8 
import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from pip._vendor.requests.packages.urllib3.util.connection import select
from jsonschema._validators import items
import shutil
from xml.dom import minidom
import urllib
import xml.etree.ElementTree as ET
import os
from urllib import urlretrieve
from bs4.builder._lxml import LXML
# import psycopg2

id = ["0CEBFACC0b00000180052923","0CEBFACC0b00000180052922","0CEBFACC0b00000180055827","0CEBFACC0b0000018011d769","0CEBFACC0b000001800bc4ba","0CEBFACC0b00000181dd8a29"]
# idarray = ["0CEBFACC0b00000180052922"]
url = "http://digimuse.nmns.edu.tw";
namelist=[]
for tempstr in id:
              # http://digimuse.nmns.edu.tw/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false&uid=1447321835121&id=0CEBFACC0b00000180052923
    url_str = url + "/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false" + tempstr
    xml_str = urllib.urlopen(url_str).read()
    xmldoc = minidom.parseString(xml_str)
    obs_values = xmldoc.getElementsByTagName('userdata')

    
    for obs_val in obs_values:
        urlb = url+obs_val.firstChild.data 
        print urlb
        res = requests.get(urlb)
        soup = BeautifulSoup(res.text,"lxml")
        for title in soup.select('#titleName'):  
#             if(title.text != ""):  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                print title.text
                
                x=title.text
                print x
                
                print type(title.text)
                
        for content in soup.select('#contenttext'):
#             print content.text
           
            try:
                   
#                 title =''
                title = content.find('title').text
#                 cont =''
                cont = content.text.replace(title,'')
                print cont.replace(title,'') 
#                 if(cont != "" or cont != "\n"):                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#                     print cont
                contOK= cont.replace(title,'')  
                print type(contOK)
            except: 
                print content.text
                contOK=content.text
                print type(contOK)
                
                
            for item in soup.select('img'):
                bfname = url+item['src']
                res2 ='000001'
                if bfname.find(res2)!=-1:
                    print bfname         
    
        # conn = psycopg2.connect(host='localhost',database='bigblack' ,user='postgres' ,password='viplab4719')
        # cur = conn.cursor()
    #     for x in xrange(len(namelist)):
#         print "INSERT INTO butterfuly_test (name,count) VALUES ('"+urlb+"', '8910');"
#         select_OK = ("INSERT INTO butterfuly_test6 (Url,Name,Count,imgurl) VALUES ('"+urlb+"','"+x+"','"+contOK+"','"+bfname+"');")
        # print cur.mogrify("INSERT INTO butterfuly_test6 (Url,Name,Count,imgurl) VALUES (%s,%s,%s,%s);",(urlb,x,contOK,bfname))
        # cur.execute("INSERT INTO butterfuly_test6 (Url,Name,Count,imgurl) VALUES (%s,%s,%s,%s);",(urlb,x,contOK,bfname))
        
#         cur.execute("INSERT INTO butterfuly_test6 (Url,Name,Count,Imgurl) VALUES ('"+urlb+"','"+x+"','"+cont_OK+"','"+bfname+"');")
#         cur.execute("INSERT INTO butterfuly_test (name,count) VALUES ('"+urlb+"','"+title.text+"', '"+cont.replace(title,'')+"' ,'"+fname+"');")
    # rows = cur.fetchall()
    #https://wiki.postgresql.org/wiki/Psycopg2_Tutorial 
    #
        # conn.commit()
    
        # cur.close()
        # conn.close()  
        