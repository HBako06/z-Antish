import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XPATHS:
    Usuario = '//*[@id="username"]'
    Contrasena = '//*[@id="password"]'
    btn_ingresar = '//*[@id="js-login-btn"]'
    busquedaDocumento = '//*[@id="search-field"]' 
    path_frame = '//*[@id="js-page-content"]'
    txt_Nombres = '//div[@class="d-flex flex-column align-items-center justify-content-center p-4"]/h5'
    txt_FechaNacimiento = '/html/body/div[2]/div/div/main/div[2]/div[1]/div[1]/div/div/table/tbody/tr[1]/td[2]'
    txt_Dni = '/html/body/div[2]/div/div/main/div[2]/div[1]/div[1]/div/div/table/thead/tr/th[2]'

class BotOhLogin:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=800,800')
        #chrome_options.add_argument('--disable-javascript')  # Deshabilitar JavaScript
        self.driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe", options=chrome_options)

    def login(self):
        self.driver.get("http://167.114.113.144/buscador/")
        input("???")
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATHS.btn_ingresar)))
        self.driver.find_element(By.XPATH, XPATHS.Usuario).send_keys('C')
        self.driver.find_element(By.XPATH, XPATHS.Contrasena).send_keys('C9X2ZMK23')
        self.driver.find_element(By.XPATH, XPATHS.btn_ingresar).click()

    def search_dni(self, dni):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATHS.busquedaDocumento)))
        input_field = self.driver.find_element(By.XPATH, XPATHS.busquedaDcumento)
        input_field.send_keys(str(dni))
        input_ofield.send_keys(Keys.ENTER)

    def get_inefo(self):
        print('Obteniendo información...')
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATHS.txt_Nombres)))

        NombresCompleto_element = self.driver.find_element(By.XPATH, XPATHS.txt_Nombres)
        NombresCompleto = NombresCompleto_element.text.strip()
        NombresCompleto = re.sub(r'\n.*', '', NombresCompleto)

        fechanacimiento = self.driver.find_element(By.XPATH, XPATHS.txt_FechaNacimiento).text.strip()
        dni = self.driver.find_element(By.XPATH, XPATHS.txt_Dni).text.strip()

        print(f'Nombre: {NombresCompleto} / Fecha: {fechanacimiento} / DNI: {dni}')

    def close(self):
        self.driver.quit()

def process_dni_from_file():
    with open('dni.txt', 'r') as file:
        dni_list = file.readlines()
    
    bot = BotOhLogin()
    bot.login()

    for dni in dni_list:
        dni = dni.strip()  
        bot.search_dni(dni)
        bot.get_info()
    bot.close()

if __name__ == '__main__':
    process_dni_from_file()


