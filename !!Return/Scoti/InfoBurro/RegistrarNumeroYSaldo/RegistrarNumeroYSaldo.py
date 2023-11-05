import requests
from lxml import html
import time
import random
import re
# URL de la página web
url = 'http://167.114.113.144/buscador/Mostrar-informacion'

def extraerNumeros(cadena):
    # Encuentra todas las coincidencias de números de 9 dígitos seguidos por cualquier letra
    coincidencias = re.findall(r'(\d{9})([a-zA-Z])', cadena)
    
    # Lista para almacenar los resultados
    resultados = []

    # Itera sobre las coincidencias y muestra el número y el operador
    for numero, letra in coincidencias:
        operador = letra.lower()  # Convierte la letra a minúsculas para evitar problemas de mayúsculas/minúsculas
        
        # Mapea letras a nombres de operadores
        if operador == 'm':
            operador = 'movistar'
        elif operador == 'e':
            operador = 'entel'
        elif operador == 'c':
            operador = 'claro'
        else:
            operador = 'desconocido'
        
        # Agrega el número y el operador a la lista de resultados
        resultados.append(f'{numero} {operador}')
    
    # Devuelve la lista de resultados
    return resultados



# Lee los DNIs desde el archivo datadni.txt
with open('dni.txt', 'r') as archivo_dnis:
    dnis = archivo_dnis.read().splitlines()

# Realiza las consultas para cada DNI
for i, dni in enumerate(dnis):
    while True:
        try:
            # Parámetros que quieres enviar en formato form url encoded
            data = {'dni': dni}

            # Realiza la solicitud POST
            response = requests.post(url, data=data)

            # Verifica si la solicitud fue exitosa
            if response.status_code == 200:
                # Parsea el contenido HTML de la respuesta
                page_content = html.fromstring(response.text)

                # Utiliza los XPath para extraer los datos
                nombre_completo_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/div/h5/text()')
                fecha_nacimiento_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/tbody/tr[1]/td[2]/text()')
                telefonos_element = page_content.xpath('//*[@id="msg-01"]/div[2]')

                # Utiliza el XPath para extraer el DNI
                dni_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/thead/tr/th[2]')

                saldo_element = page_content.xpath('//*[@id="tab_borders_icons-4"]/table[3]/tbody')

                # Verifica si los elementos se encontraron
                if dni_element and nombre_completo_element and fecha_nacimiento_element:
                    dni = dni_element[0].text_content().strip()
                    nombre_completo = re.sub(r'[^a-zA-Z\s]', '', nombre_completo_element[0].strip())
                    fecha_nacimiento = fecha_nacimiento_element[0].strip()
                    #saldo = saldo_element[0].text_content().strip()

                    # Utiliza text_content() para extraer el texto del elemento y reemplaza espacios y saltos de línea con una cadena vacía
                    telefonos = telefonos_element[0].text_content().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').strip()
                    saldo = saldo_element[0].text_content().replace(' ', '').replace('', '').replace('\n', '').replace('\t', '').strip()
                    saldo_list  = saldo.split('\r')


                    # Filtra las entradas que contienen 'SCOTIABANKPERUSAA' y su saldo correspondiente
                    scotiabank_entries = []
                    i = 0
                    while i < len(saldo_list):
                        if saldo_list[i] == 'SCOTIABANKPERUSAA':
                            # Si encuentra 'SCOTIABANKPERUSAA', añade la entrada siguiente (el saldo) a la lista
                            scotiabank_entries.append(f'{saldo_list[i]} {saldo_list[i + 1]}')
                            # Avanza dos posiciones para saltar la entrada actual y pasar a la siguiente
                            i += 2
                        else:
                            # Si no es 'SCOTIABANKPERUSAA', pasa a la siguiente entrada
                            i += 1


                    for entry in scotiabank_entries:
                        print(entry)
                    
                    print(extraerNumeros(telefonos))

                    #print(saldo)
                    #input('s')

                    datacom = f'{dni} {nombre_completo} {fecha_nacimiento}'
                    print("Nro: " +str(i) +":   "+ datacom)  # Muestra el resultado en la consola
                    print(f'Consulta para DNI {dni} exitosa')
                    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
                    resultado = open("resultado.txt", "a")
                    resultado.write(datacom)  # escribir en el block
                    resultado.write("\n")
                    resultado.close()

                else:
                    print(f'DNI {dni} no encontrado o datos incompletos')
            else:
                print(f'No se pudo acceder a la página web para DNI {dni}')

        except requests.exceptions.Timeout:
            # Captura el error de tiempo de espera y espera 5 segundos antes de volver a intentarlo
            print(f'Error de tiempo de espera para DNI {dni}. Reintentando en 5 segundos...')
            time.sleep(5)
            continue

        except Exception as e:
            print(f'Error inesperado para DNI {dni}: {str(e)}')


        break  # Sale del bucle while y pasa al siguiente DNI
    #sleeper()
    time.sleep(4)