import pytesseract
from PIL import Image

import cv2
import pytesseract
texto = ""
try:
	imagen = cv2.imread("test.jpg")
	pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
	texto = pytesseract.image_to_string(Image.open("captchas/"+imagen), config="--psm 8 -c tessedir_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz")
	texto = texto.replace("\n\x0c","")
except Exception as e:
	print(texto)
print(texto)