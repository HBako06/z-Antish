import requests
from lxml import html
import random
import threading
import queue

# Función para procesar un DNI
def procesar_dni(dni, url, proxies, headers):
    while True:
        try:
            proxy = random.choice(proxies)
            data = {'dni': dni}

            response = requests.post(url, data=data, headers=headers, proxies={'http': proxy, 'https': proxy})

            if response.status_code == 200:
                page_content = html.fromstring(response.text)
                dni_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/thead/tr/th[2]')

                if dni_element:
                    dni = dni_element[0].text_content().strip()
                    nombre_completo_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/div/h5/text()')
                    fecha_nacimiento_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/tbody/tr[1]/td[2]/text()')

                    if nombre_completo_element and fecha_nacimiento_element:
                        nombre_completo = nombre_completo_element[0].strip()
                        fecha_nacimiento = fecha_nacimiento_element[0].strip()
                        datacom = f'{dni} {nombre_completo} {fecha_nacimiento}'
                        print(f'Consulta para DNI {dni} exitosa')
                        print(datacom)
                        print("/ / /")
                        #'''
                        resultado = open("resultado.txt", "a")
                        resultado.write(datacom)
                        resultado.write("\n")
                        resultado.close()
                        #'''
                    else:
                        print(f'DNI {dni} no encontrado o datos incompletos')
                else:
                    print(f'DNI {dni} no encontrado')

                break  # Sale del bucle while si la consulta es exitosa

            else:
                print(f'No se pudo acceder a la página web para DNI {dni}')
                # Cambia el proxy en el próximo intento
                proxies.remove(proxy)
        except Exception as e:
            print(f'Error inesperado para DNI {dni}: {str(e)}')

# URL de la página web
url = 'http://167.114.113.144/buscador/Mostrar-informacion'

# Lee los DNIs desde el archivo datadni.txt
with open('datadni.txt', 'r') as archivo_dnis:
    dnis = archivo_dnis.read().splitlines()

# Configura los encabezados para simular una solicitud de navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Lee los proxies desde el archivo proxies.txt
with open('proxies.txt', 'r') as archivo_proxies:
    proxies = archivo_proxies.read().splitlines()

# Crea una cola para los DNIs a procesar
cola_dnis = queue.Queue()

# Agrega los DNIs a la cola
for dni in dnis:
    cola_dnis.put(dni)

# Crea y ejecuta múltiples hilos para procesar los DNIs
num_hilos = 15  # Puedes ajustar este número según tu preferencia
hilos = []

for _ in range(num_hilos):
    hilo = threading.Thread(target=lambda: procesar_dni(cola_dnis.get(), url, proxies.copy(), headers))
    hilo.start()
    hilos.append(hilo)

# Espera a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Proceso completo.")
