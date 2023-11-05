import pyautogui 
import time

b = None
img_confirmar = 'confirmar.png'

while (True):# Un " Y " poqe si no cumple 1 se rompe el bucle
	b = pyautogui.locateOnScreen(img_confirmar,grayscale=True,confidence=0.9)

	if (b == None):
		time.sleep(1)
	if b != None:
		pyautogui.click(1292,331)
