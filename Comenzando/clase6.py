import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		#self.driver = webdriver.Chrome(executable_path = "chromedriver.exe")
		self.driver = webdriver.Firefox(executable_path = "geckodriver.exe")

	def test_buscar(self):
		driver = self.driver
		driver.get("http://www.google.com")
		self.assertIn("Google",driver.title)
		element = driver.find_element_by_name("q")
		element.send_keys("selenium")
		element.send_keys(Keys.RETURN)
		time.sleep(4)

		assert "NOstaa: " not in driver.page_source

	def tearDown(self):
		self.driver.close()
		print("naiu")

if __name__ == '__main__':
	unittest.main()