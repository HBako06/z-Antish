from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="./geckodriver.exe")

driver.get("https://teleton.pe/donaciones/")
#time.sleep(2)
input("Esperando...1")
#boton_tarjeta = "/html/body/div/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/input"

# Carpeta del excel:
#filesheet = "./datos.xlsx"
#wb = load_workbook(filesheet)
#hojas = wb.get_sheet_names()
#print(hojas)
#Datos = wb.get_sheet_by_name('Hoja1')
#wb.close()

#archivo = open("archivo.txt","a")
#archivo.write("Dnis \n")
#variables guardadas
#xpaTarjeta = "numeroTarjeta"


#driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/input').send_keys("3")

input("Esperando...2")


driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/div/input').click()

input("Esperando...3")


html body form#frmCC.form table tbody tr td input.short.req-numeric
.short

print("Fin Del Programa!!!")

# No acabado

