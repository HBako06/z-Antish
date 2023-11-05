from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


url = "https://www.watermarkremover.io/es/upload"



driver = webdriver.Firefox(executable_path = "geckodriver.exe")
driver.get(url)

os.system("cls")
print(Fore.GREEN)
print("   ──▄────▄▄▄▄▄▄▄────▄───")
print("   ─▀▀▄─▄█████████▄─▄▀▀──") 
print("   ─────██─▀███▀─██──────")
print("   ───▄─▀████▀████▀─▄────")
print("   ─▀█────██▀█▀██────█▀──\n\n")
print(Fore.CYAN)

