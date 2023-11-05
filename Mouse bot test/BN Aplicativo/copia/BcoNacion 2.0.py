import pyautogui 
import time

#import cv2
#import telegram

donde_escribir = 367,492
ingresar = 286,542
linealote = 0
btn_reiniciarEQUIS = 461,491
btn_reiniciarArriba = 460,388
SalirSesion_SI_button = 442,593

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def buscarnumero(numero):
	image = "./imagenes/"+str(numero) + '.png'
	#time.sleep(0.1)
	#flag = True
	loc = None
	while loc is None:
		loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9, region=(0,0,570,1036))
		#print(loc)
		if loc == None:
			print("Probable error...")
			time.sleep(5)

	pyautogui.moveTo(loc)
	pyautogui.click()
	#print (loc)
def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')
		
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
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
print("\n")

#print("Equis")
click(btn_reiniciarEQUIS)
time.sleep(1)


with open ('./lote.txt') as texto:
	for x in texto:

		linealote += 1
		var = False	
		#time.sleep(0.2)
		click(donde_escribir)
		borrar(5)
		pyautogui.typewrite(x)
		#time.sleep(0.5)
		#click(lugar_clave)

		#calando del 1 al 6
		registro = open("registro.txt","w")
		registro.write(str(x)) # escribir en el block
		registro.write("\n")
		registro.close()
		
		a = None
		contadorerror = 0
		while (a is None): #Esperando que cargue
			Numeros = "./imagenes/Numeros.png"
			a = pyautogui.locateOnScreen(Numeros, grayscale=True, confidence=0.9, region=(311,928,268,119)) # x , y , ancho , alto
			#print(a)
			#time.sleep(0.1)
			if (contadorerror > 20):
				print("Pasando...")
				break

		buscarnumero(num1)
		buscarnumero(num2)
		buscarnumero(num3)
		buscarnumero(num4)
		buscarnumero(num5)
		buscarnumero(num6)


		#print(x.rstrip())
		#time.sleep(0.1)
		#print("Intentando 123456 ")

		#for j in range (1,7):
		#	buscarnumero(j)
			#print(j)

		time.sleep(0.2)
		click(ingresar)
		#print("Verificando...")
		time.sleep(0.2)

		#Confirmacion :
		c = None
		b = None
		d = None
		e = None
		f = None

		contadorerror = 0
		#flag = "flag1"
		while (b is None) and (c is None) and (d is None) and (e is None): # Un " Y " poqe si no cumple 1 se rompe el bucle
			#contador += 1
			aceptar = "./imagenes/aceptar.png"
			b = pyautogui.locateOnScreen(aceptar, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			click(b)
			#print("B",b)

			encontrado = "./imagenes/encontrado.png"
			c = pyautogui.locateOnScreen(encontrado, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			click(c)

			encontrado2 = "./imagenes/encontrado2.png"
			d = pyautogui.locateOnScreen(encontrado2, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			click(d)

			encontrado3 = "./imagenes/encontrado3.png"
			e = pyautogui.locateOnScreen(encontrado3, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			click(e)

			#print("C",c)
			#if (b == None) or (c == None) or (d == None) or (e == None):
			#	time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contadorerror > 4: # Por si no encuyentra ninguno
				print("Ocurrió un error inesperado....")	
				#input()
				click(btn_reiniciarArriba)
				time.sleep(1)
				click(btn_reiniciarArriba)
				break
			contadorerror += 1
		
		if b!=None:
			print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
			#Clickeando en reincio (esa equis del lado)
			#time.sleep(1)
			#print("Equis")
			click(btn_reiniciarEQUIS)

		if (c!=None) or (d!=None) or (e!=None) : # Por si es LIVE:
			print ('\a')
			lives = open("lives.txt","a")
			lives.write(x.rstrip()) + "  | "+num1+num2+num3+num4+num5+num6  #escribir en el block
			lives.write("\n")
			lives.close()
			print("N.", linealote ,": "+x.rstrip()+" -------------> Live" + " | + num1+num2+num3+num4+num5+num6")
			time.sleep(1)
			pyautogui.press('esc')
			while (f is None):
				#print("Cerrando sesión")
				SalirSesion = "./imagenes/SalirSesion.png"
				pyautogui.press('esc')
				f = pyautogui.locateOnScreen(SalirSesion, grayscale=True, confidence=0.9, region=(0,0,570,1036))
				time.sleep(0.3)
				if f!=None: # Si ya está el menu para salirse:
					click(SalirSesion_SI_button)
			time.sleep(1.5)
		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



