import requests
from lxml import html
import time
import random
import re
# URL de la página web
#url = 'http://158.69.119.209/data/index.php?view=mostrar&cod='
def enviar_solicitud_get(url):
    headers = {
        "Host": "198.100.155.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://198.100.155.3/seek/index.php?view=home",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=3akc1dcrdkio6lk0rpkutr2qk4",
        "Upgrade-Insecure-Requests": "1",
        "Authorization": "Basic ZGV1ZGFjZXJvOk5XQjdYMjIz",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

    response = requests.get(url, headers=headers)
    return response


def extraerSaldosScotiabank(cadena):
    # Encuentra todas las coincidencias de "SCOTIABANK" seguido de un espacio y luego números con decimales
    coincidencias = re.findall(r'SCOTIABANK\s+(\d+\.\d+)', cadena)
    
    # Devuelve la lista de saldos encontrados
    return coincidencias

# Función para procesar el DNI y extraer información
def procesar_dni(dni,archivoTxt):
    try:
        url = f"http://198.100.155.3/seek/index.php?view=mostrar&cod={dni}"
        response = enviar_solicitud_get(url)

        if response.status_code == 200:
            page_content = html.fromstring(response.content)

            # Captura el nombre completo
            nombre_completo_element = page_content.xpath('//h2[@class="name"]/text()')
            if nombre_completo_element:
                nombre_completo = nombre_completo_element[0].strip()
                print(f'Nombre completo: {nombre_completo}')
                with open(archivoTxt, 'a', encoding='utf-8') as resultados_file:
                    resultados_file.write(f'Nombre completo: {nombre_completo}\n')

            # Extraer "Listado de Números"
            tabla_numeros = page_content.xpath('//h3[contains(text(), "Listado de Numeros")]/following-sibling::div[1]//table/tbody/tr')
            print("Listado de Números:")
            for fila in tabla_numeros:
                telefono = fila.xpath('.//td[1]/text()')[0]
                operador = fila.xpath('.//td[2]/text()')[0]
                numero = {'telefono': telefono, 'operador': operador}
                print(numero)
                with open(archivoTxt, 'a', encoding='utf-8') as resultados_file:
                    resultados_file.write(f"{numero}\n")

            # Extraer "Datos Riesgo"
            print("Datos Riesgo:")
            riesgo_rows = page_content.xpath("//div[@id='creditos']//table[@class='tablabox rwd_auto']//tr[position()>1]")
            for fila in riesgo_rows:
                celdas = fila.xpath('.//td[1]//text() | .//td[2]//text()')
                if len(celdas) == 2:
                    entidad = celdas[0].strip()
                    saldo = celdas[1].strip()
                    if "00004 SCOTIABANK PERU S A A" in entidad:
                        dato = {'entidad': entidad, 'saldo': saldo}
                        print(f"Entidad: {dato['entidad']}, Saldo: {dato['saldo']}")
                        with open(archivoTxt, 'a', encoding='utf-8') as resultados_file:
                            resultados_file.write(f"Entidad: {dato['entidad']}, Saldo: {dato['saldo']}\n")
        else:
            print(f'No se pudo acceder a la página web para DNI {dni}')
    except Exception as e:
        print(f'Error inesperado para DNI {dni}: {str(e)}')

# Leer DNIs desde el archivo
with open('dni.txt', 'r') as archivo_dnis:
    for linea in archivo_dnis:
        # Obtiene los primeros 8 caracteres de la línea actual
        dni = linea[:8]
        contra = linea[9:]
        archivoTxt = "ResultadosZeeker.txt"
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n ")
        print(f'Procesando DNI: {dni}')
        
        with open(archivoTxt, 'a', encoding='utf-8') as resultados_file:
            resultados_file.write('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
            resultados_file.write(f'Procesando DNI: {dni} - - > Contra : {contra}')
        
        procesar_dni(dni,archivoTxt)
        
        time.sleep(4)  # Espera 4 segundos antes de procesar el siguiente DNI