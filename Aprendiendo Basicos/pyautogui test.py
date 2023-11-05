import pyautogui
import time

import cv2# pip install opencv-python
import pytesseract
from PIL import Image# pip install Pillow


pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
#myimage = Image.open("G:\\.Programacion\\Pyhton\\Aprendiendo Basicos\\UltimoNombre.png")
#txt = tess.image_to_string(myimage)
image = cv2.imread('test.jpg')
text = pytesseract.image_to_string(image) 

print('Texto: ', text)


#aceptar = "AceptarNaranja.png"
#b = pyautogui.locateOnScreen(aceptar, grayscale=True, confidence=0.9)
#b = pyautogui.position()
def moveyoutube():
	youtu = "youtube.png"
	c = pyautogui.locateCenterOnScreen(youtu, grayscale=True, confidence=0.9)
	print(c)
	pyautogui.moveTo(c)

def pantallazo():
 	#im1 = pyautogui.screenshot()
 	#im = pyautogui.screenshot(region=(0,0, 300, 400))
	#im2 = pyautogui.screenshot('UltimoNombre.png' , region=(1384,467,180,17))
	#Queriendo guardar el nombre:
	pyautogui.screenshot('./Nombres/'+str("4556")+'.jpg' , region=(1384,467,180,17))
	#time.sleep(1)

def pantallazo2():
	filename = './Sentineldnis/UltimoNombre.jpg'
	outfile= 'extraccion.txt'
	f = open(outfile,"a")
	text = str(((pytesseract.image_to_string(Image.open(filename)))))
	text = text.replace('-\n', '')
	f.write(text)
	f.close()

	print("Terminado")
def pasarATexto():
	my_image = Image.open("G:\\.Programacion\\Pyhton\\Aprendiendo Basicos\\UltimoNombre.png")
	txt = tess.image_to_string(my_image)
	print(txt)

#pasarATexto()

#moveyoutube()