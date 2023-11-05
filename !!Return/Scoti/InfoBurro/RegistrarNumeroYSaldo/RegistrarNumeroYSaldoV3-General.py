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
        "Cookie": "PHPSESSID=rel8shk82uar59oa775pusrut2",
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
def procesar_dni(dni):
    try:
        url = f"http://198.100.155.3/seek/index.php?view=mostrar&cod={dni}"
        response = enviar_solicitud_get(url)
        
        if response.status_code == 200:
            
            # Guardar la respuesta en un archivo de texto
            with open('pagina.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            
            page_content = html.fromstring(response.content)
            
            # Captura el nombre completo
            nombre_completo_element = page_content.xpath('//h2[@class="name"]/text()')
            if nombre_completo_element:
                nombre_completo = nombre_completo_element[0].strip()
                print(f'Nombre completo: {nombre_completo}')
            
            # Extraer "Listado de Números"
            tabla_numeros = page_content.xpath('//h3[contains(text(), "Listado de Numeros")]/following-sibling::div[1]//table/tbody/tr')
            numeros_telefonicos = []
            for fila in tabla_numeros:
                telefono = fila.xpath('.//td[1]/text()')[0]
                operador = fila.xpath('.//td[2]/text()')[0]
                periodo = fila.xpath('.//td[3]/text()')[0]
                activo = fila.xpath('.//td[4]/text()')
                fec_val = fila.xpath('.//td[5]/text()')
                
                numeros_telefonicos.append({
                    'telefono': telefono,
                    'operador': operador,
                    'periodo': periodo,
                    'activo': activo[0] if activo else '',
                    'fec_val': fec_val[0] if fec_val else ''
                })
            
            # Imprimir "Listado de Números"
            print("Listado de Números:")
            for numero in numeros_telefonicos:
                print(numero)
            
            # Extraer "Datos Riesgo"
            riesgo_rows = page_content.xpath("//div[@id='creditos']//table[@class='tablabox rwd_auto']//tr[position()>1]")
            datos_riesgo = []
            for fila in riesgo_rows:
                # Las celdas que contienen los datos de entidad y saldo son las primeras dos de cada fila
                celdas = fila.xpath('.//td[1]//text() | .//td[2]//text()')
                if len(celdas) == 2:
                    entidad = celdas[0].strip()
                    saldo = celdas[1].strip()
                    datos_riesgo.append({'entidad': entidad, 'saldo': saldo})

            # Imprimir "Datos Riesgo"
            print("Datos Riesgo:")
            for dato in datos_riesgo:
                print(f"Entidad: {dato['entidad']}, Saldo: {dato['saldo']}")
            
        else:
            print(f'No se pudo acceder a la página web para DNI {dni}')
    except Exception as e:
        print(f'Error inesperado para DNI {dni}: {str(e)}')



# Leer DNIs desde el archivo
with open('dni.txt', 'r') as archivo_dnis:
    for linea in archivo_dnis:
        # Obtiene los primeros 8 caracteres de la línea actual
        dni = linea[:8]
        print(f'Procesando DNI: {dni}')
        procesar_dni(dni)
        #time.sleep(4)  # Espera 4 segundos antes de procesar el siguiente DNI