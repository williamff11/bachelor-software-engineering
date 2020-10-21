def fatorial_de(number):
    result = 1
    if number > 0:
        for i in range(number):
            if i > 0:
                result += result * i
        print(result)
    else:
        print("não é possível calcular o fatorial de número negativo")


n = int(input("Insira um número positivo: "))
fatorial_de(n)
