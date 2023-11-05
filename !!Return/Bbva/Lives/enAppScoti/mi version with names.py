import pyautogui
import time
import os
from PIL import Image
from pytesseract import pytesseract
from printy import printy
from datetime import datetime

# Numero de intentos antes de reniciar la app
N_VECES = 73

#Define path to tessaract.exe
path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

contraseña = 771,361
iniciar = 959,562
quiero = 1091,174
pagar = 797,333
tarjeta = 856,343
banco = 769,218
bbva = 759,516
jumper = 742,329
continuar = 967,971
monto = 749,498

cerrar_apliacion = 1255,990
borrartodo = 1161,110
presionar_aplicacion = 1151,208
##IMAGENES 

img_aceptar = os.path.dirname(os.path.abspath(__file__)) + "\\img\\aceptar.png"
img_confirmar = os.path.dirname(os.path.abspath(__file__)) + "\\img\\confirmar.png"
img_seccion = os.path.dirname(os.path.abspath(__file__)) + "\\img\\seccion.png"

def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
def cerrar_app():
	click(cerrar_apliacion)
	time.sleep(1.5)
	click(borrartodo)
	time.sleep(1)
	click(presionar_aplicacion)
	time.sleep(3.5)

contador = 1

ya_hizo: list[str] = []
while True:
	
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")

	if in_between(current_time,"15:30:00","16:10:00"):
		printy("Hora de mantenimiento , descansando por 40 minutos","y")
		time.sleep(2400)

	try:
		
		click(contraseña)
		pyautogui.typewrite("Jacob2127",interval=0.02)
		click(iniciar)

		printy("El programa se iniciara en 15 segundos","c")
		time.sleep(1)
		print("empezando")
		click(quiero)
		click(pagar)
		click(tarjeta)
		time.sleep(2)
		click(banco)
		time.sleep(0.2)
		click(bbva)
		time.sleep(0.2)

		linealote: int = 0

		with open ('./lote.txt') as texto:		
			for x in texto:
				linealote += 1
				if x in ya_hizo:
					continue

				time.sleep(1)
				click(jumper,click=2)
				pyautogui.press('backspace')
				time.sleep(0.3)

				#pyautogui.borrar(16)
				#time.sleep(0.5)

				pyautogui.typewrite(x, interval=0.025)
				#pyautogui.typewrite(x)
				time.sleep(0.2)
				click(continuar)
				time.sleep(0.1)
				click(monto)
				time.sleep(0.5)
				pyautogui.typewrite("1")

		        #click(pagar,click = 1)
				time.sleep(0.2)
				pyautogui.click(830,962) #Click en el lugar de pagar
				time.sleep(1.4)
				
				rojo = pyautogui.pixelMatchesColor(830,962,(236,17,26))

				if rojo is True:      # Deja poner la contrasena 

					pyautogui.click(830,962) #Click en el lugar de pagar

					# ahora confirmar si es live o no
					contador2 = 0
			
					#print("Entrando")
					lives = open("lives.txt","a")
					#time.sleep(0.3)

					while True:# Un " Y " poqe si no cumple 1 se rompe el bucle
						try:
						
							DEATH = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9)#, region=(0,0,559,997)
							LIVE = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9)#, region=(0,0,570,200)

							if LIVE or DEATH:
								break

							#if contador2 > 100: # Por si no encuyentra ninguno
							if contador2 > 100: # Por si no encuyentra ninguno
								print("Ocurrió un error inesperado")
								lives.close()
								exit()
							contador2 += 1
						except :
							printy("Error no se detectó imagen","c")
							time.sleep(0.3)

					#time.sleep(0.1)
					print("***************************************************")
					
					if DEATH: # Si no es live
						printy(f"N. {linealote} : {x.rstrip()} -------------> [rI]DEATH@")
						time.sleep(0.05)
						click(DEATH)
						pyautogui.press('esc')
						time.sleep(0.01)

					if LIVE: # Por si es LIVE:
						# x y ,horizontal y vertical
						im = pyautogui.screenshot("test.png",region=(811,412,400,35))
						#im = pyautogui.screenshot(region=(100,300, 255, 130))

						text: str = pytesseract.image_to_string(im)
						# text es todo el texto que se encuentra en la foto
						# nombre es el nombre que se encuentra en la lista
						# si queres ver cual es texto en la foto hace print(texto.split())
						nombre :list[str] = text.split()[0:]
						#print(text.split())
						nombre =" ".join(nombre)

						print ('\a')
						lives.write(x.rstrip() + " " + nombre) # escribir en el block
						lives.write("\n")

						printy(f"N. {linealote} :{x.rstrip() + ' '  + nombre} -------------> [n]Live@")
						pyautogui.press('esc')
						time.sleep(0.01)
						pyautogui.press('esc')
						time.sleep(0.01)

						#Queriendo guardar el nombre:
						#pyautogui.screenshot('./Nombres/'+str(x.rstrip())+'.jpg' , region=(1384,467,316,21))
						#pyautogui.screenshot('./Nombres/'+str(linealote)+"++"+str(x.rstrip())+'.png' , region=(1384,467,316,21))
						#time.sleep(0.1)
						# image_Nombre = pyautogui.screenshot('./Nombres/'+str("4556")+'.jpg' , region=(1384,467,180,17))

						#img = cv2.imread("UltimoNombre.jpg")
						#text = pytesseract.image_to_string(img)
						#print(text)
						#nombres = open("nombresLives.txt","a")
						#nombresLives.write(x.rstrip()," | ",text)
						#time.sleep(0.3)
					#print("Gogogogogo")
					lives.close()
					#time.sleep(0.2)
					#time.sleep(2)
					#print("que")
					#click(lugar_clave)
					#time.sleep(1)
					#print("Loop")
					ultimo = open("registro.txt","w")
					ultimo.write(x.rstrip()) # escribir en el block
					ultimo.write("\n")
					ultimo.close()
					ya_hizo.append(x)
					if contador >= N_VECES:
						printy(f"	[rI]Ya hizo {N_VECES}@")
						raise Exception(f"	Ya hizo {N_VECES} veces")
					contador += 1	

	except Exception as E: 
		if  contador >= N_VECES:
			contador = 0
			cerrar_app()
		else:
			print(E)
			break
		
		#lives.close()
	
print("Programa finalizado")	
print("se quedo en la linea: ")
time.sleep(1)