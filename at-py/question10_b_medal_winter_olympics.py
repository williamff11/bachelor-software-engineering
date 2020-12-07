import pandas as pd

data_frame = pd.read_csv(
    'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv', sep=',')


filter_bigger_medal = data_frame[(data_frame['NOC'] == 'SWE') | (
    data_frame['NOC'] == 'DEN') | (data_frame['NOC'] == 'NOR')]


filter_ano = filter_bigger_medal[(filter_bigger_medal['Year'] >= 2001)]

filtro_esportes = filter_ano[(filter_ano['Sport'] == 'Curling') | (filter_ano['Sport'] == 'Skating') | (
    filter_ano['Sport'] == 'Skiing') | (filter_ano['Sport'] == 'Ice Hockey')]

filter_medals_of_gold = filtro_esportes[filtro_esportes['Medal'] == 'Gold']

maior_medalhista_ouro_filtro = filter_medals_of_gold.groupby(
    ['NOC'])['Medal'].count().sort_values()
print(maior_medalhista_ouro_filtro)
