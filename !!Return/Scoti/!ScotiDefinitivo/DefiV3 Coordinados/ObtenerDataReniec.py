import requests

# Función para obtener los datos de un DNI y devolver la cadena formateada
def obtener_datos_dni(dni):
    dni = dni.rstrip()
    if len(dni) == 8:
        api_url = 'https://jackelinos.azurewebsites.net/get_user_data'
        # Crea el cuerpo JSON de la solicitud POST
        payload = {'dni': dni}

        # Realiza la solicitud POST a la API
        response = requests.post(api_url, json=payload)

        try:
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

                    # Reemplaza ├æ por "N" en los campos de texto
                    NOMBRES = NOMBRES.replace('├æ', 'N')
                    AP_PAT = AP_PAT.replace('├æ', 'N')
                    AP_MAT = AP_MAT.replace('├æ', 'N')

                    # Verifica si los campos están vacíos y los rellena con "None"
                    if not NOMBRES:
                        NOMBRES = "None"
                    if not AP_PAT:
                        AP_PAT = "None"
                    if not AP_MAT:
                        AP_MAT = "None"

                    # Formatea la cadena y la devuelve
                    return f'{DNI}|{NOMBRES}|{AP_MAT}|{AP_PAT}|{FECHA_NAC}'
                else:
                    return f'ERROR'
            else:
                return f'ERROR'
        except:
            return 'ERROR'
    else:
        return f'ERROR'

#print(obtener_datos_dni('46786554'))
