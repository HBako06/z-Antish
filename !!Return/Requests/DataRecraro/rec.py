import requests

dni = "46882212"  # DNI que deseas utilizar

urls = [
    f'http://sdv.midis.gob.pe/Sis_Comunidad/Comunidad/AjaxReniecDatosPersona?In_DNI={dni}',
    f'http://sdv.midis.gob.pe/Sis_IDM_Admin/Persona/GetRENIEC?iCodAplicacion=27&iIdTipDocumento=1&vNroDocumento={dni}'
]

headers = {
    'Accept': '/',
    'Host': 'sdv.midis.gob.pe',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
}

for url in urls:
    response = requests.get(url, headers=headers)
    # Puedes hacer algo con la respuesta si es necesario
    # Por ejemplo, imprimir el contenido de la respuesta:
    print(response.text)
