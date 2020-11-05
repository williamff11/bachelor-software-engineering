from collections import defaultdict
caderno = {"Carlos": "222-3333", "Ana": "9999-9999",
           "Creed": "9356-9416", "Carlos": '8485-8521'}
print(caderno)
print(caderno.get('Ana'))

novo = caderno.copy()
novo.pop('Ana')
print(novo)


contatos = {'Carlos': {"telefone": "2222-9999", "email": 'ou@ou.com'}}
print(contatos)

frase = "O mengão deita demais meus queridos"
frase = frase.lower()

contador = defaultdict(int)
for caracter in frase.replace(' ', ''):
    contador[caracter] = 1 if caracter not in contador else contador[caracter] + 1
print(contador)


"""
Dado uma turma com três notas de prova, retorne quais alunos foram aprovados ou reprovados
com a média 6
"""


def calc_situacao_turma(turma):
    resultado = {}
    for nome, notas in turma.items():
        media = sum(notas)/len(notas)
        if media >= 6:
            resultado[nome] = " FOI APROVADO COM A MEDIA: ", media
        else:
            resultado[nome] = " FOI REPROVADO COM A MEDIA: ", media
    return resultado


turma = {
    "Carlos": [7, 7, 7],
    "Ana": [2, 8, 7],
    "Clara": [6, 6, 6]
}

print(calc_situacao_turma(turma))
