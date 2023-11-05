import undetected_chromedriver as uc
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DATA:
    dni = '45321326'
    clave = 'Crackmovi600'
    
class XPATHS:
    numDocumento = '//*[@id="mat-input-0"]'
    contrasena = '//*[@id="mat-input-1"]'
    
    btn_continuar = '//*[@id="undefined"]/button'
    btn_iniciarsesion = '//*[@id="undefined"]/button'
    btn_confiar_dispositivo = '//*[@id="mat-checkbox-1-input"]'

class BotOhLogin:
    def __init__(self, driver):
        self.driver = driver

    def get_fase1(self):
        self.driver.get("https://mi.scotiabank.com.pe/login")
        
    def get_fase2(self):
        wait0 = WebDriverWait(self.driver, 10)
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.numDocumento)))
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys(str(DATA.dni))
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys('1231')
        time.sleep(1)
        
        self.driver.find_element(By.XPATH, XPATHS.btn_continuar).click()
        
        #esperar que aparesca la contraseña
        time.sleep(5)
        self.driver.save_screenshot("screenshot.png")
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.contrasena)))
        self.driver.find_element(By.XPATH, XPATHS.contrasena).send_keys(str(DATA.clave))
        time.sleep(1)
        self.driver.find_element(By.XPATH, XPATHS.btn_iniciarsesion).click()
        
        time.sleep(5)
        driver.save_screenshot("screenshot.png")
        input('continua2')
        
        
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys('000')
        self.driver.find_element(By.XPATH, XPATHS.claveDigital).click()

if __name__ == '__main__':
    # Configurar opciones de Chrome con undetected_chromedriver
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

    options = uc.ChromeOptions()
    options.add_argument("--headless")
    #options.add_argument(f"user-agent={my_user_agent}")
    
    driver = uc.Chrome(options=options)
    
    # Resto del código aquí...

    # Definimos una función para el procesamiento del DNI en un worker
    def process_dni(dni):
        bot = BotOhLogin(driver)
        bot.get_fase1()
        bot.get_fase2()

    def files():
        with open(f"dni.txt", "r") as dnis:
            for dni in dnis.readlines():
                process_dni(dni.strip())

    files()  # Llamar a la función files al final del código