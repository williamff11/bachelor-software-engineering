# number = int(input())

# n_primos = [1]

# i = 1
# j = 1

# while i < number:
#     i += 1
#     while j < i:
#         print(i, j)
#         print(not j % i == 0)
#         if not j % i == 0:
#             n_primos.append(i)
#         j += 1

# print(n_primos)

# while i < number:
#     while j < number:
#         if number % i == 0:
#             print('NÃO É PRIMO')
#             bool = False
#         i += 1
#     if not number % i == 0:
#         print(i)
#     i += 1

# print(n_primos)

numero = int(input("\nDigite um número: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print(lista)