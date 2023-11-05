import  unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

import pandas
from selenium.webdriver.support import expected_conditions as ec
import selenium.webdriver.support.ui as ui

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "geckodriver.exe")

	def test_Cuerpo(self):
		driver = self.driver 
		wait = ui.WebDriverWait(driver,10)
		driver.get('https://www.bbva.pe/personas/afiliacion.html')
		#time.sleep(2)
		tarje = '4010343434'
		#test
		xpath_tarjeta = '/html/body/div/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/input'
		
		#driver.find_element(By.XPATH ,xpath_tarjeta).clear()  #limpiear todo

		driver.find_element(By.XPATH,xpath_tarjeta).send_keys(tarje.rstrip()) # Poniendo el usuario
		print(tarje)

		#login = driver.find_elements_by_id("numeroTarjeta")
		#elements = driver.find_elements(By.XPATH, "//*[@id='numeroTarjeta']")

		'''
		for i in range(1000):
			try:
				login[i].send_keys(str("34343"))
				print("------------------------------------------")

			except Exception as e: 
				#time.sleep(1)
				print(str(i) +"otr int")

		'''
			

		
		#login = clear()
		#login.send_keys('Sisu')
		#driver.find_element_by_xpath("//*[@id='numeroTarjeta']")

		#BuscarXpath_Tarjeta = driver.find_elements(By.XPATH, "//*[@id='numeroTarjeta']")
		time.sleep(2)
		#element.send_keys('1')
		#BuscarXpath_Tarjeta.send_keys(Keys.RETURN)
		#print ('\a')
		print("Si pasó")
		time.sleep(4)

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
	unittest.main()