import requests
import json
#admin.suite@u-uplanner.com | administrador
def buscarId(id):
  #dni = "n00100020"
  #id = "00100017"
  id = id[-6:]
  url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt=n00{str(id)}"

  token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIzLTA1LTMxVDIzOjMyOjE4LjI4N1oiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2ODU2NjIzMzh9.zhh_zYm2w-RdGJezRUdiYnIapl6NwFY2Se5y6on8RKY"
  #_headers = {'Authorization': token }
  _headers = {'x-access-token': token }


  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  if(dataJson['status'] == False):
    print("Tokem caducado")
    print(dataJson)
    return

  if(dataJson['data'] == None):
    print("No existe")
    return

  persona = dataJson['data']

  #print(dataJson)
  #print(persona)
  #print(persona)|
  print("userId: ",persona[0]['userId'])
  print("userName: ",persona[0]['userName'])
  print("userCode: ",persona[0]['userCode'])

def buscarNombre(name):
   #dni = "n00100020"
   #id = "00100017"
   url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt={name}"

   token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIyLTExLTA3VDIwOjU1OjAxLjIwN1oiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2Njc5NDA5MDF9.4ZMoubl4-UbbGECNIP-Hf4w2H3MpRIvNmPL4x8ElN1U"
   _headers = {'Authorization': token }


   response = requests.get(url, headers=_headers)
   dataJson = response.json()

   if(dataJson['status'] == False):
    print("Tokem caducado")
    print(dataJson)
    return

   if(dataJson['data'] == []):
     print("No existe")
     return
   persona = dataJson['data']

   print("userId: ",persona[0]['userId'])
   print("userName: ",persona[0]['userName'])
   print("userCode: ",persona[0]['userCode'])

print("-------------------------")

option = input("option 1 or 2:\n- ")
if option == "1":
  efe = input("Id: \n - ")
  print("\n")
  buscarId(efe)
if option == "2" :
  efe = input("Nombre: \n - ")
  print("\n")
  buscarNombre(efe)
