import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = "chromedriver.exe")

	def test_buscar(self):
		driver = self.driver
		#driver.maximize_window()
		#driver.implicitly_wait(20)
		driver.get("https://www.bbva.pe/personas/afiliacion.html")
		#print(dir(driver))
		#self.assertIn("Google",driver.title)
		time.sleep(2)
		print("buscando")
		element = driver.find_elements_by_ID("numeroTarjeta")
		element.send_keys("selenium")
		element.send_keys(Keys.RETURN)
		time.sleep(4)

		assert "NOstaa: " not in driver.page_source

	def tearDown(self):
		self.driver.close()
		print("naiu")

if __name__ == '__main__':
	unittest.main()