import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

inicio = time.time()

def buscarId(id):
  url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt={id}"
  token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIzLTA1LTMxVDIzOjMyOjE4LjI4N1oiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2ODU2NjIzMzh9.zhh_zYm2w-RdGJezRUdiYnIapl6NwFY2Se5y6on8RKY"
  _headers = {'x-access-token': token }

  response = requests.get(url, headers=_headers)
  dataJson = response.json()

  if dataJson['status'] == False:
    print("Token caducado")
    print(dataJson)
    return

  if dataJson['data'] == None:
    print("No existe")
    return

  persona = dataJson['data']

  print("\n")

  for x in persona:
    print("userId:", x['userId'])
    print("userName:", x['userName'])
    print("userCode:", x['userCode'])
    print("\n")

def main():
  print("-------------------------")
  print("\n")

  start_id = 25600
  end_id = 25699

  # Crear un ThreadPoolExecutor con un número adecuado de hilos
  executor = ThreadPoolExecutor(max_workers=10)

  # Lista para almacenar las futuras consultas
  futures = []

  # Realizar las consultas en paralelo
  for i in range(start_id, end_id + 1):
    id = f"n{i:08}"
    future = executor.submit(buscarId, id)
    futures.append(future)

  # Obtener los resultados de las consultas (opcional)
  for future in futures:
    future.result()

if __name__ == '__main__':
  main()
  fin = time.time()
  print(fin - inicio)
