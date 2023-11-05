from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.firefox.options import Options
from threading import Thread, Barrier

pathBotonIngresar = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/div[1]/index1/div/div/div/div[3]/div/a'
contador = 0

def func(threads):
    
    driver = webdriver.Firefox(executable_path = "geckodriver.exe")
    print("--------------------------------------------------")
    print(driver)
    driver.get(url)

    driver.find_element(By.ID,'nuDni').send_keys("12345678")
    driver.find_element(By.ID,'npass').send_keys("12345678")
    ingresar = driver.find_element(By.XPATH,pathBotonIngresar)

    #threads.wait()
    time.sleep(1)
    ingresar.click()

url='https://cel.reniec.gob.pe/celweb/index.html'

numero_multitareas = 4

barrier = Barrier(numero_multitareas)

threads = []

for _ in range(numero_multitareas):

    i = Thread(target=func, args=(barrier,))
    print("pausa 1")
    time.sleep(2)
    i.start()
    threads.append(i)
    print("pausa 2")
    time.sleep(2)
    print("pausa 3")
    time.sleep(2)

for i in threads:
    i.join()