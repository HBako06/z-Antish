from PIL import Image
import pytesseract
import cv2
import os
import time

imagePath = "nombre.jpg"
preprocess="thresh"

image= cv2.imread(imagePath)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if(preprocess=="thresh"):
 gray = cv2.threshold(gray,0,25,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif(preprocess=="blur"):
 gray = cv2.medianBblur(gray,3)

filename= "{}.jpg".format(os.getpid())
cv2.imwrite(filename,gray)


try:
 #Creación Archivo
 outfile='extraccion.txt' 
 f = open(outfile,"a") 
 img= Image.open(filename,mode = 'r')
 pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract_OCR\tesseract.exe'
 #pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 text = pytesseract.image_to_string(img)

 print("--------------------------")
 print("LISTO!!")
 print("--------------------------")
 print(text)
 print("--------------------------")

 #Guarda el Texto Reconocido en extraccion.txt
 f.write(text)
 f.close()
 cv2.imshow("Image",image)
 cv2.imshow("Output",gray)
 print("Press <ESC> para salir ")

 while (1):
  if(cv2.waitKey(20) & 0xFF==27):
   break
 cv2.destroyAllWindows()

except IOError as e:
 print("I/O ERROR: "+str(e))
except Exception as e:
 print("OPss!! No se pudo reconocer")
