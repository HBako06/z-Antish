import pyautogui 
import time

# pyautogui.displayMousePosition()


#introduceNumero = 1470,576 
numtarj = 282,202
monto = 324,329
continuar = 279,955
#aceptar = 286,608
#live_salir = 1382,86
#posibles_contras 
#123456
#111111
#555555
#222222
def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)
def borrar(i):
	for i in range (1,i):
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
			#var = False	
			#print("Comenzando")
			click(numtarj,click=2)
			pyautogui.press('backspace')

			#time.sleep(0.2)
			time.sleep(0.4)
			pyautogui.typewrite(x)
			time.sleep(0.2)
			#pyautogui.typewrite(x, interval=0.07)
			# Logueando monto:
			#click(monto)
			if (linealote == 1):
				click(monto)
				borrar(3)
				pyautogui.typewrite("99", interval=0.03)

			click(continuar,click = 2)
			#time.sleep(2.6)
			
			# ahora confirmar si es live o no
			contador = 0
			b = None
			c = None
			print("Entrando")
			lives = open("lives.txt","a")

			while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
				try:
					print("Dentro")
					acept = "aceptar.png"
					time.sleep(0.2)
					b = pyautogui.locateOnScreen(acept, grayscale=True, confidence=0.9, region=(0,0,559,997))
					print(b, "b")
					#time.sleep(1)
					
					confirm = "confirm.png"
					time.sleep(0.2)
					c = pyautogui.locateOnScreen(confirm, grayscale=True, confidence=0.9, region=(0,0,570,200))
					print(c, "c")
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
				except :
					time.sleep(0.1)

			time.sleep(0.3)
			print("***************************************************")

			if b!=None: # Si no es live
				print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
				time.sleep(0.1)
				click(b)
				#time.sleep(0.3)
			if c!=None: # Por si es LIVE:
				print ('\a')
				lives.write(x.rstrip()) # escribir en el block
				lives.write("\n")
				print("N.", linealote ,": "+x.rstrip()+" -------------> Live")
				pyautogui.press('esc')

				#Queriendo guardar el nombre:
				time.sleep(0.2)
				#pyautogui.screenshot('./Nombres/'+str(x.rstrip())+'.jpg' , region=(1384,467,316,21))
				#pyautogui.screenshot('./Nombres/'+str(linealote)+"++"+str(x.rstrip())+'.png' , region=(1384,467,316,21))
				#time.sleep(0.1)
				# image_Nombre = pyautogui.screenshot('./Nombres/'+str("4556")+'.jpg' , region=(1384,467,180,17))

				#img = cv2.imread("UltimoNombre.jpg")
				#text = pytesseract.image_to_string(img)
				#print(text)
				#nombres = open("nombresLives.txt","a")
				#nombresLives.write(x.rstrip()," | ",text)
				#time.sleep(0.3)
			#print("Gogogogogo")
			lives.close()
			time.sleep(0.2)
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
	#time.sleep(4)
#lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()