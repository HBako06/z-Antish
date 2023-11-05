from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://www.bbva.pe/personas/olvido-contrasena.html")
time.sleep(2)

#boton_tarjeta = "/html/body/div/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/input"

# Carpeta del excel:
filesheet = "./datos.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
Datos = wb.get_sheet_by_name('Hoja1')
wb.close()

archivo = open("archivo.txt","w")
#archivo.write("Dnis \n")
#variables guardadas
xpaTarjeta = "numeroTarjeta"

# Solo para 1234
for i in range(1,6):
	tarjeta, contra = Datos[f'A{i}:B{i}'][0]

	print(tarjeta.value, contra.value)
	#Para el cuadrado de la tarjeta:
	time.sleep(1)
	#driver.find_element_by_xpath(boton_tarjeta).send_keys(tarjeta.value)
	
	driver.find_element_by_id("numeroTarjeta").send_keys(apellM.value)
	print("si pasoo")


print("Fin Del Programa!!!")
archivo.close()
driver.close()
time.sleep(5)
# No acabado

