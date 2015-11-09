# -*- coding: UTF-8 -*-
import json
import urllib2

response = urllib2.urlopen('http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=fe6767ec-9732-4bc9-b051-0990087c708d')
a=response.read().decode('utf_8')

#doc=json.load(response)

#print(type(a))

for i in a :
	if i=='[':
		b=a.index(i)
		break

a=a[b:len(a)-2:]
doc=json.loads(a)
for x in xrange(len(doc)):
	print doc[x]["address"]




