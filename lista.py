lista = [1,12,3,6,7,9,10,54,67]
outra_lista = ['a', 2, True]
lista.copy()
print(lista.count(1))

for index, item in enumerate(lista):
  if item == 3:
    print(index)

lista_de_lista = [[10],[9,5],[6,5, 90, 100]]
lista.sort()
lista_de_lista.sort()

print(lista)

import random
random.shuffle(lista)
print(lista)

