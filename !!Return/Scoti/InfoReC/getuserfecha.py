import requests
import concurrent.futures
import threading
import re

# Bloqueo para controlar el acceso a las operaciones de escritura
lock = threading.Lock()

# Expresión regular para aceptar solo letras del alfabeto de la A a la Z
regex_pattern = re.compile(r'[a-zA-Z ]+')

# Función para obtener los datos de un DNI
def obtener_datos_dni(i, dni):
    for intento in range(10):  # Intenta un máximo de 5 veces
        try:
            # Crea el cuerpo JSON de la solicitud POST
            payload = {'dni': dni}

            # Realiza la solicitud POST a la API
            response = requests.post(api_url, json=payload)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Verifica si la respuesta contiene datos
                user_data_list = response.json()
                if user_data_list:
                    user_data = user_data_list[0]  # Obtiene la información del usuario

                    # Extrae los campos necesarios
                    DNI = user_data.get('DNI', '')
                    NOMBRES = user_data.get('NOMBRES', '')
                    AP_PAT = user_data.get('AP_PAT', '')
                    AP_MAT = user_data.get('AP_MAT', '')
                    FECHA_NAC = user_data.get('FECHA_NAC', '')

                    # Filtra solo letras del alfabeto de la A a la Z
                    NOMBRES = ''.join(regex_pattern.findall(NOMBRES))
                    AP_PAT = ''.join(regex_pattern.findall(AP_PAT))
                    AP_MAT = ''.join(regex_pattern.findall(AP_MAT))


                    # Bloquea el acceso a las operaciones de escritura
                    with lock:
                        # Imprime la información en la consola con el número de iteración
                        print(f'N° {i} | {DNI} | {NOMBRES} | {AP_MAT} | {AP_PAT} | {FECHA_NAC}')

                        # Escribe los resultados en el archivo resultados.txt con codificación UTF-8
                        with open('resultados.txt', 'a', encoding='utf-8') as resultados_file:
                            resultados_file.write(f'{DNI}|{NOMBRES}|{AP_MAT}|{AP_PAT}|{FECHA_NAC}\n')
                    break  # Sale del bucle si la solicitud fue exitosa
                else:
                    # La respuesta está vacía, intenta nuevamente
                    continue
            else:
                # Bloquea el acceso a las operaciones de escritura
                #with lock:
                # Escribe el error en la consola y en el archivo resultados.txt con codificación UTF-8
                print(f'Error al obtener datos para el DNI {dni} (Intento {intento + 1})')
                #with open('resultados.txt', 'a', encoding='utf-8') as resultados_file:
                #    resultados_file.write(f'Error al obtener datos para el DNI {dni} (Intento {intento + 1})\n')
        except Exception as e:
            # Bloquea el acceso a las operaciones de escritura
            #with lock:
            # Escribe el error en la consola y en el archivo resultados.txt con codificación UTF-8
            print(f'Error en la solicitud para el DNI {dni} (Intento {intento + 1})')
            #with open('resultados.txt', 'a', encoding='utf-8') as resultados_file:
                #resultados_file.write(f'Error en la solicitud para el DNI {dni} (Intento {intento + 1}): {str(e)}\n')

if __name__ == '__main__':
    # Ruta del archivo DNI.txt
    dni_file_path = 'dni.txt'
    max_workers = 10
    # URL de la API
    api_url = 'https://jackelinos.azurewebsites.net/get_user_data'

    # Lista para almacenar las líneas de DNI del archivo
    dni_list = []

    # Abre el archivo DNI.txt y lee las líneas
    with open(dni_file_path, 'r') as file:
        dni_list = [line.strip() for line in file]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i, dni in enumerate(dni_list, start=1):
            executor.submit(obtener_datos_dni, i, dni)
