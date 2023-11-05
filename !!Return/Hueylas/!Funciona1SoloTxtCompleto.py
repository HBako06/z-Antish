from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import reconocerTexto

class Xpath:
    dni= '//*[@id="nuDni"]'
    img_catpcha = '/html/body/main/div/div[1]/form/div/div[4]/div[1]/img'
    img_catpcha = '/html/body/main/div/div[1]/form/div/div[4]/div[1]/img'
    
    btn_consultar = '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button'
    captcha = '/html/body/main/div/div[1]/form/div/div[4]/div[2]/input'
    result = '/html/body/main/div/div[1]/form/div/div[6]/div/img'
    btn_nuevaConsulta = '/html/body/main/div/div[1]/form/div/div[7]/div[2]/button'
    
    div_mensajeIncorrecto  = '/html/body/main/div/div[1]/form/div/div[2]/div'

class BotHuellas:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url, headers):
        firefox_options = Options()
        for key, value in headers.items():
            firefox_options.add_argument(f"--custom-header={key}:{value}")
        firefox_options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get(url)
        
        wait = WebDriverWait(self.driver, 3)
        
        with open('dni.txt', 'r') as f:
            lines = f.readlines()
            
        for dni in lines:
            # aca 
            dni = dni[:8]
            captcha_correcto = False
            while not captcha_correcto:
                start_time = time.time()
                #self.driver.find_element(By.XPATH, Xpath.dni).clear()
                self.driver.find_element(By.XPATH, Xpath.dni).send_keys(str(dni))

                wait.until(EC.visibility_of_element_located((By.XPATH, Xpath.img_catpcha)))
                imagen_elemento = self.driver.find_element(By.XPATH, Xpath.img_catpcha)
                captcha_filename = 'captcha.png'
                imagen_elemento.screenshot(captcha_filename)

                txt_captcha = reconocerTexto.detect_text_from_image(captcha_filename)
                #print(f'captcha es > {txt_captcha}')
                txt_captchaLarge = txt_captcha + 'testo'

                self.driver.find_element(By.XPATH, Xpath.captcha).clear()
                self.driver.find_element(By.XPATH, Xpath.captcha).send_keys(str(txt_captchaLarge))
                self.driver.find_element(By.XPATH, Xpath.btn_consultar).click()

                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH, Xpath.result)))
                    captcha_correcto = True

                    # Obtener el resultado y guardar la imagen
                    result_elemento = self.driver.find_element(By.XPATH, Xpath.result)
                    result_filename = 'result.png'
                    result_elemento.screenshot(result_filename)

                    txt_result = reconocerTexto.detect_text_from_image2(result_filename)
                    print(' > > > ')
                    print(txt_result)
                    # Guardado en el txt
                    with open("resultado.txt", "a") as guardando:
                        guardando.write(f"{txt_result}\n - - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - -\n")
                except:
                    print("Captcha incorrecto. Volviendo a intentar...")
                    continue

                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"El tiempo en completar fue > {elapsed_time} segundos")
                print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

                self.driver.find_element(By.XPATH, Xpath.btn_nuevaConsulta).click()


        #input("pa")

if __name__ == '__main__':
    # Definir la URL del sitio web y los encabezados
    url = "https://serviciosbiometricos.reniec.gob.pe/appConsultaHuellas/index.htm"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-419,es-US;q=0.9,es-PE;q=0.8,es;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "serviciosbiometricos.reniec.gob.pe",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36",
        "dnt": "1",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1"
    }


    bot = BotHuellas(None) 
    bot.open(url, headers)

    
