import requests
from bs4 import BeautifulSoup
import re

url = "http://brasil.pyladies.com/about"
requisicao = requests.get(url)

if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com Sucesso")

requisicao.encoding = 'utf-8'

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

paragrafos = []
for paragrafo in soup.find_all('p', class_='about-text'):
    paragrafos.append(paragrafo.get_text().replace('\n', "").split())


lists = []
for listas in paragrafos:
    lists += listas

dict = {}
list_just_one_word = []
for word in lists:
    new_string = re.sub(
        u'[^a-zA-Z0-9àáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', word).lower()

    if new_string in dict:
        dict[new_string] += 1
    else:
        dict[new_string] = 1
        list_just_one_word.append(new_string)

print(f"número de palavras: {len(dict)}")
print(list_just_one_word)

palavra = "ladies"

c = len(re.findall(palavra, soup.get_text()))

print("Ocorrências da palavra", palavra, ":", c)
