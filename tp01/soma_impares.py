def soma_impares():
    sum = 0
    number = int(input("Insira um número: "))
    for i in range(number + 1):
        if i % 2 != 0:
            sum += i
    print(sum)


soma_impares()
