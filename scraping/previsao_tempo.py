import requests
from bs4 import BeautifulSoup

url = "http://www.cptec.inpe.br/cidades/tempo/241"
requisicao = requests.get(url)

if requisicao.status_code != 200:
    requisicao.raise_for_status()


html = requisicao.text
soup = BeautifulSoup(html, "lxml")

for div_prev in soup.find_all('div', class_='previsao'):
    print(div_prev)


for div_previsao in soup.find_all('div', class_='previsao'):
    for div_prev in div_previsao.find_all('div', class_='prev'):
        print(div_prev)
    for div_tit in div_previsao.find_all('div', class_='tit'):
        print(div_tit)


Dict = {}
rotulo_lin = []
for div_previsao in soup.find_all('div', class_='previsao'):
    d = {}
    rotulo_col = []
    for div_prev in div_previsao.find_all('div', class_='prev'):
        for c in div_prev.find_all('div', class_='c2'):
            d[c.contents[0]] = c.b.text
            rotulo_col.append(c.contents[0])
        for c in div_prev.find_all('div', class_='c3'):
            d[c.contents[0]] = c.b.text
            rotulo_col.append(c.contents[0])
        for c in div_prev.find_all('div', class_='c4'):
            d[c.contents[0]] = c.b.text
            rotulo_col.append(c.contents[0])
        for c in div_prev.find_all('div', class_='c5'):
            d[c.contents[0]] = c.b.text
            rotulo_col.append(c.contents[0])
        for c in div_prev.find_all('div', class_='c6'):
            d[c.contents[0]] = c.b.text
            rotulo_col.append(c.contents[0])
    for div_tit in div_previsao.find_all('div', class_='tit'):
        Dict[div_tit.text] = d
rotulo_lin.append(div_tit.text)

# Imprimir uma tabela
print("DIA", end=' ')
for j in rotulo_col:
    print(j, end=' ')
print()

for i in rotulo_lin:
    print(i, end=' ')
    for j in rotulo_col:
        if len(Dict[i][j].split()) > 0:
            print(Dict[i][j], end=' ')
        else:
            print("-", end=' ')
    print()
