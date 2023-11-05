import requests
import json

def obtener_Fila_Cantidad(proceso):
    try:
        api_url = 'https://jackelinos.azurewebsites.net/obtener_total_filas_por_procesado'

        data = {
            'proceso': proceso  # Aquí define el proceso que necesitas enviar
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        resultado = requests.post(api_url, data=json_data, headers=headers)

        if resultado.status_code == 200:
            cantidad_info = resultado.json()
            cantidad = cantidad_info.get("cantidad")

            return cantidad
        else:
            print("Error en la solicitud a la API.")
            return None

        print("Status Code:", resultado.status_code)
        print("Response Content:", resultado.content)

    except Exception as e:
        print("Error durante la solicitud a la API:", str(e))
        return None

print(obtener_Fila_Cantidad(10))