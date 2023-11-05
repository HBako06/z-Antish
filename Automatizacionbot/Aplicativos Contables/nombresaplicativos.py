from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path="chromedriver.exe")
#No estoy logeado
driver.get("https://app.aplicativoscontables.pe/login")

#Nombre del excel
filesheet = "./NombresAplicativos.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name('Hoja1')
wb.close()
archivo = open("archivo.txt","a")

# Logeandome en Applicativos
email = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div/form/div[1]/div[1]/div/input")
#Dni de la cuenta
email.send_keys(str("hoyosmires102@gmail.com"))
contrasena= driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div/form/div[1]/div[2]/div/input")
#Contraseña
contrasena.send_keys(str("camote159"))
contrasena.send_keys(Keys.ENTER)
time.sleep(6)
driver.get("https://app.aplicativoscontables.pe/aplicativos/dnipornombre")
nombre_xpath = "//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/div/input"
apellPP_xpath = ""
appllMM_xpath = ""

#RangoFinal = int(input("Cantidad: : "))

for i in range(1,6):
	nomb, nomb2 , apellP, apellM = nombres[f'B{i}:E{i}'][0]
	print(nomb.value,nomb2.value, apellP.value, apellM.value)
	#time.sleep(1)
	nombresito = driver.find_element_by_xpath(Nombre_xpath)
	nombresito.clear()
	nombresito.send_keys(nomb.value)
	try:
		nombresito.send_keys(" ")
		nombresito.send_keys(nomb2.value)
	except Exception as e:
		print("sin segundo nombre.")

	apellidoP = driver.find_element_by_xpath(apellPP_xpath)
	apellidoP.clear()
	apellidoP.send_keys(apellP.value)

	apellM = driver.find_element_by_xpath(appllMM_xpath)
	apellM.clear()
	apellM.send_keys(apellM.value)

	

		
	
	#time.sleep(1)
	'''
	driver.find_element_by_id("Apa").clear()
	driver.find_element_by_id("Apa").send_keys(apellP.value)
	#time.sleep(1)
	driver.find_element_by_id("Ama").clear()
	driver.find_element_by_id("Ama").send_keys(apellM.value)
	time.sleep(2)
	#boton final aceptar
	driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/app-search/div[3]/div/app-new/div/app-name/div/form/div[5]/button").click()
	time.sleep(7)
	#print('--- Datos enviados ---')
		'''
	print("a")


time.sleep(5)
print("Fin")



