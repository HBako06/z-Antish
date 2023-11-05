import requests
import json
import re #Para separar los nombres y apellidos



def buscar(ApellidoP,ApellidoM,Nombres):

   #dni = "48481980"
   url = "https://www.softwarelion.xyz/api/reniec/reniec-nombres"
   _json = { "paterno": ApellidoP, "materno": ApellidoM, "nombres": Nombres }
   token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNDIxLCJjb3JyZW8iOiJtb2NvOTEyeGRAZ21haWwuY29tIiwiaWF0IjoxNjYyMDkwMTU2fQ.B4p41hmxEvTNb3jCunu1LcS2gDe18FKGw9JbAEA3wdo"
   _headers = { 'Content-Type': 'application/json', 'Authorization': token }

   response = requests.post(url, data=json.dumps(_json), headers=_headers)

   #dataJson = response.json()
   payload = response.json()
   results = payload.get('result',[])

   if results:
    for pok in results:
      todos = pok['dni']
      print(todos)

buscar("mogrovejo ","mendoza","katia maria ")



texNombre = "JAQUELYNE ELBA GALVEZ ZEGARRA"


partido = re.split(r'[;\s]\s*',texNombre)

print(partido[0])
print(partido[1])
print(partido[2])
print(partido[3])


