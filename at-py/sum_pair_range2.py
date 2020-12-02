n = int(input("insira um numero inteiro: "))
lista = []
result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        lista.append(i)
    result = sum(lista)

print(result)
