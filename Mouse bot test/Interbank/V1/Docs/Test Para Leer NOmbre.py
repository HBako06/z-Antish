
import pytesseract
#import cv2
from PIL import Image

text1 = pytesseract.image_to_string(Image.open("nombre.png"), config= '--psm 7 -c tessedit_char_whitelist= abcdefghijkmnlopqrsturstuvwxyz')

print("Text: "+ text1)