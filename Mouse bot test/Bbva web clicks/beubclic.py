import os #Borrar consola
import pytesseract
from PIL import Image
from collections import Counter

import pyautogui 
import time
import datetime
from openpyxl import load_workbook # excel

#import cv2
#import telegram

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
#text = pytesseract.image_to_string(Image.open("test5.png"),config='--psm 10 --oem 3 -c tessedit_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz')


#Datos ingresados es incorrecto Y limite superado:
Pos_NumeroTarje = 101,407
Pos_ClaveCajero = 170,546
Pos_CodigoImagen = 228,682
exe = 708,16

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614


def click (pos,click = 1 ):
	pyautogui.moveTo(pos)
	pyautogui.click(clicks=click)

def borrar(i):
	for i in range (1,i):
		pyautogui.press('backspace')


#Nombre del excel
filesheet = "./Felizanio22.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name('Hoja1')
wb.close()

os.system ("cls") 
CantidadInicial = input("Escriba desde que numero iniciará:  ")
CantidadInicial = (int(CantidadInicial))
CantidadFinal = input("Escriba desde que numero finalizará:  ")
CantidadFinal = (int(CantidadFinal))

#archivo.write("Dnis \n")

#Rango de los Excels que se ejecutarán :D


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
print()
for i in range(CantidadInicial,CantidadFinal):
	tarjeta, fecha1, fecha2,fecha3,fecha4 = nombres[f'A{i}:E{i}'][0]

	print("N°.", i)

	#Comenzando con la tarjeta
	click(Pos_NumeroTarje,click=2)
	borrar(2)
	time.sleep(0.3)
	click(Pos_NumeroTarje)
	
	print(tarjeta.value)
	pyautogui.typewrite(tarjeta.value)

	#Futuro While-----------------------------------------
	j = 0
	#for j in range(j,4):
	while j < 4:
		j = j + 1
		#time.sleep(0.1)
		#print("borrado")

		click(Pos_ClaveCajero)
		borrar(5)
		click(Pos_ClaveCajero)

		if fecha1.value=="-":
			print("No tiene clave")
			break;
		

		if j == 1:
			print(fecha1.value)
			pyautogui.typewrite(fecha1.value)
		if j == 2:
			print(fecha2.value)
			pyautogui.typewrite(fecha2.value)
		if j == 3:
			print(fecha3.value)
			pyautogui.typewrite(fecha3.value)
		if j == 4:
			print(fecha4.value)
			pyautogui.typewrite(fecha4.value)
		


		click(Pos_CodigoImagen)
		borrar(7)


		pyautogui.screenshot('captcha.jpg' , region=(181,560,171,76))

		time.sleep(0.2)

		text = pytesseract.image_to_string(Image.open("test2.jpg"), lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz')
		#text = pytesseract.image_to_string(Image.open("captcha.jpg"),config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6")
		#text = pytesseract.image_to_string(Image.open("captcha.jpg"), lang='eng', boxes=False,config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')
		time.sleep(0.2)
		'''
		#textlimpio = text.strip()
		text = text.replace(' ','')
		text = text.replace("'", "")
		text = text.replace('"', '')
		text = text.replace(".","")
		text = text.replace(' ° ','')
		text = text.replace('°','')
		text = text.replace('_','')
		text = text.replace('-','')
		text = text.strip()
		'''
		print("++++++++")
		print("Antiguo: "+text)
		
		text = text.replace(' ','')
		text = text + "aaaaaa"
		
		print(text)
		print("++++++++")

		click (Pos_CodigoImagen)
		pyautogui.typewrite(text)
		time.sleep(0.2)
		pyautogui.press('enter')

		time.sleep(1)

		'''
		r = None
		invalido = "error.png"
		time.sleep(1.5)
		r = pyautogui.locateOnScreen(invalido, grayscale=True, confidence=0.9, region=(440,593,85,152))
		#print("r",r)
		if r!=None:
			print("retrocediendo")
			j = j-1	
		'''

		rojo =  False
		#try:
		#Color: 464,685(252,223,223)
		rojo = pyautogui.pixelMatchesColor(464,685,(252,223,223))
		time.sleep(0.1)
		if (rojo is True):
			print("retrocediendo")
			j = j-1	
		if(rojo is False):
			print("Acertado! next")


		#print("...")

		time.sleep(0.5)
		
		'''
		print("continuar??")
		click(exe)
		input()
		print("\n")
		#reconfirnar =input("Retroceder?")
		#if reconfirnar == "si": # por si me equivoco
		'''
			

		

	os.system ("cls") 
	print("Next")




	







