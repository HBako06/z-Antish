import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credenciales = r'G:\Programacion\Pyhton\Automatizacionbot\cuentastst.xlsx'

df = pandas.read_excel(excel_credenciales, sheet_name='HojaDeCanciones')

url = 'https://www.youtube.com'

#Xpath:

path_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input'
boton_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button'
path_cancion = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]'

#driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)

for i in df.index:
	cancion = str(df['cancion'][i])

	#Tipear la cancion:
	driver.find_element_by_xpath(path_busqueda).send_keys(cancion)
	driver.find_element_by_xpath(boton_busqueda).click()
	# Esperar que aparezcan las canciones:
	wait = WebDriverWait(driver,10)
	wait.until(ec.visibility_of_element_located((By.XPATH,path_cancion)))
	#entrar a la cancion
	driver.find_element_by_xpath(path_cancion).click()
	#disfrutar la cancion:
	time.sleep(6)
	#borrar la busqueda 
	driver.find_element_by_xpath(path_busqueda).clear()

driver.quit()
