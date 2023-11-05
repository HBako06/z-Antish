import pyautogui 
import time
import telegram
#import pytesseract

bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)
# pyautogui.displayMousePosition()

introduceNumero = 1470,576 
numtarj = 1598, 194
continuar = 1774, 818
live_salir = 1382,86
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
time.sleep(1)
print("2")
time.sleep(1)
print("1")
bot.send_message(chat_id=chat_id, text = 'Corriendo bot bcp')
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
				b = pyautogui.locateOnScreen(acept, grayscale=True, confidence=0.9, region=(1357,41,559,997))
				#print(b, "b")
				#time.sleep(1)
				
				confirm = "confirm.png"
				c = pyautogui.locateOnScreen(confirm, grayscale=True, confidence=0.9, region=(1357,41,559,997))
				print(c, "c")
				#time.sleep()
				if (b == None) or (c == None):
					time.sleep(0.2)
					#print("Espere...")
					#print(b)
					#time.sleep(5)
				if contador > 60: # Por si no encuyentra ninguno
					print("Ocurrió un error inesperado")
					lives.close()
					bot.send_message(chat_id=chat_id, text = 'Ocurrio un error, vaya a verlo')
					bot.send_message(chat_id=chat_id, text = 'Se quedo en: '+str(linealote))
					exit()
				contador += 1

			time.sleep(0.3)
			print("***************************************************")

			if b!=None:
				print("N.", linealote ,": "+ x.rstrip() +" -------------> Death")
				click(b)
				#time.sleep(0.5)
			if c!=None: # Por si es LIVE:
				print '\a'
				lives.write(x.rstrip()) # escribir en el block
				lives.write("\n")
				print("N.", linealote ,": "+x.rstrip()+" -------------> Live")

				#Queriendo guardar el nombre:
				time.sleep(0.2)
				#pyautogui.screenshot('./Nombres/'+str(x.rstrip())+'.jpg' , region=(1384,467,316,21))
				pyautogui.screenshot('./Nombres/'+str(linealote)+"++"+str(x.rstrip())+'.png' , region=(1384,467,316,21))
				time.sleep(0.1)
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
	bot.send_message(chat_id=chat_id, text = 'Ocurrio un error, vaya a verlo')
	bot.send_message(chat_id=chat_id, text = 'Se quedo en: '+ str(linealote))

	lives.close()

	#time.sleep(4)
lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
bot.send_message(chat_id=chat_id, text = 'finalizado con exito')
print("*****************")
print("Presione 'Enter' para continuar")
input()
