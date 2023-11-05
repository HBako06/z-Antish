from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import reconocerTexto
import uuid
import os
import threading

class Xpath:
    dni = '//*[@id="nuDni"]'
    img_catpcha = '/html/body/main/div/div[1]/form/div/div[4]/div[1]/img'
    btn_consultar = '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button'
    captcha = '/html/body/main/div/div[1]/form/div/div[4]/div[2]/input'
    result = '/html/body/main/div/div[1]/form/div/div[6]/div/img'

class BotHuellas:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.options = Options()

    def process_dni(self, dni):
        captcha_id = str(uuid.uuid4())[:8]

        driver = webdriver.Firefox(options=self.options)
        driver.get(self.url)
        driver.find_element(By.XPATH, Xpath.dni).send_keys(str(dni))
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, Xpath.img_catpcha)))

        imagen_elemento = driver.find_element(By.XPATH, Xpath.img_catpcha)
        captcha_filename = f'captcha_{captcha_id}.png'
        with open(captcha_filename, 'wb') as archivo:
            archivo.write(imagen_elemento.screenshot_as_png)

        txt_captcha = reconocerTexto.detect_text_from_image(captcha_filename)
        #print(f'captcha es > {txt_captcha}')
        txt_captcha_large = txt_captcha + 'testo'

        driver.find_element(By.XPATH, Xpath.captcha).send_keys(str(txt_captcha_large))
        driver.find_element(By.XPATH, Xpath.btn_consultar).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Xpath.result)))

        result_elemento = driver.find_element(By.XPATH, Xpath.result)
        result_filename = f'result_{captcha_id}.png'
        with open(result_filename, 'wb') as archivo:
            archivo.write(result_elemento.screenshot_as_png)

        txt_result = reconocerTexto.detect_text_from_image2(result_filename)
        print(f'Resultado:')
        print(txt_result)

        with open("resultado.txt", "a") as guardando:
            guardando.write(str(dni))
            guardando.write("\n")
            guardando.write(str(txt_result))
            guardando.write('\n - - - - - -- - - - - - - - - - - - - - - - -- -- - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - -\n')

        os.remove(captcha_filename)
        os.remove(result_filename)

        driver.quit()

if __name__ == '__main__':
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
    bot = BotHuellas(url, headers)
    dni_list = []
    dni_file_path = 'dni.txt'
    with open(dni_file_path, 'r') as file:
        dni_list = [line.strip() for line in file]

    # Conjunto para almacenar los DNIs procesados
    processed_dnies = set()

    def process_dni_thread():
        global processed_dnies
        while True:
            # Obtener un DNI de la lista que no ha sido procesado
            dni = None
            with threading.Lock():
                if dni_list:
                    dni = dni_list.pop(0)

            if dni is not None and dni not in processed_dnies:
                bot.process_dni(dni)
                # Agregar el DNI al conjunto de DNIs procesados
                with threading.Lock():
                    processed_dnies.add(dni)

    # Crear y lanzar hilos para procesar los DNIs
    num_threads = 3  # Puedes ajustar este número según la cantidad de hilos que desees
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=process_dni_thread)
        thread.start()
        threads.append(thread)

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
