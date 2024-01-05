import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import os
from basededatos import BaseDeDatos

class BotInfoburo:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=800,800')
        #chrome_options.add_argument('--headless')  # Modo headless para ejecutar en segundo plano
        self.driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe", options=chrome_options)

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
        


    def consultarDNIS(self, dni):
        self.print2(' \n / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / \n')
        wait = WebDriverWait(self.driver, 40)
        # Para borrar
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Documento_filter"]')))

        input_field = self.driver.find_element(By.XPATH, '//*[@id="Documento_filter"]')
        self.driver.execute_script("arguments[0].value = '';", input_field)

    
        dni_recortado = dni.strip()[:8]
        self.print2(f' {dni} > >')
        # Escribiendo el DNI
        self.driver.find_element(By.XPATH, '//*[@id="Documento_filter"]').send_keys(str(dni_recortado))
        self.driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

        # Esperar un rato para que el modal no detecte bot
        time.sleep(1)
        # Iniciar el bucle while
        start_time = time.time()
        while time.time() - start_time < 30:  # Esperar hasta 20 segundos como máximo
            try:
                modal_load = self.driver.find_element(By.XPATH, "//div[@class='modalLoad']")
                display_style = modal_load.value_of_css_property('display')
                # self.print2(f"Estado de modalLoad: {display_style}")
                if display_style == 'none':
                    self.driver.save_screenshot('captura_de_pantalla.png')
                    
                    self.capturarDatos()
                    
                    return True  # Salir del bucle si el estilo es 'none'
            except:
                self.print2("No se encontró el elemento modalLoad.")
                return False  # Salir del bucle si no se encuentra el elemento
            time.sleep(0.5)  # Esperar 1 segundo antes de la siguiente iteración

    def capturarDatos(self):
        # Obtener el HTML de la página actual
        page_source = self.driver.page_source
        
        # Analizar el HTML con BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Buscar la tabla con id "resfinanciero"
        tabla_resfinanciero = soup.find('div', {'id': 'resfinanciero'})
        tabla_correos = soup.find('div', {'id': 'correos1'})
        tabla_telefonos = soup.find('div', {'id': 'telefonos1'})
        seccion_persona = soup.find('div', {'class': 'card-body text-mediano'})
        
        try:
                    
            self.print2('\n Persona > >')

            # Buscar las filas dentro de la sección persona
            for row in seccion_persona.find_all('div', {'class': 'row'}):
                # Obtener el texto de la columna font-weight-bold
                columna_bold = row.find('div', {'class': 'font-weight-bold'})
                columna_valor = row.find('div', {'class': re.compile('score-gen.*')})

                if columna_bold and columna_valor:
                    # Imprimir el texto de la columna bold y el valor correspondiente
                    self.print2(f"{columna_bold.text.strip()}: {columna_valor.text.strip()}")

        except:
            self.print2("No se encontró la sección 'card-body text-mediano'")
            
        #Resumen financiero
        try:
            self.print2('\n Estado Financiero > >')
            # Imprimir los encabezados
            self.print2("Entidad, Préstamo, TC, HIPOTECARIO, AUTO, COMERCIAL, Linea Disponible")

            # Imprimir la información de la tabla
            for row in tabla_resfinanciero.select('tbody tr'):
                columns = row.find_all('td')
                self.print2(", ".join(column.text.strip() for column in columns))
        except:
            self.print2("No se encontró la tabla con id 'resfinanciero'")
        
        #Correos
        try: 
            self.print2('\n Correos > >')
            # Imprimir la información de la tabla
            for row in tabla_correos.select('tbody tr'):
                columns = row.find_all('td')
                self.print2(", ".join(column.text.strip() for column in columns))
        except:
            self.print2("No se encontró la tabla con id 'correos1'")
            
        #Telefonos
        try: 
            self.print2('\n Telefonos > >')
            self.print2("Fecha, Actualización, Teléfono, Fuente, Plan")
            # Imprimir la información de la tabla
            for row in tabla_telefonos.select('tbody tr'):
                columns = row.find_all('td')
                self.print2(", ".join(column.text.strip() for column in columns))
        except:
            self.print2("No se encontró la tabla con id 'telfono1'")

    def print2(self,message, filename="log.txt"):
        with open(filename, "a") as file:
            file.write(message + "\n")
        print(message)     

if __name__ == '__main__':

    base_de_datos = BaseDeDatos()
    namedb = "info2024selenium chrome"
    base_de_datos.aumentar_veces_iniciado(namedb)
    estado = base_de_datos.verificar_estado_bot("info2024selenium chrome")


    if estado:
        bot = BotInfoburo()
        bot.open()
        bot.ingresar()
        os.system('cls')

        def files():
            contador = 0
            with open("dni.txt", "r", encoding="utf-8") as dnis:
                for dni in dnis.readlines(): # Obtener los primeros 8 caracteres del DNI
                    bot.consultarDNIS(dni)
                    
                    contador += 1

        files()
    else:
        print('DeprecationWarning: executable_path has been deprecated, please pass in a Service object self.driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe",  options=chrome_options)')
    
    
