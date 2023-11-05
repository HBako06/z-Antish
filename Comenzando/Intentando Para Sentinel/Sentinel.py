from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome(executable_path=r"G:\.Programacion\Pyhton\Comenzando\chromedriver.exe")
#No estoy logeado
driver.get("https://misentinel.sentinelperu.com/misentinelweb/dist/#/")

'''
#driver.get("https://misentinel.sentinelperu.com/MiSentinelWeb/dist/#/app/busqueda/nueva/nombre")
# Logeandome en Sentinel
usuario = driver.find_element_by_id("user")
#Dni de la cuenta
usuario.send_keys(str("76567823"))
contrasena= driver.find_element_by_id("password")
#Contraseña
contrasena.send_keys(str("C@mote159"))
contrasena.send_keys(Keys.ENTER)
time.sleep(6)
# Yendo a la busqueda de DNI :D
driver.find_element_by_xpath("/html/body/app-root/app-main-layout/app-menu-left/nav/ul/li[4]/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/app-root/app-main-layout/app-menu-left/nav/ul/li[4]/mat-accordion/mat-expansion-panel/div/div/li[1]/a/div").click()
driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/app-search/div[3]/div/app-new/ul/li[2]/p").click()
time.sleep(1)
'''

# llenando datos para sacar DNI
#Nombre del excel
filesheet = "./Sentineldnis.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name('Hoja1')
wb.close()
archivo = open("archivo.txt","a")
#archivo.write("Dnis \n")
try:
	#Rango de los Excels que se ejecutarán :D
	for i in range(1,422):
		nomb, apellP, apellM = nombres[f'A{i}:C{i}'][0]
		print(nomb.value, apellP.value, apellM.value)
		#time.sleep(1)
		driver.find_element_by_id("Nom").clear()
		driver.find_element_by_id("Nom").send_keys(nomb.value)
		#time.sleep(1)
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
		# falta su trycatch cuando no hay dnis 

		#imprimiedo datos
		try:
			denei = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/app-search/div[3]/div/app-new/div/app-name/div[2]/table/tbody/tr/td[3]").text
			print(denei)
			archivo.write(denei)
			archivo.write("\n")
			#usuariodeldni = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/app-search/div[3]/div/app-new/div/app-name/div[2]/table/tbody/tr[1]/td[4]").text
			print('----')
			time.sleep(1)
		except NoSuchElementException: #except NoSuchElementException: #except Exception as e:
			print("Sin DNI")
			archivo.write("Sin DNI\n")
			print('-----')
			time.sleep(1)
	print("a")
except Exception as e:
	print('----------')
	print('----------')
	print("Error en el programa")
print("Fin Del Programa!!!")
archivo.close()
time.sleep(5)



