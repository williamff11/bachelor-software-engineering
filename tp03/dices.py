from random import randint


def mostra_numero_repeticoes():
    lancamentos = faz_lancamentos()
    for i in range(1, 7):
        print(lancamentos.count(i))


def faz_lancamentos():
    result_lancamentos = []
    for i in range(0, 100):
        random_numero = randint(1, 6)
        result_lancamentos.append(random_numero)
    return result_lancamentos


mostra_numero_repeticoes()
