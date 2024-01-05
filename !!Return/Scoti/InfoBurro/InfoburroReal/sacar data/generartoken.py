import requests

url = "https://www.google.com/recaptcha/api2/reload?k=6Ld7wUcnAAAAADPzTvPWOAEswBzJfqyNErkKIOhQ"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-419,es-US;q=0.9,es-PE;q=0.8,es;q=0.7,en;q=0.6,pt;q=0.5",
    "Content-Length": "8843",
    "Content-Type": "application/x-protobuffer",
    "Dnt": "1",
    "Origin": "https://www.google.com",
    "Sec-Ch-Ua": '"Not=A?Brand";v="99", "Chromium";v="118"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Aquí podrías incluir cualquier información adicional necesaria en la carga útil.
payload = {}  # Ajusta esto según la documentación de reCAPTCHA

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)




'''
import requests

url = "http://infoburo.com.pe/Score/BuscarDocumento"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "es-419,es-US;q=0.9,es-PE;q=0.8,es;q=0.7,en;q=0.6,pt;q=0.5",
    "Connection": "keep-alive",
    "Content-Length": "1632",
    "Content-Type": "application/json",
    "Cookie": "_ga=GA1.1.2122346607.1704435343; ASP.NET_SessionId=vqjqfnnvinudxgdt02dyutpa; _ga_B633F8HCWF=GS1.1.1704435342.1.1.1704435457.0.0.0",
    "Host": "infoburo.com.pe",
    "Origin": "http://infoburo.com.pe",
    "Referer": "http://infoburo.com.pe/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Dnt": "1",
    "Sec-Gpc": "1"
}

data = {
    "dni": "07316480",
    "token": "03AFcWeA4SebCa0AGaBLi2kNA48i7RCG5pjW3O6g7buE_bE_jhUD10BUq6ZujZaLXDTwSDFgVOVGgvfqny47V7jQzCKD1OIinSpDJNSfMxiO4s8TfRlCdFEKi1Z8lbtfFYE-VYMtIviAjd2uj3Xd5gSk2tExfXuVbkhgDRAehPrkpfJUfxAb3rTy1ANKLgocmQpcSg6qnDaENtqpUIcuYS32L1a8KCVB3zJl9glpnCi8dsO3NVvRBewJQqLWbVyXSPghz05COh7wvNK0JeDY5HLawBG7BQJcOpmZ8-emnZ94Smsw29KaG7NINtI2NViG-s20hFR7C6-y-CRbj8HZeA5xsnDwoyjZSXSAntshOK5eRoL1xugsXH6Zn2h3QgJ3fM73k7T2c7yElKvCwQeQoB6M8RJVropZRUBdc8FcY6sLIUYc_X1Eu7i2CRPYXcTBJoIR6czyNnTyb7CEQWz5G4wxC0vI40vqkNoLFndNJesVKYDfw_CPIJebGzufeGz8CNLPNe1atc6h7kimsVBsuE6ERmD3VkV-saCk0X0QZ1gICuty0QKCRVJ5GaQQCVV_JrDWKmHx_gYiY7bceg9IcDRFhOqPD_4Gmfx52HWSu9-oYI9QOOyAtiOp6ufvYPlPz1TnON5iL9i1QmzMXIRGTc6NaaATboz5qdaPGCij4OIgB88lEsYmgeoBq6NC_zM3jGtT9Gcqpyaj9uq-3y89RGIcrgYuhjlDM557-weEAc534zEaS5io9ZBWrzxwZIo956Ii81-UWvH-mfPU9y-akD8yKphQ8100MbOeFIH_sKOt7hVd8yC3KSq9AcWF2JhHWfG8d3tPrt8QzLw2OCBwqUVK2KpPUgXCaEikCj1dy8p1PTykfzMM7gdyzRzt6XrjCi1n6S4pGbn_Yjj7k33ZSdd-SwyPAWyIhtgmONWTXTEgDBH2nYRG0VlNs9jJuulvbtljNU6VVXCvRUeEOm3VDhzGc9r7x60XoCIf2j71zHnEzrV2GQUzQwJCQTYjvLSi9bwJeBz35vlsBP94Swt-KSkenGXjatrMeXKB4sHHsboxaukiDAbx5LVImqOIthcVHwV8pK2qTdnohVXN_jNIXRf-kwTfTlMKVVrV6KXmGkH9z5xBJtuqt-DYfaKktA-eR_V8UOpSRWUa3wHfWGmzL9NjLbNLphnon0E7mx_SAsUO0JQgBwRNkBp8yLKPirxmqmBwMxUTOU_k_hLNZwAfhHeCKHNP76msNJvQAD86BBAZjUBq5dNEGaBfz-8DjDKNIeTeMP83PjmgmodEea3j3YahCskeIgDaumB1UrEcGORD0dj_q6R--NHeKKwtO_RxoUWqWCvkwDlJl62U6vSnU__ESDtFCrolCaAkNtqCaTKFDB4DCFcJfTPG8Zh0iOZmzMGJyMFNPa7MIyABME77Dl7PxDtaxX7LPVohkh6xlLo5GjjX8c7f-Sm49nz4IXpyCxEiGZtwgdmC3SD8gf3YB2y94oy7qIGRNWoQ4PYcUc11pQJHff1mVVvUB_p88wSBkO9-UbnO28aotlyg69o8AFznlsuCRa-nty-dQLgikB-Vf9VdnYNX3bPfYD3llUyHVNV8MHmgOAjF3u"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
'''