import pyautogui 
import time

import pytesseract
from PIL import Image
import pyperclip3 as pc
from io import open

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

numtarj = 312,177
monto = 324,329
buscar = 289,961
#coords = 25,164,208,16

def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
def reiniciar():
	time.sleep(1)
	pyautogui.click(61,1011) #productos
	time.sleep(0.2)
	pyautogui.click(171,1009) #operaciones
	time.sleep(0.2)
	pyautogui.click(141,191) #pagos y recargar
	time.sleep(0.3)
	pyautogui.click(157,292) #tarjeta de credito
	time.sleep(0.3)
	pyautogui.click(123,268) #tarjeta oh
	time.sleep(0.3)
	pyautogui.click(188,182) #cuenta simple
	time.sleep(0.5)


print("***************")
print("Presione 'Enter' para continuar")
input()

#live

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")

numerosseguidos = 0
linealote= 0
flag2 = True

with open ('./lote.txt') as texto:
	for x in texto:
		#print("Dentro")
		linealote += 1
		numerosseguidos += 1
		if numerosseguidos > 50:
			time.sleep(0.5)
			pyautogui.press('esc')
			time.sleep(1)
			pyautogui.click(188,182) #cuenta simple
			#pyautogui.click(241,262) #cuenta simple2
			time.sleep(1)
			numerosseguidos = 0

		time.sleep(0.5)
		pc.copy(x)
		pyautogui.doubleClick(numtarj)
		time.sleep(0.1)
		pyautogui.hotkey('ctrl', 'v') # pegando lo copiado
		pyautogui.click(buscar) # click en continuar


		# ahora confirmar si es live o no
		contador = 0
		b = None
		c = None
		#print("Entrando")
		
		#time.sleep(0.3)
		img_aceptar = "aceptar.png"
		img_confirmar = 'confirmar.png'
		while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
			#print("Dentro")
			#time.sleep(0.2)
			#print("antes")
			b = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9, region=(6,393,564,369))
			#print("luego")
			#print(b, "b")
			#time.sleep(1)
			
			#img_confirmar = 'confirmar.png'
			c = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9, region=(0,0,261,184))
			#print(c, "c")
			#time.sleep()
			#if (b == None) or (c == None):
			#	time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contador > 100: # Por si no encuyentra ninguno
				print("Ocurrió un error inesperado, presione enter para reintentar")
				contador = 0
				input()
				

			contador += 1


		#time.sleep(0.1)
		print("***************************************************")

		if b!=None: # Si no es live
			print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
			#time.sleep(0.2)
			pyautogui.click(285,630) #aceptar
			#time.sleep(0.3)
		if c!=None: # Por si es LIVE:
			print('\a')
			#Queriendo guardar el nombre:
			ImagNombre = pyautogui.screenshot(region = (25,164,208,16)) 
			texNombre = pytesseract.image_to_string( ImagNombre , config= '--psm 7 -c tessedit_char_whitelist= abcdefghijkmnlopqrsturstuvwxyz0123456789')

			lives = open("lives.txt","a")
			lives.write(x.rstrip()+" "+texNombre.rstrip()) # escribir en el block
			lives.write("\n")
			lives.close()
			print("N.", linealote ,": "+x.rstrip()+ "  |  " +texNombre.rstrip()+ "  -------------> Live")
			#print("N.", linealote ,": "+x.rstrip()+ "  |  "+"  -------------> Live")
			pyautogui.press('esc')
			
			time.sleep(0.3)
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