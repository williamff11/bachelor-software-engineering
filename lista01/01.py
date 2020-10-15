t = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80) )

lista = []
list_all = []
for i in range(len(t)):
    lista = list(t[i])
    print(f"{i}: {sum(lista)}")
    list_all.append(sum(lista))
media = sum(list_all) / len(t)
print(f"Média: {media}")