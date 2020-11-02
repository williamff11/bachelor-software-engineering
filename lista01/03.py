def cumsum(lista_numeros):
    result = 0
    nova_lista = []
    for i in lista_numeros:
        result += i
        nova_lista.append(result)
    return nova_lista


lista = [1, 3, 6, 10, 15, 21]
print(cumsum(lista))