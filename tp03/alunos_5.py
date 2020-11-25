"""
Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um
nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que indica todos os
alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos).
"""


def get_avg_height_alunos(alunos):
    alturas = alunos.values()
    media = sum(alturas) / len(alunos)
    show_alunos_bigger_than(media, alunos)


def show_alunos_bigger_than(media, alunos):
    alunos_bigger_that_media = []
    for aluno in alunos:
        if alunos[aluno] > media:
            alunos_bigger_that_media.append(aluno)
    print(alunos_bigger_that_media)


terminou = False
dict_alunos = {}
while not terminou:
    nome_aluno = input("Insira o nome do aluno: ")
    if nome_aluno == 'Sair':
        terminou = True
    if not terminou:
        altura_aluno = float(input("Insira a altura do aluno: "))
        dict_alunos[nome_aluno] = altura_aluno
        get_avg_height_alunos(dict_alunos)
