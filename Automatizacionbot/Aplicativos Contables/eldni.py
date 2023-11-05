from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os #Borrar consola


driver = webdriver.Chrome(executable_path="chromedriver.exe")
#No estoy logeado
driver.get("https://eldni.com/pe/buscar-por-nombres")

#Nombre del excel
filesheet = "./NombresAplicativos.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name('Hoja1')
wb.close()
#archivo = open("archivo.txt","a")

#Variables
nombre_xpath = "//*[@id='nombres']"
apellPP_xpath = "//*[@id='apellido_p']"
appllMM_xpath = "//*[@id='apellido_m']"
buscarDNI_xpath = "//*[@id='buscar-por-nombres']/div[4]/button"
tabla_xpath = "//*[@id='column-center']/div[1]/table/tbody/tr[1]"

#RangoFinal = int(input("Cantidad: : "))
os.system("cls")
for i in range(1,23):
	nomb, nomb2 , apellP, apellM = nombres[f'A{i}:D{i}'][0]
	print("********************************************************************")
	print(nomb.value,nomb2.value, apellP.value, apellM.value)
	
	WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,nombre_xpath)))

	nombresito = driver.find_element(By.XPATH, nombre_xpath)
	nombresito.clear()
	nombresito.send_keys(nomb.value)
	try:
		#driver.find_element_by_id("nombres").send_keys(" ")
		#driver.find_element_by_id("nombres").send_keys(nomb2.value)
		nombresito.send_keys(" ")
		nombresito.send_keys(nomb2.value)
	except Exception as e:
		print("ssn.")

	apellidoP = driver.find_element(By.XPATH, apellPP_xpath )
	apellidoP.clear()
	apellidoP.send_keys(apellP.value)

	apellidoM = driver.find_element(By.XPATH, appllMM_xpath ) 
	apellidoM.clear()
	apellidoM.send_keys(apellM.value)

	driver.find_element(By.XPATH, buscarDNI_xpath).click() #dar click en buscar

	try:
		element = WebDriverWait(driver,15).until(
			EC.presence_of_element_located((By.XPATH,tabla_xpath))
			)
		denei = driver.find_element(By.XPATH, tabla_xpath).text
		if denei == "":
			archivo = open("archivo.txt","a")
			archivo.write("Sin DNI\n")
			archivo.close()
			print("No se encontró DNI ")
		else: 
			archivo = open("archivo.txt","a")
			print("DNI: "+ denei)
			archivo.write(denei)
			archivo.write("\n")
			archivo.close()
			print('---------')
			#time.sleep(0.5)

	except Exception as e:
		archivo = open("archivo.txt","a")
		archivo.write("Sin DNI\n")
		archivo.close()
		print("No se encontró DNI ")
	print("********************************************************************")

print("Terminó")
time.sleep(5)




