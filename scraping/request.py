import requests

url = "https://www.gta.ufrj.br/grad/07_1/ass-dig/index.html"

# Usando requests
requisicao = requests.get(url, timeout=5)

if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com sucesso!")
