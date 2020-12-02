import requests
from bs4 import BeautifulSoup
import re

url = "https://pt.wikipedia.org/wiki/Brasil"
palavra = "Brasil"

# Usando requests
html = requests.get(url).text

soup = BeautifulSoup(html, "lxml")
c = len(re.findall(palavra, soup.get_text()))

print("Ocorrências da palavra", palavra, ":", c)
