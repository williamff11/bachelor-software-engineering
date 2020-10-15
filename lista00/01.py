# number = 1
# pares = 0
# impares = 0

# while number <= 10:
#     a = int(input())
#     number = number + 1
#     if a % 2 == 0:
#         a = pares
#         pares = pares + 1
#     else:
#         a = impares
#         impares = impares + 1


# print("A qtn de números pares é: ", pares)
# print("A qtn de números impares é: ", impares)

contadores_pares = 0
contadores_impares = 0
for i in range(10):
    n = int(input("insira um numero inteiro: "))
    if n % 2 == 0:
        contadores_pares += 1
    else:
        contadores_impares += 1

print(f"{contadores_pares} pares e {contadores_impares} impares")
