import requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# checando conexao
requisicao = requests.get(url, timeout=5)

if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado")


# pegando o csv
csv = requisicao.text

# separa as linhas em uma lista
linhas = csv.splitlines()

# separa os rotulos da coluna
rotulo_col = linhas[0].split(',')

# faz o rotul0 das colunas ir da posicao 4 para frente
rotulo_col = rotulo_col[4:]

rotulo_lin = []  # rotulo das linhas
tabela = {}  # A tabela em forma de dicionario

for l in range(1, len(linhas)):
    colunas = linhas[l].split(',')  # pega os valores saparados por virgula
    rotulo = colunas[0]
    rotulo_lin.append(rotulo)
    d = {}
    c = 4

    for mes in rotulo_col:
        d[mes] = float(colunas[c])
        c = c + 1
    tabela[rotulo] = d


# Imprime primeiramente os rotulos da coluna
print("{:^15}".format("Modelo "), end=' ')
for j in rotulo_col:
    print("{:^15}".format(j), end=' ')
print()

# Depois, imprime o restante da tabela
for i in rotulo_lin:
    print("{:^15}".format(i), end=' ')
    for j in rotulo_col:
        print("{:^5.2f}".format(tabela[i][j]), end=' ')
    print()
