# -*- coding: UTF-8 -*-
import sys
import urllib2
import json
from bs4 import BeautifulSoup


response = urllib2.urlopen('http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=fe6767ec-9732-4bc9-b051-0990087c708d')  
html = response.read()
response.close


soup=BeautifulSoup(''.join(html))


print (soup)

