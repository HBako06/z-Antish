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
        
if __name__ == '__main__':
    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)
    

    bot = BotInterbank(driver)
    bot.open()
    input()

