import requests
import json
import time

#admin.suite@u-uplanner.com | administrador

inicio = time.time()

def buscarId(id):
  #id = "00100017"
  #id = id[-6:]
  url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt=n00{str(id)}"

  token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIzLTA1LTMxVDIzOjMyOjE4LjI4N1oiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2ODU2NjIzMzh9.zhh_zYm2w-RdGJezRUdiYnIapl6NwFY2Se5y6on8RKY"
  #_headers = {'Authorization': token }
  _headers = {'x-access-token': token }


  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  print(dataJson)

  if(dataJson['status'] == False):
    print("Tokem caducado")
    print(dataJson)
    return

  if(dataJson['data'] == None):
    print("No existe")
    return

  persona = dataJson['data']

  print("\n")

  #acá quiero implementar como un foreach
  for x in persona:
    print("userId: ",x['userId'])
    print("userName: ",x['userName'])
    print("userCode: ",x['userCode'])
    print("\n")

def main():
  print("-------------------------")

  #efe = input("Id: \n - ")
  print("\n")

  #Omitiendo el N00
  codigoUPN = 25600

  buscarId(codigoUPN)
  #buscarId("n00256002")
  #buscarId("n00256003")
  #buscarId("n00256004")


if __name__ == '__main__':
  main()
  fin = time.time()
  print(fin-inicio) 
