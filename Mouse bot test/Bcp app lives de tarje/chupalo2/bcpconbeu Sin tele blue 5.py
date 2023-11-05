import pyautogui 
import time

introduceNumero = 446,582
numtarj = 366,184
continuar = 420,815
live_salir = 22,80
#posibles_contras 
#123456
#111111
#555555
#222222
def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar():
	for i in range (1,17):
		pyautogui.press('backspace')

print("***************")
print("Presione 'Enter' para continuar")
input()

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
linealote= 0
try:
	with open ('./lote.txt') as texto:
		for x in texto:

			linealote += 1
			var = False	


			click(introduceNumero)
			time.sleep(0.2)
			click(numtarj)
			borrar()
			time.sleep(0.2)
			#pyautogui.typewrite(x)
			#print("Probando: ", x)
			pyautogui.typewrite(x, interval=0.07)
			time.sleep(0.5)
			pyautogui.press('esc')
			time.sleep(0.8)
			click(continuar)
			time.sleep(2.6)

			# ahora confirmar si es live o no
			contador = 0
			b = None
			c = None
			#print("Entrando")
			lives = open("lives.txt","a")
			while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
				acept = "aceptarcito.png"
				b = pyautogui.locateOnScreen(acept, grayscale=True, confidence=0.9, region=(0,0,559,997))
				#print(b, "b")
				#time.sleep(1)
				
				confirm = "confirm.png"
				c = pyautogui.locateOnScreen(confirm, grayscale=True, confidence=0.9, region=(0,0,570,1036))
				#print(c, "c")
				#time.sleep()
				if (b == None) or (c == None):
					time.sleep(0.2)
					#print("Espere...")
					#print(b)
					#time.sleep(5)
				if contador > 100: # Por si no encuyentra ninguno
					print("Ocurrió un error inesperado")
					lives.close()
					exit()
				contador += 1

			time.sleep(0.3)
			print("***************************************************")

			if b!=None:
				print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
				click(b)
				#time.sleep(0.5)
			if c!=None: # Por si es LIVE:
				print ('\a')
				lives.write(x.rstrip()) # escribir en el block
				lives.write("\n")
				print("N.", linealote ,": "+x.rstrip()+" -------------> Live")

				#Queriendo guardar el nombre:
				#time.sleep(0.2)
				#pyautogui.screenshot('./Nombres/'+str(x.rstrip())+'.jpg' , region=(1384,467,316,21))
				#pyautogui.screenshot('./Nombres/'+str(linealote)+"++"+str(x.rstrip())+'.png' , region=(1384,467,316,21))
				#time.sleep(0.1)
				# image_Nombre = pyautogui.screenshot('./Nombres/'+str("4556")+'.jpg' , region=(1384,467,180,17))

				#img = cv2.imread("UltimoNombre.jpg")
				#text = pytesseract.image_to_string(img)
				#print(text)
				#nombres = open("nombresLives.txt","a")
				#nombresLives.write(x.rstrip()," | ",text)

				click(live_salir)
				#time.sleep(0.3)
			lives.close()
			time.sleep(0.4)
			#time.sleep(2)
			#print("que")
			#click(lugar_clave)
			#time.sleep(1)
			#print("Loop")
			ultimo = open("registro.txt","w")
			ultimo.write(x.rstrip()) # escribir en el block
			ultimo.write("\n")
			ultimo.close()

except:
	print("error en el pograma")
	lives.close()

	#time.sleep(4)
lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para continuar")
input()
