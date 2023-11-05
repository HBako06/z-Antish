import pyautogui 
import time

numtarj = 282,202
monto = 324,329
continuar = 279,955

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
flag2 = True

with open ('./lote.txt') as texto:
	for x in texto:
		#print("Dentro")
		linealote += 1
		#var = False	
		#print("Comenzando")
		time.sleep(1.1)
		if (flag2): # Por si es No live comenzando
			click(numtarj,click=2)
			time.sleep(0.1)
			pyautogui.press('backspace')
			#time.sleep(0.2)
			time.sleep(0.2)
			pyautogui.typewrite(x.rstrip())
		else:
			click(numtarj,click=2)
			time.sleep(1)
			pyautogui.press('backspace')
			#time.sleep(0.2)
			time.sleep(1)
			pyautogui.typewrite(x.rstrip(), interval=0.07)
			flag2 = True

		
		#pyautogui.typewrite(x, interval=0.07)
		# Logueando monto:
		#click(monto)
		if (linealote == 1):
			time.sleep(0.2)
			click(monto)
			borrar(3)
			pyautogui.typewrite("99", interval=0.03)

		click(continuar)
		time.sleep(0.5)
		
		# ahora confirmar si es live o no
		contador = 0
		b = None
		c = None
		#print("Entrando")
		
		#time.sleep(0.3)

		while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle
			try:
				#print("Dentro")
				img_aceptar = "aceptar.png"
				#time.sleep(0.2)
				#print("antes")
				b = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9, region=(0,0,559,997))
				#print("luego")
				#print(b, "b")
				#time.sleep(1)
				
				img_confirmar = 'confirmar.png'
				#time.sleep(0.2)
				c = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9, region=(0,0,570,200) )
				#print(c, "c")
				#time.sleep()
				if (b == None) or (c == None):
					#time.sleep(0.2)
					#print("Espere...")
					#print(b)
					#time.sleep(5)
				if contador > 100: # Por si no encuyentra ninguno
					print("Ocurrió un error inesperado")
					#lives.close()
					#exit()

				contador += 1
			except :
				print("Error no se detectó imagen  | Aceptar o live |")
				time.sleep(0.1)

		#time.sleep(0.1)
		print("***************************************************")

		if b!=None: # Si no es live
			print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
			time.sleep(0.2)
			click(b)
			#time.sleep(0.3)
		if c!=None: # Por si es LIVE:
			print ('\a')
			lives = open("lives.txt","a")
			lives.write(x.rstrip()) # escribir en el block
			lives.write("\n")
			lives.close()
			print("N.", linealote ,": "+x.rstrip()+" -------------> Live")
			pyautogui.press('esc')
			flag2 = False # Para que sea live

			#Queriendo guardar el nombre:
			time.sleep(2)

		ultimo = open("registro.txt","w")
		ultimo.write(x.rstrip()) # escribir en el block
		ultimo.write("\n")
		ultimo.close()
			

#lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()