import requests
from lxml import html

# URL de la página web
url = 'http://167.114.113.144/buscador/Mostrar-informacion'

# Parámetros que quieres enviar en formato form url encoded
data = {'dni': '08163569'}

# Realiza la solicitud POST
response = requests.post(url, data=data)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Parsea el contenido HTML de la respuesta
    page_content = html.fromstring(response.text)
    
    # Utiliza el XPath para extraer el nombre completo
    nombre_completo_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/div/h5/text()')
    
    # Utiliza el XPath para extraer la fecha de nacimiento
    fecha_nacimiento_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/tbody/tr[1]/td[2]/text()')
    
    # Utiliza el XPath para extraer el elemento deseado
    dni_element = page_content.xpath('//*[@id="js-page-content"]/div[2]/div[1]/div[1]/div/div/table/thead/tr/th[2]')
    
    # Verifica si los elementos se encontraron
    if dni_element:
        dni = dni_element[0].text_content().strip()
        print('DNI:', dni)
    else:
        print('DNI no encontrado')
    
    if nombre_completo_element:
        nombre_completo = nombre_completo_element[0].strip()
        print('Nombre completo:', nombre_completo)
    else:
        print('Nombre completo no encontrado')
    
    if fecha_nacimiento_element:
        fecha_nacimiento = fecha_nacimiento_element[0].strip()
        print('Fecha de nacimiento:', fecha_nacimiento)
    else:
        print('Fecha de nacimiento no encontrada')
else:
    print('No se pudo acceder a la página web')
print(response.status_code)
