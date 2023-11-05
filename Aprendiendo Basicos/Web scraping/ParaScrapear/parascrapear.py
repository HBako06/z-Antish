import requests
from bs4 import BeautifulSoup

client = requests.Session()

html = client.get('https://parascrapear.com/login').content
soup = BeautifulSoup(html, 'html.parser')

print(soup.find(id="toptext").text)

crsf = soup.find('input',{'name':'csrf_token'}).get('value')
print(crsf)

login_information = {
	'csrf_token': crsf,
	'username': "admin",
	'password': "admin",
}

client.post('https://parascrapear.com/login', data=login_information)

html = client.get('https://parascrapear.com').content
soup = BeautifulSoup(html, 'html.parser')

print(soup.find(id="toptext").text)
