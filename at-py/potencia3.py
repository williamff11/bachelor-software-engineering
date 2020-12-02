def potencia(a, b):
    return (a**b)


n1 = int(input("insira um numero inteiro: "))
n2 = int(input("insira um numero inteiro: "))

if n1 and n2 >= 0:
    print('O resultado é', potencia(n1, n2))
else:
    print("Digite numeros inteiros positivos")
