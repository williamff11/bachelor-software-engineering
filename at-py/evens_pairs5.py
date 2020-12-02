tuple_number = (32, 89, 15, 99, 2)
list_pais = []
list_evens = []
for i in tuple_number:
    if i % 2 == 0:
        list_pais.append(i)
    else:
        list_evens.append(i)


print("Números Ímpares: ", list_evens)
print("Números Pares: ", tuple(list_pais))
