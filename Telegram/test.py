import requests
import json

url = 'https://api.municallao.gob.pe/pide/public/v1/reniec/dni/buscar'
r = requests.get(url)

response = r.text
print(response)