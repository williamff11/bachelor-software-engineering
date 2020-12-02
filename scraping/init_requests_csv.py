"""
Obtendo dados de um csv e calculando a média
"""

import requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text

linhas = csv.splitlines()

for l in range(1, len(linhas)):
    colunas = linhas[l].split(',')
    soma = 0
    for c in range(4, len(colunas)):
        soma = soma + float(colunas[c])
    print(colunas[0], soma/(len(colunas)-4))
