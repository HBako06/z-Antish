import pyautogui
import time
import pytesseract
from PIL import Image


#time.sleep(0.5)
#pyautogui.screenshot('CaptchaActual.png' , region=(180,569,173,75))

#limite 362,652
#otr: 362,650
def LentraImagen(Imagen):
	p1 = pytesseract.image_to_string(Imagen, config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
	if p1=="":
		p1 = pytesseract.image_to_string(Imagen, config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
		#print(texto) 
	return p1

Ima1 = pyautogui.screenshot(region=(359,620,34,84)) #588 de altura
Ima2 = pyautogui.screenshot(region=(390,620,32,84))
Ima3 = pyautogui.screenshot(region=(418,620,24,84))
Ima4 = pyautogui.screenshot(region=(442,620,27,84)) #max iquierda
Ima5 = pyautogui.screenshot(region=(465,620,30,84))
Ima6 = pyautogui.screenshot(region=(490,620,29,84))


pyautogui.screenshot('A1.png' , region=(359,620,34,84)) #588 de altura
pyautogui.screenshot('A2.png' , region=(390,620,32,84))
pyautogui.screenshot('A3.png' , region=(418,620,24,84))
pyautogui.screenshot('A4.png' , region=(442,620,27,84)) #max iquierda
pyautogui.screenshot('A5.png' , region=(465,620,30,84))
pyautogui.screenshot('A6.png' , region=(490,620,29,84))


texto = ""

texto = texto + LentraImagen(Ima1).rstrip() + "|"
texto = texto + LentraImagen(Ima2).rstrip() + "|"
texto = texto + LentraImagen(Ima3).rstrip() + "|"
texto = texto + LentraImagen(Ima4).rstrip() + "|"
texto = texto + LentraImagen(Ima5).rstrip() + "|"
texto = texto + LentraImagen(Ima6).rstrip() + "|"

texto = texto.replace(" ","")

print("-------------------------")
print("Texto: "+ texto)
print("-------------------------")
texto = texto + "iiiii"





