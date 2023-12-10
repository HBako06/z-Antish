import requests

# URL del endpoint
url = 'https://bbva.kontigo.pe/api-bl/v1/calculadora/consulta-rapida'

# Datos que se enviarán en el POST
data = {
  "datosPersonales": {
    "name": "GLEDIS",
    "lastName1": "MONTES",
    "lastName2": "REATEGUI DE ROSEMBERG",
    "documentNumber": "07542837"
  },
  "empresaConvenioId": None,
  "recaptcha": "03AFcWeA53qIsBpGrLoItK-clHYMKsbNqgYZtB9HtxztkO5fhEBlQtBBKU1a00NSvHorHowEsBdh_tqCciYGRleUfLeHAhH5X_fLxVKJ-Gb-39mv7UC2FVVWjWhELrbE5rj9058uA8ohLUQnQ8i9jjqFr3J0SpY-gF8LVNTrQ6zeW4AzGxiHrhROwLeM4Dl4RzxWB6uKYHXa7daHtDwrskJRjpL8K1GkZK2cHXc12_Qbok0prEHg-YbnYEaihWN_dIMYoYcd_pogHRMfEJwXIBvjoR-eMDyedAPh2o4vQhYwKNj1Nn8MIe3SdP6nB6FgKPuqSZCr1tjqIMIy5OOaixl042YCUVK2eLCP_PfEzSqHCgEfDNHYCXtZnhOR-LZj0r7lynuO2jbIY2-ctyqb5Op_zSYvTRihG3v8ryTMtrMuhn4fpT1jiDBXNOPZ7UXPc2wemSl57liC26qfbCfLrHrJY33dZLevkqsSSwyOW7shW3OzSR_jpPX3MZtk__KQI9C8fOK6mVrfbayIKz0sfsngwDSvKmM_XIJ1xVowww4O-Gqw5j5rzv-iVmOSYNTfe3BoP5ESUtE3I38KoTCkNznMExLSm7qNwo9N2e7AS8uQIDY3WZs7qR63uQFf1k8DZGZDVh-iDKcVda0Y94gt4tUVYkeLen0i_T24GCrVNuGBsdU0dr4Iqd8JHYVXdSGB9cWjbPKzg9qN2rG1dRGy0Ye_FTp9ZnQHyI3481c-MOWwzE6FzDZYnDky-L3sn0yUEb_F-uiCJ-iQ_5IwFvsAvq-sJTIppYm_8SL27RWwkDz53uCmKe84Hald2YBEKUcE096QN68TTa82u7ZohbaM9MMTsHFBTDbH24JwG5FAlsd1vtdq_iJ4M2HERkF65o3iAD8kTeC_XgQwSwSJ719b5q1GiqQkBP_q7s_Aj5j3ybRE_PPJAHU-7G7_OQ_IfGpBUgzj7Cliy12sV4jRPnv1FtpxpnBDo8LUyO2Vp8BpLnXTVlgKSCmzA6Bp8DEBx17pqvpA2uPw59psOmNdTcVSSta927pECr9iaFgdlw8fg6HwHIOn2Bs46gmODd0Bd7TZlZPleQ1lsYBvcCP14xv6BQtpEso1mLaJHkXA45ntzkVHHIC7s66N-9B-_51le2j_CdDv-ut8NMouhfE-jpdKiGx5Cb3ybkcRlhddw4sClUUl3fey61TNSlmc5TTk-JsG1ODsGSwHxk-PNM9v9h3dHiBTO0ESvC_KTnctT2R4EpLVaVQvl5QuHMZjV4uJ5D8z9tKTLtbfaEMXdbfzUNvBLphYjKTikftCZJqLF9MNW5Q32UVkAA6wPxSkPQaKh42Hxa86Q7CSupV4gnKT8mis6VIKLSHDiETBZxBohAn4UQ9P5FfktaMLQTZo0zMYYdplryVvBADf8TO9Zr2k0u9oAHQt77Hw-o-eBk9e39Hi3_OpkCE8jOsa_POsCN25cWQuYb0HtzizobOGT3jVDnR6dqWxiqtieOMo_pOUv0YW5ApQNYpXuL6L3xoDRtjI81TAFWUvr3Wgzao72D039myUE-i61PzSSpE6TS6V8yVV8kGr5ff5D2rIEn32I"
}

# Headers de la solicitud
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xhYm9yYWRvcklkIjo1MDQ4LCJ1c2VybmFtZSI6IktBVEVSSS5ZRVNRVUVOLlBST01PVE9SIiwiZG5pIjoiNzI4NjYzMTkiLCJmdWxsbmFtZSI6IktBVEVSSSBFTElTQUJFSFQgWUVTUVVFTiBNQVJUSU5FWiIsInJvbCI6Miwic2NvcGUiOiJwcm9tb3RvckZ1dmV4IiwiYWJpbGl0aWVzIjpbInJlZ2lzdHJvUmVtZXNhIl0sInNlc3Npb24iOm51bGwsImNvbnZlbmlvcyI6WyJwaiIsImVzc2FsdWQiLCJmYXAiLCJjYWphaHVhbmNheW8iLCJmYyIsInRlbGVmb25pY2EiLCJyZWRvbmRvcyIsImZicG5wIl0sImVtcHJlc2FJZCI6MTMsImhhc1JlbWl0dGFuY2VDaGFyZ2UiOmZhbHNlLCJpYXQiOjE3MDEzODc0ODl9.ruMko30uKzDm-4zA8tl5WWIj5ZySVKdc3ZMNUiV-93RRAjtosBnPDgQQ2b7x2RP1hO5HxxaIWOwqpttnpBdCP16RCFIIiS0lqRbbfQiDX1u_o1o42U5Gs5fG-y9KSXmdFG82FL7FtHzUSPTWEvuwzh0fwLjlEMQYBKi8RpzF3ODfuJ9PhIxuAh_QatxpjHzHQP9Az2OTaonst6fj_n5ptPWyK3QWjmqHfgSh2tmhpi4fiZ8dnp7jqvRy0_7UCcaXVqb8NSc7aZ1n29x5oseM4JhoUzvPFjWiSDlj5Pb0Za8K48snsLqrIxZgltuVxjnJqKNjVLPQMhcHUMyJHIWLE8wyx1x6e8AkC_goDrEp1BLs4HYgcjSOqX-b31bsA_Jmr7Hh8bdLvP5878WDDOhbokd9x7ckKtuxn1YyLdctVJoOgbzhGqZ89rwxnjwD0UWiM9CRZ-DWp8SxxXMzpU3l7baPpy91AzyqpMi2vV11p0DcrKXf8c7wfAonSfAYJ2m9RakTr3Wf1e9L66SujtrJ1w98gQJhKtODnGQEM63nKNJEPNrZtdr7a32YxVdFt4q1qQEGWJ1vyGl3UBYLMONL8fkAilGjhzhuF5G85x8yZpknxSlUAN3XjbAXE0g1mBgofGfWFODkOKofuhKMj3IiRGDTeFWVrKsZBlZQfOqb_ho',  # Reemplaza [Tu_Token_Aquí] con tu token real
    'Content-Type': 'application/json',
    'Origin': 'https://conveniosbbva.kontigo.pe',
    'Referer': 'https://conveniosbbva.kontigo.pe/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

# Realizar la solicitud POST
response = requests.post(url, json=data, headers=headers)

# Imprimir la respuesta
print(response.status_code)
print(response.json())
