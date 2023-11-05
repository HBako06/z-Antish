'''import requests
import json
import base64 as b64

#admin.suite@u-uplanner.com | administrador
def buscarId():
  #dni = "n00100020"
  #id = "00100017"
  #id = id[-6:]
  #url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt=n00{str(id)}"
  #url = "https://mimundo.upn.edu.pe/api/participants?courseId=FISI1111&courseSection=2224345751&period=222434"
  url = "https://mimundo.upn.edu.pe/api/profileuserinfo"
  token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9eyJzdWIiOiJuMDAyNTYwMDEiLCJpc3MiOiJodHRwczovL21pbXVuZG8udXBuLmVkdS5wZS9zYW1sMi9hY3MiLCJpYXQiOjE2Njc4OTA0MjAsImV4cCI6MTY2NzkwMTIyMCwibmJmIjowLCJqdGkiOiI4cEFBTFNUNjRFclZzZ1A1In0._g71lCdLmyGOpeyPf9IKpbAQD155yy-SpHWSMDK74mM"
  _headers = {'Authorization': token }


  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  print(response)
  print(dataJson)
  #persona = dataJson['data']

  #print(dataJson)
  #print(persona)
  #print(persona)|
  #print("userId: ",persona[0]['userId'])
  #print("userName: ",persona[0]['userName'])
  #print("userCode: ",persona[0]['userCode'])

buscarId()
#txt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuMDAyNTYwMDIiLCJpc3MiOiJodHRwczovL21pbXVuZG8udXBuLmVkdS5wZS9zYW1sMi9hY3MiLCJpYXQiOjE2Njc4ODI4MzIsImV4cCI6MTY2Nzg5MzYzMiwibmJmIjoxNjY3ODgyODMyLCJqdGkiOiJhNDgyZklWSU4zaGpPTVhTIn0=.IBZubcd7tFnOLo362XHC3qKW-jlwh6MQwuksaK3G1Ao"
#txt1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
#txt2 = "eyJzdWIiOiJuMDAyNTYwMDEiLCJpc3MiOiJodHRwczovL21pbXVuZG8udXBuLmVkdS5wZS9zYW1sMi9hY3MiLCJpYXQiOjE2Njc4ODI4MzIsImV4cCI6MTY2Nzg5MzYzMiwibmJmIjoxNjY3ODgyODMyLCJqdGkiOiJhNDgyZklWSU4zaGpPTVhTIn0"
#txt3 = "IBZubcd7tFnOLo362XHC3qKW-jlwh6MQwuksaK3G1Ao"
#texto_decodificado = b64.b64decode(txt3)
#print('El texto deco es: {} '.format(texto_decodificado))
'''
import requests
import json

def obtener_token():
  url_token = "https://personalsiteshstorage.blob.core.windows.net/contenedorblob/tokenConsultaUPN.txt"

  response = requests.get(url_token)
  token = response.text.strip()
  #print(token)
  return token

def buscarId(consulta):
  url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt={str(consulta)}"
  token = obtener_token()
  _headers = {'Authorization': token}

  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  return dataJson


data = buscarId("n0025600")
print(data)