import pandas as pd


data_frame = pd.read_csv(
    'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv', sep=',')


filter_paises = data_frame[(data_frame['NOC'] == 'SWE') | (
    data_frame['NOC'] == 'DEN') | (data_frame['NOC'] == 'NOR')]
filter_ano = filter_paises[(filter_paises['Year'] >= 2001)]
filter_esportes = filter_ano[(filter_ano['Sport'] == 'Curling') | (filter_ano['Sport'] == 'Skating') | (
    filter_ano['Sport'] == 'Skiing') | (filter_ano['Sport'] == 'Ice Hockey')]

sport_curling = filter_esportes[(filter_esportes['Sport'] == 'Curling') & (
    filter_esportes['Medal'] == 'Gold')]
curling_result = sport_curling.groupby(['NOC'])['NOC'].count()

print(curling_result)


sport_skating = filter_esportes[(filter_esportes['Sport'] == 'Skating') & (
    filter_esportes['Medal'] == 'Gold')]
skating_result = sport_skating.groupby(['NOC'])['NOC'].count()

print(skating_result)

sport_skiing = filter_esportes[(filter_esportes['Sport'] == 'Skiing') & (
    filter_esportes['Medal'] == 'Gold')]
skiing_result = sport_skiing.groupby(['NOC'])['NOC'].count()

print(skiing_result)


sport_ice_hockey = filter_esportes[(filter_esportes['Sport'] == 'Ice Hockey') & (
    filter_esportes['Medal'] == 'Gold')]
ice_hockeu_result = sport_ice_hockey.groupby(['NOC'])['NOC'].count()

print(ice_hockeu_result)
