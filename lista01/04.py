def is_palindromo(palavra):
    inicio = 0
    fim = len(palavra) - 1

    for i in range(len(palavra)//2):
        if palavra[inicio] != palavra[fim]:
            return False
        inicio = inicio + 1
        fim = fim - 1
    return True