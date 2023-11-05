from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import reconocerTexto
import concurrent.futures
import uuid
import os


class Xpath:
    dni = '//*[@id="nuDni"]'
    img_catpcha = '/html/body/main/div/div[1]/form/div/div[4]/div[1]/img'
    img_catpcha = '/html/body/main/div/div[1]/form/div/div[4]/div[1]/img'

    btn_consultar = '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button'
    captcha = '/html/body/main/div/div[1]/form/div/div[4]/div[2]/input'
    result = '/html/body/main/div/div[1]/form/div/div[6]/div/img'


class BotHuellas:
    def __init__(self, driver):
        self.driver = driver

    def open(self, i, dni, url, headers):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        for key, value in headers.items():
            firefox_options.add_argument(f"--custom-header={key}:{value}")

        # Generar identificador único para el captcha y el resultado
        # Los primeros 8 caracteres del UUID generado
        captcha_id = str(uuid.uuid4())[:8]
        result_id = str(uuid.uuid4())[:8]

        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 20)

        # continuar
        self.driver.find_element(By.XPATH, Xpath.dni).send_keys(str(dni))

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, Xpath.img_catpcha)))
        imagen_elemento = self.driver.find_element(By.XPATH, Xpath.img_catpcha)
        # Guardar la imagen en un archivo local
        captcha_filename = f'captcha_{captcha_id}.png'
        with open(captcha_filename, 'wb') as archivo:
            archivo.write(imagen_elemento.screenshot_as_png)

        txt_captcha = reconocerTexto.detect_text_from_image(captcha_filename)
        print(f'captcha es > {txt_captcha}')
        txt_captchaLarge = txt_captcha + 'testo'

        self.driver.find_element(By.XPATH, Xpath.captcha).send_keys(
            str(txt_captchaLarge))
        self.driver.find_element(By.XPATH, Xpath.btn_consultar).click()

        # print(f'DNI > {dni}  |  captcha > {txt_captchaLarge}')
        # Esperar el resultado
        wait.until(EC.visibility_of_element_located((By.XPATH, Xpath.result)))

        result_elemento = self.driver.find_element(By.XPATH, Xpath.result)
        # Guardar la imagen del resultado con un nombre único
        result_filename = f'result_{result_id}.png'
        with open(result_filename, 'wb') as archivo:
            archivo.write(result_elemento.screenshot_as_png)

        txt_result = reconocerTexto.detect_text_from_image2(result_filename)
        print(f'Resultado :')
        print(txt_result)

        # Guardado en el txt
        guardando = open("resultado.txt", "a")
        guardando.write(str(dni))
        guardando.write("\n")
        guardando.write(str(txt_result))
        guardando.write(
            '\n - - - - - -- - - - - - - - - - - - - - - - -- -- - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - -\n')
        guardando.close()

        os.remove(captcha_filename)
        os.remove(result_filename)

        self.driver.close()


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

    dni_list = []
    max_workers = 2
    dni_file_path = 'dni.txt'
    with open(dni_file_path, 'r') as file:
        dni_list = [line.strip() for line in file]

    bot = BotHuellas(None)

    # Procesar los DNIs en paralelo utilizando multiprocesos
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i, dni in enumerate(dni_list, start=1):
            executor.submit(open, i, dni, url, headers)
