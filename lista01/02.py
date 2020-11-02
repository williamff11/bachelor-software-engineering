n = 1
m = 1
result = 1
numero = int(input("Insira um número limite para n: "))

print(f"S = {n}/{m}", end=" ")
for i in range(numero-1):
    n += 1
    m += 2
    print(f" + {n}/{m}", end=" ")
    result += (n / m)

print()
print(f"S = {result}")