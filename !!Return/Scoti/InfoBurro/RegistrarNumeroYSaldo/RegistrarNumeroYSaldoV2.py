import requests
from lxml import html
import time
import random
import re
# URL de la página web
#url = 'http://158.69.119.209/data/index.php?view=mostrar&cod='

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
        elif operador == 'b':
            operador = 'bitel'
        else:
            operador = 'desconocido'
        
        # Agrega el número y el operador a la lista de resultados
        resultados.append(f'{numero} {operador}')
    
    # Devuelve la lista de resultados
    return resultados

def extraerSaldosScotiabank(cadena):
    # Encuentra todas las coincidencias de "SCOTIABANK" seguido de un espacio y luego números con decimales
    coincidencias = re.findall(r'SCOTIABANK\s+(\d+\.\d+)', cadena)
    
    # Devuelve la lista de saldos encontrados
    return coincidencias

# Realiza las consultas para cada DNI
with open('dni.txt', 'r') as archivo_dnis:
    for linea in archivo_dnis:
        # Obtiene los primeros 8 caracteres de la línea actual
        dni = linea[:8]

        while True:
            try:
                # Parámetros que quieres enviar en formato form url encoded
                url = "http://198.100.155.3/seek/index.php?view=mostrar&cod=" + dni
                print("\n")
                print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")
                print(linea)
                # Realiza la solicitud POST
                response = requests.get(url)
                #print(response)
                
                # Verifica si la solicitud fue exitosa
                if response.status_code == 200:
                    # Parsea el contenido HTML de la respuesta
                    page_content = html.fromstring(response.text)

                    resultadoo = open("resultadoo1015.txt","a")
                    resultadoo.write("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    resultadoo.write("\n")
                    resultadoo.write(str(linea))

                    # Utiliza los XPath para extraer los datos
                    nombre_completo_element = page_content.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/h2')
                    telefonos_element = page_content.xpath('//*[@id="telefonos"]/div/div[2]/div[3]/table/tbody')
                    # Utiliza XPath para obtener las filas de la tabla de saldos de SCOTIABANK
                    filas_saldos_scotiabank = page_content.xpath('//*[@id="creditos"]/div/div[2]/div[4]/table/tbody/tr[contains(td[1], "SCOTIABANK PERU S A A")]') 
                    
                    # Verifica si los elementos se encontraron
                    if nombre_completo_element:
                        nombre_completo = nombre_completo_element[0].text_content().strip()
                        telefonos = telefonos_element[0].text_content().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').strip()

                        # Utiliza XPath para obtener las filas de la tabla de saldos de SCOTIABANK
                        filas_saldos_scotiabank = page_content.xpath('//*[@id="creditos"]/div/div[2]/div[4]/table/tbody/tr[contains(td[1], "SCOTIABANK PERU S A A")]')

                        # Itera sobre las filas y extrae los datos
                        for fila in filas_saldos_scotiabank:
                            banco = fila.xpath('td[1]/text()')[0].strip()
                            saldo = fila.xpath('td[2]/text()')[0].strip()
                            print(f'{banco} - Saldo: {saldo}')
                            resultadoo.write(f'{banco} - Saldo: {saldo}')
                            resultadoo.write("\n")

                        telefonitostotal = extraerNumeros(telefonos)
                        print(telefonitostotal)
                        resultadoo.write(str(telefonitostotal))
                        #input()
                    else:
                        print(f'DNI {dni} no encontrado o datos incompletos')
                else:
                    print(f'No se pudo acceder a la página web para DNI {dni}')
                
                 
                resultadoo.write("\n")
                resultadoo.write("\n")
                resultadoo.close()

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