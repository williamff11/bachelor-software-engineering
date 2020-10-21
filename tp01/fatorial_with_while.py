def fatorial_de(number):
    result = 1
    cont = 1
    while number > 0 and cont < number:
            result += result * cont
            cont += 1
    if number > 0:
        print(result)
    else:
        print("não é possível calcular o fatorial de número negativo")


n = int(input("Insira um número positivo: "))
fatorial_de(n)
