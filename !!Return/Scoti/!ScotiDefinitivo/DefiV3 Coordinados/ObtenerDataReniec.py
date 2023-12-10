import requests
import re  # Importamos la librería de expresiones regulares

# Función para filtrar solo caracteres del abecedario inglés
def filtrar_caracteres(texto):
        # Mantener solo letras del abecedario inglés y espacios
    texto_filtrado = re.sub(r'[^a-zA-Z ]', '', texto)
    return texto_filtrado

# Función para obtener los datos de un DNI y devolver la cadena formateada
def obtener_datos_dni(dni):
    dni = dni.rstrip()
    if len(dni) == 8:
        api_url = 'https://jackelinos.azurewebsites.net/get_user_data'
        payload = {'dni': dni}
        response = requests.post(api_url, json=payload)

        try:
            if response.status_code == 200:
                user_data_list = response.json()
                if user_data_list:
                    user_data = user_data_list[0]
                    DNI = user_data.get('DNI', '')
                    NOMBRES = filtrar_caracteres(user_data.get('NOMBRES', ''))
                    AP_PAT = filtrar_caracteres(user_data.get('AP_PAT', ''))
                    AP_MAT = filtrar_caracteres(user_data.get('AP_MAT', ''))
                    FECHA_NAC = user_data.get('FECHA_NAC', '')

                    if not NOMBRES:
                        NOMBRES = "None"
                    if not AP_PAT:
                        AP_PAT = "None"
                    if not AP_MAT:
                        AP_MAT = "None"

                    return f'{DNI}|{NOMBRES}|{AP_MAT}|{AP_PAT}|{FECHA_NAC}'
                else:
                    return 'ERROR'
            else:
                return 'ERROR'
        except:
            return 'ERROR'
    else:
        return 'ERROR'

# Ejemplo de uso
print(obtener_datos_dni('46786550'))

