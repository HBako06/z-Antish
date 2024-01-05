import requests

# URL y headers para la solicitud de recarga
reload_url = "https://www.google.com/recaptcha/api2/reload?k=6Ld7wUcnAAAAADPzTvPWOAEswBzJfqyNErkKIOhQ"
reload_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-419,es-US;q=0.9,es-PE;q=0.8,es;q=0.7,en;q=0.6,pt;q=0.5",
    "Content-Type": "application/x-protobuffer",  # Puedes necesitar ajustar esto según la implementación de reCAPTCHA
    "Dnt": "1",
    "Origin": "https://www.google.com",
    "Sec-Ch-Ua": '"Not=A?Brand";v="99", "Chromium";v="118"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Realiza la solicitud de recarga
reload_response = requests.post(reload_url, headers=reload_headers)
print(reload_response.status_code)
print(reload_response.text)

# Verifica si la solicitud fue exitosa
if reload_response.status_code == 200:
    try:
        # Intenta extraer el token de la respuesta
        token = reload_response.json()[13]
        print("Token de recarga obtenido correctamente:", token)
    except (ValueError, IndexError):
        print("Error al obtener el token de recarga.")
        token = None

    if token:
        # URL y headers para la solicitud BuscarDocumento
        buscar_documento_url = "http://infoburo.com.pe/Score/BuscarDocumento"
        buscar_documento_headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "es-419,es-US;q=0.9,es-PE;q=0.8,es;q=0.7,en;q=0.6,pt;q=0.5",
            "Connection": "keep-alive",
            "Content-Length": "1643",
            "Content-Type": "application/json",
            "Cookie": "_ga=GA1.1.2122346607.1704435343; ASP.NET_SessionId=vqjqfnnvinudxgdt02dyutpa; _ga_B633F8HCWF=GS1.1.1704435342.1.1.1704435457.0.0.0",
            "Dnt": "1",
            "Host": "infoburo.com.pe",
            "Origin": "http://infoburo.com.pe",
            "Referer": "http://infoburo.com.pe/",
            "Sec-Gpc": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        # Carga útil para la solicitud BuscarDocumento
        payload = {
            "dni": "07316480",
            "token": token
        }

        # Realiza la solicitud BuscarDocumento
        buscar_documento_response = requests.post(buscar_documento_url, headers=buscar_documento_headers, json=payload)

        # Imprime la respuesta
        print(buscar_documento_response.status_code)
        print(buscar_documento_response.text)
else:
    print("Error al obtener el token de recarga.")
