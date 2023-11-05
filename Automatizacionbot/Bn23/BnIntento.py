from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time
import colorama  # Importar el módulo colorama
from colorama import Fore, Style  # Importar estilos de color

class XPATHS:
    numeroTarjeta = '//*[@id="txtNumeroTarjeta"]'
    tipoDocumento = '//*[@id="cboTipoDoc-button"]'
    seleccionarDNI = '//*[@id="cboTipoDoc-menu"]/li[2]/a'
    numeroDocumento = '//*[@id="txtNumDoc"]'

    
    
class BotOhLogin:
    def __init__(self, driver):
        self.driver = driver

    def get_fase1(self):
        self.driver.get("https://bancaporinternet.bn.com.pe/BNWeb/Inicio")
        
    def get_fase2(self):
        wait0 = WebDriverWait(self.driver, 10)
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.numeroTarjeta)))
        
        self.driver.find_element(By.XPATH, XPATHS.numeroTarjeta).clear()
        self.driver.find_element(By.XPATH, XPATHS.numeroTarjeta).send_keys('4214100227871045')
        
        self.driver.find_element(By.XPATH, XPATHS.tipoDocumento).click()
        self.driver.find_element(By.XPATH, XPATHS.seleccionarDNI).click()

        self.driver.find_element(By.XPATH, XPATHS.numeroDocumento).clear()
        self.driver.find_element(By.XPATH, XPATHS.numeroDocumento).send_keys('12345678')
        


    def get_fase3(self, num_pathNumerico):
        wait0 = WebDriverWait(self.driver, 10)
        teclado_numerico = wait0.until(EC.presence_of_element_located((By.XPATH, XPATHS.tecladoNumerico)))

        # Obtener todos los elementos dentro del teclado numérico
        elementos_teclado = teclado_numerico.find_elements(By.XPATH, './div')

        # Iterar sobre los elementos y hacer clic en los números deseados
        for num in num_pathNumerico:
            for elemento in elementos_teclado:
                if elemento.text.strip() == num:
                    elemento.click()
                    break
            else:
                print(f"No se encontró el elemento {num} en el teclado numérico.")
        self.driver.find_element(By.XPATH, XPATHS.btnIniciarSesion).click()


    def get_Verificar(self):
        try:
            wait0 = WebDriverWait(self.driver, 15)
            wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.ventanaError)))
            
            mensaje_error_element = self.driver.find_element(By.XPATH, XPATHS.mssgeVentanaTxt)
            mensaje_error = mensaje_error_element.text.strip()
            print(mensaje_error)
            return False
        
        except Exception as e:
            return True
        
    def verify_get_logo(self):
        expected_url = "https://enlinea.tarjetaoh.pe/tarjeta-oh/mis-saldos"
        current_url = self.driver.current_url
        if current_url == expected_url:
            return True
        else:
            return False
    def get_logo(self):
        #self.driver.get("https://enlinea.tarjetaoh.pe/tarjeta-oh/mis-saldos")
        
        #Cerrar cuenta:
        wait0 = WebDriverWait(self.driver, 15)
        try:
            wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.login_divCerrar)))
            self.driver.find_element(By.XPATH, XPATHS.login_divCerrar).click()
        except:
            pass
        
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.login_opciones)))
        self.driver.find_element(By.XPATH, XPATHS.login_opciones).click()
        
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.longin_cerrarSesion)))
        self.driver.find_element(By.XPATH, XPATHS.longin_cerrarSesion).click()
        time.sleep(0.3)
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.login_confirmarSalir)))
        self.driver.find_element(By.XPATH, XPATHS.login_confirmarSalir).click()
        
    def color_print(self, text, color_code):
        # Imprimir en pantalla con color utilizando colorama
        print(f"{color_code}{text}{Style.RESET_ALL}")
        
if __name__ == '__main__':
    #max_workers = 5
    num_pathNumerico = '123456'
    
    colorama.init()  # Inicializar colorama
    # Códigos ANSI para los colores usando colorama
    COLOR_RED = Fore.RED
    COLOR_GREEN = Fore.GREEN
    
    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_options.add_argument('--window-size=800,800')
    #firefox_options.add_argument("--headless")
    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=firefox_options)
    
    # Definimos una función para el procesamiento del DNI en un worker
    def process_dni():
        bot = BotOhLogin(driver)
        bot.get_fase1()
        bot.get_fase2()


    process_dni()
    input()