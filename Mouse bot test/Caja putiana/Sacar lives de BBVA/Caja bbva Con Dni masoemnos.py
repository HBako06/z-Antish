import pyautogui 
import time
import datetime
import pytesseract
from PIL import Image
import pyperclip3 as pc
from colorama import init,Fore,Back,Style
import re #Para separar los nombres y apellidos
import requests
import json

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


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
def run():
	pyautogui.click(209,372)#entrar
	time.sleep(2.4)
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

def buscar(ApellidoP,ApellidoM,Nombres):

	url = "https://www.softwarelion.xyz/api/reniec/reniec-nombres"
	_json = { "paterno": ApellidoP, "materno": ApellidoM, "nombres": Nombres }
	token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNDIxLCJjb3JyZW8iOiJtb2NvOTEyeGRAZ21haWwuY29tIiwiaWF0IjoxNjYyMDkwMTU2fQ.B4p41hmxEvTNb3jCunu1LcS2gDe18FKGw9JbAEA3wdo"
	_headers = { 'Content-Type': 'application/json', 'Authorization': token }

	response = requests.post(url, data=json.dumps(_json), headers=_headers)

	#dataJson = response.json()
	payload = response.json()
	results = payload.get('result',[])

	if results:
		for pok in results:
			todos = pok['dni']
			print(todos + "hola")
	return results


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

with open ('./lote.txt') as texto:
	for x in texto:
		print("-------------------------------------------------------------")
		
		linealote = linealote + 1
		

		run() #empezar a logearse
		pc.copy(x) #Copiando los ultimos digiutos
		time.sleep(0.1)
		pyautogui.click(243,504)
		time.sleep(0.3)
		pyautogui.hotkey('ctrl', 'v')
		time.sleep(0.3)
		pyautogui.click(165,706) #glosa
		time.sleep(0.3)
		pyautogui.click(271,946) #continuar

		contador = 0
		b = None
		d = None
		confirmarDatos = "./imagenes/confirmarDatos.png"
		img_entendi = './imagenes/img_entendi.png'


		time.sleep(1)

		while (b is None) and (d is None):# Un " Y " poqe si no cumple 1 se rompe el bucle

			b = pyautogui.locateOnScreen(confirmarDatos,grayscale=True,confidence=0.9, region=(0,63,550,342)) 
			d = pyautogui.locateOnScreen(img_entendi, grayscale=True, confidence=0.9, region=(101,394,346,315))
			#print(b,"b")
			#print (d,"d")
			if (b != None):
				break
			if contador > 150: # Por si no encuyentra ninguno
				print("Presione enter para reconocer nuevamente las imagenes")
				contador = 0
				input()

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

			texNombre = texNombre.rstrip() + texNombre2.rstrip()
			texNombre = texNombre.replace(".","")
			texNombre = texNombre.replace("-","")

			print("N.", linealote ,": "+x.rstrip()+ "  |  " +texNombre.rstrip())
			print(Fore.GREEN+"-----------------------------------> [ Live ]");
			print(Style.RESET_ALL)

			partido = re.split(r'[;\s]\s*',texNombre)


			flag = True

			if (partido[3]!="") & (flag == True):
				nom = partido[0] + " "+ partido[1]
				resulBusquedaDNI = buscar(partido[3],partido[2],nom)
				flag = False
				for pok in resulBusquedaDNI:
					todos = pok['dni']
					print(todos)
					lives.write(todos.rstrip())
					if todos =="":
						print("No se encontró DNI")
				
			if(partido[2]!="") & (flag == True):
				resulBusquedaDNI = buscar(partido[2],partido[1],partido[0])
				flag = False
				for pok in resulBusquedaDNI:
					todos = pok['dni']
					print(todos)
					lives.write(todos.rstrip())
					if todos == null:
						print("No se encontró DNI")
				

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

		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



