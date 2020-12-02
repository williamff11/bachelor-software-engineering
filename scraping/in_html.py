import requests
from bs4 import BeautifulSoup

url = "https://www.gta.ufrj.br/grad/06_1/wap/"

# Usando requests
html = requests.get(url+"index.htm").text

soup = BeautifulSoup(html, "lxml")

print(soup.html.head.title.text)

print(soup.html.body.p.text)

for i in soup.html.body.find_all('a'):
    print(i.text)
    print(i.get('href'))


lista_paginas = []
for i in soup.html.body.find_all('a'):
    nome_pagina = url + i.get('href')
    html = requests.get(nome_pagina).text
    soup = BeautifulSoup(html, "lxml")
    lista_paginas.append(soup)

for s in lista_paginas:
    print(s.html.head.title.text)
