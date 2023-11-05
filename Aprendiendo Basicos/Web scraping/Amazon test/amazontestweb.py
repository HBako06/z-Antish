import requests
import xlsxwriter
from bs4 import BeautifulSoup as b

workbook = xlswriter.Workbook('prueba1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1','Producto')
worksheet.write('B1','Precio')

url = 'https://www.amazon.com/s?k=apple'

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}
#"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 Safari/537.36"
html = requests.get(url,headers=headers)

content = html.content
soup = b(content,"lxml")
print(soup)
