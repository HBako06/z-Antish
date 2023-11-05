from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

dni = "74214076"
url = "https://www.watermarkremover.io/es/upload"

id_Button= "UploadImage__HomePage"


driver = webdriver.Firefox(executable_path = "geckodriver.exe")
driver.get(url)

time.sleep(1)
#file = "D:\\.Programacion\\Pyhton\\Telegram\\pipipiBlackcc\\74214076.jpg"
file = "./dni.jpg"
time.sleep(1)
driver.find_element(By.ID,"UploadImage__HomePage").send_keys(os.path.join(os.getcwd(),file))

time.sleep(1)
input("pipi")
driver.close()


