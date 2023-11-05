import  unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
driver.get('https://www.bbva.pe/personas/afiliacion.html')
#time.sleep(2)
tarje = '4010343434'
Siguiente_Xpath = "//*[@id='wizardNext']"
#test

#login = driver.find_elements_by_id("numeroTarjeta")


#elements = driver.find_elements("//*[@id,'numeroTarjeta']")
#elements = driver.find_elements_by_xpath('//*[contains(@id,"numeroTarjeta")]')
#elements = driver.find_element(By.XPATH, "//*[@id='numeroTarjeta']")

driver.implicitly_wait(15)
button = driver.find_element(By.ID, "numeroTarjeta")
#christmasTag = driver.find_element_by_id('numeroTarjeta')
button.click()


print("Busc.")
time.sleep(1)

#print(elements)


print("\nBuscFF")
#login = clear()
#login.send_keys('Sisu')
#driver.find_element_by_xpath("//*[@id='numeroTarjeta']")

#BuscarXpath_Tarjeta = driver.find_elements(By.XPATH, "//*[@id='numeroTarjeta']")
#time.sleep(2)
#element.send_keys('1')
#BuscarXpath_Tarjeta.send_keys(Keys.RETURN)
#print ('\a')
#print("Si pasó")
time.sleep(4)


