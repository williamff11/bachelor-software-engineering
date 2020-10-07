lista = []

previous = 0
currency = 1
lista.append(previous)
lista.append(currency)

for i in range(2,11):
    next_number = previous + currency

    print(next_number)
    previous = currency
    currency = next_number
    lista.append(next_number)
print(lista)
