from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

image = cv2.imread('ejem.png')

text = pytesseract.image_to_string(image)
print(text)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()