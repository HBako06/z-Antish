
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import FirefoxProfile
from printy import printy

import time
import requests
import json


class BotInfoburo:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("http://infoburo.com.pe/Account/Login")
        wait0 = WebDriverWait(self.driver, 20)
        wait0.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="txt_User"]')))

        self.driver.find_element(By.XPATH, '//*[@id="txt_User"]').send_keys("VVENTO.STBK")
        self.driver.find_element(By.XPATH, '//*[@id="txt_Password"]').send_keys("Fernando@4567")
        self.driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()

    def ingresar(self):

        wait0 = WebDriverWait(self.driver, 20)
        #Esperar a que cargue la pagina para pasar de url
        wait0.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[1]/div[1]/a/span/span[2]')))
        
        self.driver.get("http://infoburo.com.pe/Score/Score?idbc=2")
        

        
    def consultarDNIS(self,dni):
        print(' / / / / // / / / / // / / /')
        wait = WebDriverWait(self.driver, 10)
        #Para borrar
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Documento_filter"]')))
        
        input_field = self.driver.find_element(By.XPATH, '//*[@id="Documento_filter"]')
        self.driver.execute_script("arguments[0].value = '';", input_field)
        
        #Escribiendo el DNI
        self.driver.find_element(By.XPATH, '//*[@id="Documento_filter"]').send_keys(str(dni))
        self.driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
        
        #Esperar un rato para que el modal no detecte bot
        time.sleep(1)
        # Iniciar el bucle while
        start_time = time.time()
        while time.time() - start_time < 30:  # Esperar hasta 20 segundos como máximo
            try:
                modal_load = self.driver.find_element(By.XPATH, "//div[@class='modalLoad']")
                display_style = modal_load.value_of_css_property('display')
                #print(f"Estado de modalLoad: {display_style}")
                if display_style == 'none':
                    driver.save_screenshot('captura_de_pantalla.png')
                    return True  # Salir del bucle si el estilo es 'none'
            except NoSuchElementException:
                print("No se encontró el elemento modalLoad.")
                return False  # Salir del bucle si no se encuentra el elemento
            time.sleep(0.5)  # Esperar 1 segundo antes de la siguiente iteración
      
    def capturarDatos(self):
        pass
      
        
if __name__ == '__main__':
    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_options.headless = True  # Si prefieres que Firefox se ejecute en segundo plano
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)
    

    bot = BotInfoburo(driver)
    bot.open()

    bot.ingresar()
    
    def files():
        contador = 0
        with open("dni.txt", "r", encoding="utf-8") as dnis:
            for dni in dnis.readlines():
                
                registro = open("registro.txt","w")
                registro.write(dni.rstrip()) # escribir en el block
                registro.write("\n")
                registro.close()
        
                verify = bot.consultarDNIS(dni.strip())
                contador += 1
                print('verificando')
                if verify:
                    print(f"- [{contador}] / dni: {dni.strip()} - - - > se encontro")
                    
                else:  
                    print(f"- [{contador}] / dni: {dni.strip()} - - - > no se encontro")
                    
                input('presione enter para continuar')
    files()
  
            


