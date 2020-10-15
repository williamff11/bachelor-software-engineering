number = int(input("Digite o número que será multiplicado: "))
init = int(input("Digite o inicio da multiplicação: "))
end = int(input("Digite o fim da multiplicação: "))

for i in range(init, end + 1):
    result = number * i
    print(f"{number} X {i} = {result}")