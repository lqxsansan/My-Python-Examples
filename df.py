# -*- coding: utf-8 -*-

import requests
import sys
import tkMessageBox


# detect argv-----------

if not len(sys.argv) == 3:
	print '''Argv Error!
			Usage: df.py -Department -roomnumber'''
	exit(0)
else:
	pass

dep = sys.argv[1]
room = sys.argv[2]

# get values

url = r'http://www.hugongda.com:8888/api/v1/get/power/' +str(dep) + '/' + str(room)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url,headers = headers)

dict = eval(response.text)

result = "剩余电量： %s 剩余电费： %s" % ( dict['oddl'], dict['prize'] )
tkMessageBox.showinfo('Result',result)
exit(0)
