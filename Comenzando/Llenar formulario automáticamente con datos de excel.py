from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time

driver = webdriver.Chrome(executable_path=r"G:\.Programacion\Pyhton\DriverChrome\chromedriver.exe")
driver.get("file:///G:/.Programacion/Pyhton/Comenzando/Pagina%20web%20HTML%20de%20prueba%20a%20.html")
time.sleep(3)

filesheet = "./ejemplo.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name('Hoja 1')
wb.close()

for i in range(1,5):
	nomb, apell, edad = nombres[f'A{i}:C{i}'][0]
	print(nomb.value, apell.value, edad.value)
	time.sleep(1)
	driver.find_element_by_id("nom").send_keys(nomb.value)
	time.sleep(1)
	driver.find_element_by_id("ape").send_keys(apell.value)
	time.sleep(1)
	driver.find_element_by_id("edad").send_keys(str(edad.value))
	time.sleep(1)
	driver.find_element_by_id("enviar").click()
	time.sleep(1)
	print('--- Datos enviados ---')

driver.close()