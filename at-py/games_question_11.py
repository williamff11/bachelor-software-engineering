import pandas as pd

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

data_frame = pd.read_csv(url, sep=',')

# questao a
filter_genre = data_frame[(data_frame['Genre'] == 'Action') | (
    data_frame['Genre'] == 'Shooter') | (data_frame['Genre'] == 'Platform')]
result_a = filter_genre.groupby(['Publisher'])[
    'Publisher'].count().sort_values(ascending=False).head(3)
print(result_a)

# questao b
maior_vendas = data_frame.groupby(
    ['Publisher'])['Global_Sales'].sum().sort_values(ascending=False)
result_b = maior_vendas.head(3)
print(result_b)

# questao c
publi_in_japan_action = data_frame[(data_frame['Year_of_Release'] >= 2020 - 10) & (
    data_frame['Genre'] == 'Action')]
group_action = publi_in_japan_action.groupby(['Publisher'])[
    'Publisher'].count().sort_values(ascending=False)

result_c_action = group_action.head(1)

print(result_c_action)

publi_in_japan_shooter = data_frame[(data_frame['Year_of_Release'] >= 2020 - 10) & (
    data_frame['Genre'] == 'Shooter')]
group_shooter = publi_in_japan_shooter.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False)

result_c_shooter = group_shooter.head(1)

print(result_c_shooter)

publi_in_japan_platform = data_frame[(
    data_frame['Year_of_Release'] >= 2020 - 10) & (data_frame['Genre'] == 'Platform')]
group_platform = publi_in_japan_platform.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False)

result_c_platform = group_platform.head(1)

print(result_c_platform)

# questao d
vendas_action_in_action = data_frame[(
    data_frame['Year_of_Release'] >= 2020 - 10) & (data_frame['Genre'] == 'Action')]
group_vendas_action = vendas_action_in_action.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

result_d_action = group_vendas_action.head(1)
print(result_d_action)


vendas_shooter_in_japan = data_frame[(
    data_frame['Year_of_Release'] >= 2020 - 10) & (data_frame['Genre'] == 'Shooter')]
group_vendas_shooter = vendas_shooter_in_japan.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

result_d_shoort = group_vendas_shooter.head(1)
print(result_d_shoort)

vendas_platform_in_japan = data_frame[(
    data_frame['Year_of_Release'] >= 2020 - 10) & (data_frame['Genre'] == 'Platform')]
group_vendas_platform = vendas_platform_in_japan.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

result_d_platform = group_vendas_platform.head(1)
print(result_d_platform)
