import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
requisicao = requests.get(url)

if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com Sucesso")

html = requisicao.text
soup = BeautifulSoup(html, "lxml")


def fix_quebra_linha(obj):
    return obj.text.replace('\n', '//')[2:-2].split('//')


rows = []
title = []
for div_table in soup.find_all('div', class_='tabela'):
    for div_titulo in div_table.find_all('div', class_='titulo'):
        title.append(fix_quebra_linha(div_titulo))

        for div_linha in div_table.find_all('div', class_='linha'):
            rows.append(fix_quebra_linha(div_linha))

data_frame = pd.DataFrame(data=rows, columns=title)
result_a = data_frame.to_html(index=False)

print(result_a)
sigla_estado = input("Digite uma região: ")

exist = False
for row in rows:
    if sigla_estado.upper() in row[0]:
        exist = True
        print(row)
        break

if not exist:
    print("Sigla não existe!")
