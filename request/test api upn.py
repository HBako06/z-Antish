import requests
import json



def buscar():

   #dni = "48481980"
   url = "https://upn-api.u-planner.com/api/user-api/getUserList?txt=N00252525"
   #_json = { "dni": dni }
   token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIyLTExLTA3VDIwOjU1OjAxLjIwN1oiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2Njc5NDA5MDF9.4ZMoubl4-UbbGECNIP-Hf4w2H3MpRIvNmPL4x8ElN1U"
   
   #token = "Bearer eyJ0b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpsYldGcGJDSTZJazR3TURJMU5qQXdNVUIxY0c0dWNHVWlMQ0oxYzJWeVNXUWlPak0xTnpjMU1pd2laVzUwWlhKd2NtbHpaVWxrSWpwdWRXeHNMQ0pwWVhRaU9pSXlNREl5TFRFd0xUSTJWREUzT2pBNU9qQTBMalF3TjFvaUxDSnFkR2tpT2lKaE56VXpNR1V5TVMwNE1qRTFMVFE0WmpJdFlqTTROaTB5WVRFM04yWXlORFV5WlRjaUxDSmxlSEFpT2pFMk5qWTRPVEExTkRSOS5lQWR4ZlBZdk9IdzV0QkFFUW13NWVELVRyQzJ0Q0J6Q19jeHJWbF9PS3Q4IiwicmVmcmVzaFRva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxiV0ZwYkNJNklrNHdNREkxTmpBd01VQjFjRzR1Y0dVaUxDSjFjMlZ5U1dRaU9qTTFOemMxTWl3aVpXNTBaWEp3Y21selpVbGtJanB1ZFd4c0xDSnBZWFFpT2lJeU1ESXlMVEV3TFRJMlZERTNPakE1T2pBMExqUXdOMW9pTENKcWRHa2lPaUpoTnpVek1HVXlNUzA0TWpFMUxUUTRaakl0WWpNNE5pMHlZVEUzTjJZeU5EVXlaVGNpTENKbGVIQWlPakUyTmpZNU1EYzRNalI5Lk9KWXRNZVVmSE9jaldfb0xxWXFpV3VJbF9NTnJrNElBMUpsZmpaT2hzeGMifQ=="
   _headers = { 'Authorization': token }

   response = requests.post(url, headers=_headers)

   #dataJson = response.json()

   print(response.text)
   # if(dataJson['success'] == False):
   #   print("No existe")
   #   return

   # persona = dataJson['result']

   # print(persona['paterno'])
   # print( persona['materno'])
   # print(persona['nombres'])
   # print( dni +"-"+ persona['codigoVerificacion'])
   # print( persona['sexo'])

buscar()