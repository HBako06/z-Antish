import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credenciales = r'G:\.Programacion\Pyhton\CromiunEdge Test\FormulasPremiun.xlsx'

df = pandas.read_excel(excel_credenciales)

#tarjeta = str(df['tarjetas'][0])
#clave = str(df['nacimiento'][0])
#clave2= df['DiaAnyo'][0]
#clave3= df['DiaMes'][0]
#clave4= df['MesDia'][0]

url = 'https://www.bbva.pe/personas/olvido-contrasena.html'

#Testeo Del Excel
#url= 'https://www.google.com/'
#buscador= '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'


boton_tarjeta= '/html/body/div[1]/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/input'
boton_clave= '/html/body/div[1]/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/input'
boton_captcha= '/html/body/div[1]/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[4]/div/div/input'
boton_siguiente= '/html/body/div[1]/div/div/div/div/div/form/article/div[3]/button[2]'

#Abriendo el navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(url)
time.sleep(2)

for i in df.index:
	tarjetas = str(df['tarjetas'][i])
	#Ingresando tarjeta
	driver.find_element_by_xpath(boton_tarjeta).send_keys(tarjeta)
	time.sleep(5)

#cerrar ventana
driver.quit()




#Abriendo google
#driver.find_element_by_xpath(buscador).send_keys(tarjeta)
#time.sleep(5)

"""
#Ingresando tarjeta
driver.find_element_by_xpath(boton_tarjeta).send_keys(tarjeta)
time.sleep(2)


#Ingresando Clave
driver.find_element_by_xpath(boton_clave).send_keys(clave)

#Leyendo captcha
driver.find_element_by_xpath(boton_captcha).click()
time.sleep(10)

#boton final aceptar
driver.find_element_by_xpath(boton_siguiente).click()
time.sleep(12)
"""


