number = int(input())

i = 2
bool = True
while i < number:
    if number % i == 0:
        print(f"{number} NÃO É PRIMO")
        bool = False
    i += 1

if bool:
    print(f"{number} É PRIMO")