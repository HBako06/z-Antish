import pyautogui 
import time
from pytesseract import pytesseract
from PIL import Image
from printy import printy
import datetime


#Define path to tessaract.exe
path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


numtarj = 808,330
continuar1 = 967,971
monto = 749,498
rojoabajo = 830,962
rojoabajo2 = 957,957



def click (pos,click = 1 ):
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=click)
def borrar(i):
    for i in range (1,i):
        pyautogui.press('backspace')
def ingresarACuenta():
    time.sleep(0.5)
    pyautogui.click(771,361)
    time.sleep(0.5)
    pyautogui.typewrite('Jacob2127') # Jacob2127 Elizabet2 Crackmovi600
    time.sleep(0.3)
    pyautogui.click(959,562) # click iniciar
    time.sleep(13) # esperar (12)
    pyautogui.click(1091,174) # quiero
    time.sleep(1)
    pyautogui.click(797,333) # pagar
    time.sleep(1)
    pyautogui.click(856,343) # tarjeta de credito
    time.sleep(3.2) #(5)
    pyautogui.click(769,218) # mostrar bancos
    time.sleep(0.4)
    pyautogui.click(759,516) # click en bbva 
    time.sleep(0.4)
def reinicio():
    time.sleep(0.5)
    pyautogui.click(778,26)
    time.sleep(1)
    pyautogui.click(1149,218)

    time.sleep(5) #(7)
    ingresarACuenta()
    time.sleep(2)

#.------------------------------------------
printy("po po po po po po po po po po po po po po po po po","n")
print("**************************************************")

#teequiste = input("Archivo txt:  ")
logeopreg = input(" ¿logeo? si/no:  ")

print("**************************************************")
print("\n")
#print("Presione 'Enter' para continuar")
#input()

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
print ('\a')

linealote= 0
flag2 = True
contadorReinicio = 0

if logeopreg=="si":
    ingresarACuenta()
#with open ('./lotes/'+teequiste+'.txt') as texto:
with open ('./lote.txt') as texto:
    for x in texto:
        #print("Dentro")
        linealote += 1

        contadorReinicio += 1
        if(contadorReinicio > 70):
            reinicio()
            contadorReinicio = 0

        #Comprobar si abajo está rojo
        pixelrojoContinuar = False
        while pixelrojoContinuar is False:
            time.sleep(0.4)
            pyautogui.doubleClick(numtarj)
            #time.sleep(0.1)
            time.sleep(0.5)
            pyautogui.typewrite(str(x), interval=0.03)
            time.sleep(0.3)
            pixelrojoContinuar = pyautogui.pixelMatchesColor(1137,968,(236,17,26)) 
            print(f"Pixel rojo: {pixelrojoContinuar}")
            pyautogui.click(continuar1) # click en continuar
            time.sleep(0.5)
        
        print(f"Pixel rojo afuera: {pixelrojoContinuar}")
        
        pyautogui.click(749,498) # monto en soles
        pyautogui.typewrite('1')
  
        pyautogui.click(rojoabajo)
        time.sleep(0.4)
        #time.sleep(1)
        contador = 0
        b = None
        c = None
        img_aceptar = "aceptar.png"
        img_confirmar = 'confirmar.png'
        while (b is None) and (c is None):# Un " Y " poqe si no cumple 1 se rompe el bucle

            #print("Dentro")
            #time.sleep(0.1)
            #rojo
            #blanco = pyautogui.pixelMatchesColor(462,993,(236,17,26))
            blanco = pyautogui.pixelMatchesColor(1055,882,(255,255,255)) 
            #print(blanco)
            if (blanco is True):
                time.sleep(0.3) # esperar un rato el continuarRojo
                pyautogui.click(rojoabajo2)

            #img_aceptar = "aceptar.png"
            #time.sleep(0.2)
            #print("antes")
            b = pyautogui.locateOnScreen(img_aceptar,grayscale=True,confidence=0.9, region=(1010,566,1222,686))
            #print("luego")
            #print(b, "b")
            #time.sleep(1)
            
            #img_confirmar = 'confirmar.png'
            #time.sleep(0.2)
            c = pyautogui.locateOnScreen(img_confirmar, grayscale=True, confidence=0.9, region=(666,58,954,164))
            #print(c, "c")
            #time.sleep()
            #if (b == None) or (c == None):
                #time.sleep(0.2)
                #print("Espere...")
                #print(b)
                #time.sleep(5)
            if contador > 200: # Por si no encuyentra ninguno
                #time.sleep(0.03)
                print("Ocurrió un error inesperado")
                #lives.close()
                input("Presione enter si ya lo solucionó")    #  es una opcion desactivada
                contador = 1
                

            contador += 1
            time.sleep(0.1)


        #print("fin test")
        #input()

        #time.sleep(0.1)
        print("***************************************************")
        fechaActual = datetime.datetime.now()

        if b!=None: # Si no es live
            #fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')
            #print(fechaActual2, " | ","N. ", linealote ,": "+x.rstrip()+ "  -------------> Death")
            printy(f"N. {linealote} : {x.rstrip()} -------------> [rI]DEATH@")
            #time.sleep(0.2)
            click(b) # click en aceptar de la imagen 
            time.sleep(0.4)
            pyautogui.press('esc')
            #time.sleep(0.3)
        if c!=None: # Por si es LIVE:
            print ('\a')
            
            im = pyautogui.screenshot("test.png",region=(811,413,382,35))

            text: str = pytesseract.image_to_string(im)
            #print(f'El nombre es: {text}')

            lives = open("lives.txt","a")
            lives.write(x.rstrip()+"    "+text.rstrip()) # escribir en el block
            lives.write("\n")
            lives.close()

            #fechaActual2 = datetime.datetime.strftime(fechaActual,'%H:%M:%S')

            #print(fechaActual2, " | ","N. ", linealote ,": "+x.rstrip()+ "  |  " +text.rstrip()+ "  -------------> Live")
            printy(f"N. {linealote} :{x.rstrip() + ' '  + text.rstrip()} -------------> [n]Live@")
            
            pyautogui.press('esc')
            time.sleep(0.2)
            pyautogui.press('esc')
            flag2 = False # Para que sea live


        ultimo = open("registro.txt","w")
        #ultimo.write("El ultimo calado de lote es: ")
        ultimo.write(x.rstrip()) # escribir en el block
        ultimo.write("\n")
        ultimo.close()      

#lives.close()
print("Programa finalizado")
print("se quedo en la linea: ", linealote)
time.sleep(1)
print("*****************")
print("Presione 'Enter' para Finalizar")
input()
295177722


