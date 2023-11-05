from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import FirefoxProfile

class BotHuellas:
    def __init__(self, driver):
        self.driver = driver

    def open_google(self):
        self.driver.get("https://serviciosbiometricos.reniec.gob.pe/appConsultaHuellas/index.htm")

if __name__ == '__main__':
    # Configurar opciones de Firefox
    firefox_options = Options()
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)

    bot = BotHuellas(driver)
    bot.open_google()

    
