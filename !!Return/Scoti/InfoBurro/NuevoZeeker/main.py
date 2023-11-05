import requests

url = "http://198.100.155.3/seek/index.php?view=mostrar&cod=07881692"

headers = {
    "Host": "198.100.155.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://198.100.155.3/seek/index.php?view=home",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=upjk3snct9169itkurn113dl56",
    "Upgrade-Insecure-Requests": "1",
    "Authorization": "Basic ZGV1ZGFjZXJvOk5XQjdYMjIz",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
