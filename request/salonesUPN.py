import requests
import json
import time

#admin.suite@u-uplanner.com | administrador

inicio = time.time()

def buscarId(id):
  #id = "00100017"
  #id = id[-6:]
  url = f"https://mimundo.upn.edu.pe/api/participants?courseId=ISOF1311&courseSection={str(id)}&period=223413"

  token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuMDAyNTYwMDEiLCJpc3MiOiJodHRwczovL21pbXVuZG8udXBuLmVkdS5wZS9zYW1sMi9hY3MiLCJpYXQiOjE2ODU1OTg1NjQsImV4cCI6MTY4NTYwOTM2NCwibmJmIjoxNjg1NTk4NTY0LCJqdGkiOiJsTWJIRjdpYm1LeXhDWkNqIn0.K5YYGIdcEIREWk0I2cGIJDXPKG-hd8jZxcHWeAVP554"
  #_headers = {'Authorization': token }
  _headers = {'Authorization': token }


  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  print(dataJson)
  '''
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
  '''

def main():
  #print("-------------------------")

  #efe = input("Id: \n - ")
  #print("\n")

  codigosalon = 2234139640

  buscarId(codigosalon)



if __name__ == '__main__':
  main()
  fin = time.time()
  print(fin-inicio) 
