import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
#text = pytesseract.image_to_string(Image.open("test2.jpg"), lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
text = pytesseract.image_to_string(Image.open("./Beuvea/test4.jpg"), lang='eng',config='--psm 8 -c tessedir_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz')
#self.__txtCaptcha = pytesseract.image_to_string(Image.open("captchas/"+self.captcha), config="--psm 8 -c tessedir_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz")
