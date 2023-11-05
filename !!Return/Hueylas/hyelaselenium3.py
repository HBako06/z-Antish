from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class BotHuellas:
    def __init__(self, driver):
        self.driver = driver

    def open_google(self, url, headers):
        firefox_options = Options()
        for key, value in headers.items():
            firefox_options.add_argument(f"--custom-header={key}:{value}")

        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get(url)

        time.sleep(10)
        #continuar
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button').click() 
        time.sleep(10)
        #continuar
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button').click() 
        time.sleep(10)
        #continuar
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button').click() 
        time.sleep(10)
        #continuar
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/form/div/div[5]/div[2]/button').click() 


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
    bot = BotHuellas(None)  # La instancia del
    bot.open_google(url, headers)

    
