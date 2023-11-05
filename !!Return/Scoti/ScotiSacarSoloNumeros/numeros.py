import pyautogui 
import time
import os
from PIL import Image
from pytesseract import pytesseract
from printy import printy
import pyperclip3 as pc

documento = 775,388
continuar = 960,510
cambiar_usuario = 880,267
error_aplicativo = 1134,583
contraseña = 771,359
iniciar = 957,563

cerrar_apliacion = 1255,986
borrartodo = 1159,111
presionar_aplicacion = 1150,204
bloqueado = 1023,615

#Define path to tessaract.exe
path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

##IMAGENES 
img_aceptar = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\aceptar.png"
img_bloqueado = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\bloqueado.png"
img_tarjeta = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\tarjeta.png"
img_afiliate = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\afiliate.png"
img_error = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\error.png"
img_logo = os.path.dirname(os.path.abspath(__file__)) + "\\alfa\\logo.png"

def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')

def cerrar_app():
	click(cerrar_apliacion)
	time.sleep(0.5)
	click(borrartodo)
	time.sleep(0.6)
	click(presionar_aplicacion)
	time.sleep(3.5)

def cancelar():
	pyautogui.press('esc')
	pyautogui.press('esc')
	time.sleep(0.2)
	click(documento,click=2)
	pyautogui.press('backspace')
	time.sleep(0.1)
	pyautogui.typewrite("46346305",interval= 0.014)
	time.sleep(0.1)
	click(continuar)
	time.sleep(1.8)
	click(contraseña)
	time.sleep(0.1)
	pyautogui.typewrite("11111111",interval= 0.016)
	time.sleep(0.1)
	click(iniciar)
	time.sleep(2)
	click(bloqueado)
	time.sleep(0.2)


linealote= 0

while True:
    with open('./lote.txt', 'r') as f:
        lines = f.readlines()
        total_lines = len(lines)
        if linealote >= total_lines:
            break
        
		# Procesar la línea actual
		line = lines[linealote]
		values = line.strip().split('\t')
		valor1 = values[0]
		valor2 = values[1]

		time.sleep(0.6)
		click(documento)
		pyautogui.typewrite(valor1,interval= 0.013)
		time.sleep(0.1)
		click(continuar)
		time.sleep(1.7)
		click(contraseña)
		time.sleep(0.1)
		pyautogui.typewrite(valor2,interval= 0.016)
		time.sleep(0.4)
		click(iniciar)
	
		# Realizar las acciones necesarias con los valores leídos

		contador = 0
		
		#print("Entrando")
		lives = open("lives.txt","a")
		#time.sleep(0.3)

		while True: # Un " Y " poqe si no cumple 1 se rompe el bucle
			try:

				DEATH = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9, region= (1079,560,1185,592))
				DEATH2 = pyautogui.locateOnScreen(img_bloqueado,grayscale=True,confidence=0.9) # ,region=(675,482,1237,732)) 
				DEATH3 = pyautogui.locateOnScreen(img_tarjeta,grayscale=True,confidence=0.9)#, region=(0,0,559,997)
				DEATH4 = pyautogui.locateOnScreen(img_afiliate,grayscale=True,confidence=0.9)#, region=(0,0,559,997)
				DEATH5 = pyautogui.locateOnScreen(img_error,grayscale=True,confidence=0.9)#, region=(0,0,559,997)
				LIVE = pyautogui.locateOnScreen(img_logo,grayscale=True, confidence=0.9)#, region=(0,0,570,200)

				if LIVE or DEATH or DEATH2 or DEATH3 or DEATH4:
					break

				if contador > 350: # Por si no encuyentra ninguno
					printy("Ocurrió un error inesperado","nB")
					lives.close()
					exit()
				contador += 1
			except :
				printy("Error no se detectó imagen", "n")
				time.sleep(0.1)

		#time.sleep(0.1)
				print("***************************************************")

		if DEATH: # Si no es live
			printy(f"N. {linealote} : {valor1.rstrip()  + '  ' + valor2} ----------> [rI]DEATH@")
			time.sleep(0.01)
			click(DEATH)
			time.sleep(0.2)
			#click(contraseña)
			#pyautogui.typewrite(valor3,interval= 0.016)
			#time.sleep(0.2)
			#click(iniciar)
			#time.sleep(2.5)
			#click(DEATH)
			#time.sleep(0.2)
			click(cambiar_usuario)
			
		if DEATH2: # Si no es live
			printy(f"N. {linealote} : {valor1.rstrip()  + '  ' + valor2} ----------> [y]BLOQUEADO@")
			time.sleep(0.01)
			click(DEATH2)
			time.sleep(0.2)
			click(cambiar_usuario)

		if DEATH3: # Si no es live
			printy(f"N. {linealote} : {valor1.rstrip()  + '  ' + valor2} ----------> [cU]Tarjeta@")
			time.sleep(0.2)
			cancelar()
			click(cambiar_usuario)
			time.sleep(0.1)

		if DEATH4: # Si no es live
			printy(f"N. {linealote} : {valor1.rstrip()  + '  ' + valor2} ----------> [cU]BAN BAN@")
			time.sleep(0.01)
			click(error_aplicativo)
			time.sleep(0.2)
			click(documento,click=2)
			pyautogui.press('backspace')
			time.sleep(0.1)

		if LIVE: # Por si es LIVE:
			# x y ,horizontal y vertical
			im = pyautogui.screenshot("test.png",region=(700,536, 350, 48))
			#im = pyautogui.screenshot(region=(100,300, 255, 130))
			
			text: str = pytesseract.image_to_string(im)
			# text es todo el texto que se encuentra en la foto
			# nombre es el nombre que se encuentra en la lista
			# si queres ver cual es texto en la foto hace print(texto.split())
			numero :list[str] = text.split()[0:]
			#print(text.split())
			numero =" ".join(numero)

			print ('\a')
			lives.write(valor1.rstrip()  + "  " + valor2  + " | "  + numero) # escribir en el block
			lives.write("\n")
			printy(f"N. {linealote} : {valor1.rstrip() + '  ' + valor2  + ' | ' + numero} ---> [n]Logo Encontrado@")
			time.sleep(0.01)
			pyautogui.press('esc')
			time.sleep(0.01)
			cerrar_app()

			#Queriendo guardar el nombre:
			time.sleep(0.2)

		#print("Gogogogogo")
		lives.close()
		ultimo = open("registro.txt","w")
		ultimo.write(valor1.rstrip()) # escribir en el block
		ultimo.write("\n")
		ultimo.close()
		# Incrementar el contador de líneas
        linealote += 1
			

#lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()