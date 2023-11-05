import pyautogui 
import time

#import pytesseract
from PIL import Image
import pyperclip3 as pc
import datetime


#pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

numtarj = 116,253
continuar1 = 278,465
monto = 233,459
rojoabajo = 289,994



def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
def ingresarACuenta():
	time.sleep(0.5)
	pyautogui.click(297,316)
	time.sleep(0.5)
	pyautogui.typewrite('Pulsar200')
	time.sleep(0.3)
	pyautogui.click(291,683) # click iniciar
	time.sleep(12) # esperar
	pyautogui.click(345,153) # quiero
	time.sleep(1)
	pyautogui.click(297,272) # pagar
	time.sleep(1)
	pyautogui.click(186,301) # tarjeta de credito
	time.sleep(5)
	pyautogui.click(400,182) # mostrar bancos
	time.sleep(0.4)
	pyautogui.click(103,424) # click en bbva 
	time.sleep(0.4)

#.------------------------------------------
print("po po po po po po po po po po po po po ")
print("***************")

teequiste = input("Archivo txt:  ")
logeopreg = input(" ¿logeo? si/no:  ")

print("**************************************************")
print("\n")
print("Presione 'Enter' para continuar")
input()

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
print ('\a')

linealote= 0
flag2 = True
contadorReinicio = 0

if logeopreg=="si":
	ingresarACuenta()

with open ('./lotes/'+teequiste+'.txt') as texto:
	for x in texto:
		#print("Dentro")
		linealote += 1

		contadorReinicio += 1
		if(contadorReinicio > 100):
			time.sleep(0.5)
			pyautogui.press('esc')
			time.sleep(0.3)
			pyautogui.press('esc')
			time.sleep(0.3)
			pyautogui.press('esc')
			time.sleep(0.3)

			pyautogui.click(454,595)
			time.sleep(7)
			ingresarACuenta()
			contadorReinicio = 0

		time.sleep(0.5)
		pc.copy(x)
		pyautogui.doubleClick(numtarj)
		time.sleep(0.1)
		pyautogui.hotkey('ctrl', 'v') # pegando lo copiado
		pyautogui.click(continuar1) # click en continuar

		time.sleep(0.6)
		pyautogui.typewrite('1')
		pyautogui.click(rojoabajo)		

		#time.sleep(1)
		contador = 0
		b = None
		c = None
		img_aceptar = "aceptar.png"
		img_confirmar = 'confirmar.png'
		while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle

			#print("Dentro")
			#time.sleep(0.1)
			#rojo
			blanco = pyautogui.pixelMatchesColor(462,993,(236,17,26))
			#print(blanco)
			if (blanco is True):
				pyautogui.click(rojoabajo)

			#img_aceptar = "aceptar.png"
			#time.sleep(0.2)
			#print("antes")
			b = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9, region=(333,498,228,147) )
			#print("luego")
			#print(b, "b")
			#time.sleep(1)
			
			#img_confirmar = 'confirmar.png'
			#time.sleep(0.2)
			c = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9, region=(0,0,251,214))
			#print(c, "c")
			#time.sleep()
			#if (b == None) or (c == None):
				#time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contador > 200: # Por si no encuyentra ninguno
				#time.sleep(0.03)
				print("Ocurrió un error ( imagen no detectada o continuar rojo")
				print("Enter para continuar")
				contador = 0
				#lives.close()
				input()

			contador += 1


		#print("fin test")
		#input()

		#time.sleep(0.1)
		print("***************************************************")
		fechaActual = datetime.datetime.now()

		if b!=None: # Si no es live
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote ,": "+x.rstrip()+ "  -------------> Death")
			#time.sleep(0.2)
			click(b) # click en aceptar de la imagen 
			time.sleep(0.4)
			pyautogui.press('esc')
			#time.sleep(0.3)
		if c!=None: # Por si es LIVE:
			print ('\a')
			
			#Queriendo guardar el nombre:
			#ImagNombre = pyautogui.screenshot(region= (coords)) # d pc
			ImagNombre = pyautogui.screenshot(region= (102,324,252,22)) # d pc
			#ImagNombre = pyautogui.screenshot(region= (281,167,250,20)) # Disco c lap
			#texNombre = pytesseract.image_to_string( ImagNombre , config= '--psm 7 -c tessedit_char_whitelist= abcdefghijkmnñlopqrsturstuvwxyz')

			lives = open("lives.txt","a")
			lives.write(x.rstrip()) # escribir en el block
			#lives.write(x.rstrip()+"	"+texNombre.rstrip()) # escribir en el block
			lives.write("\n")
			lives.close()

			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')

			print(fechaActual2, " | ","N. ", linealote ,": "+x.rstrip()+ "  -------------> Live")
			pyautogui.press('esc')
			time.sleep(0.2)
			pyautogui.press('esc')
			flag2 = False # Para que sea live

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