contadores_pares = 0
contadores_impares = 0
for i in range(10):
    n = int(input("insira um numero inteiro: "))
    if n % 2 == 0:
        contadores_pares += 1
    else:
        contadores_impares += 1

print(f"{contadores_pares} pares e {contadores_impares} impares")
