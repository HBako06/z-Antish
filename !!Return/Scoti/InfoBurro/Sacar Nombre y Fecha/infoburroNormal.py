import requests
from lxml import html
import time
import random
# URL de la página web
url = 'http://167.114.113.144/buscador/Mostrar-informacion'

# Lee los DNIs desde el archivo datadni.txt
with open('dataBBVAANTIGUA.txt', 'r') as archivo_dnis:
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

                # Utiliza el XPath para extraer el elemento deseado
                dni_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/thead/tr/th[2]')

                # Verifica si los elementos se encontraron
                if dni_element and nombre_completo_element and fecha_nacimiento_element:
                    dni = dni_element[0].text_content().strip()
                    nombre_completo = nombre_completo_element[0].strip()
                    fecha_nacimiento = fecha_nacimiento_element[0].strip()
                    datacom = f'{dni} {nombre_completo} {fecha_nacimiento}'
                    print("Nro: " +str(i) +":   "+ datacom)  # Muestra el resultado en la consola
                    print(f'Consulta para DNI {dni} exitosa')
                    print("/ / /")
                    resultado = open("resultado_dataBBVAANTIGUA.txt", "a")
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

        #if (i + 1) % 17 == 0 and i != 0:
        #    # Espera 1 minuto después de cada lote de 18 solicitudes
        #    print(f'Esperando 1 minuto...')
        #    time.sleep(60)


        break  # Sale del bucle while y pasa al siguiente DNI
    #sleeper()
    time.sleep(4)