"""
    Usando Python, faça o que se pede (código e printscreen)
    """

# a - Crie uma lista vazia
list = []

# b - Adicione os elementos: 1, 2, 3, 4 e 5,  usando append()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

# c - Imprima a lista;
print(list)

# d - Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
if(3 in list):
    list.remove(3)

if(6 in list):
    list.remove(6)

# e - Imprima a lista modificada;
print(list)

# f - Imprima também o tamanho da lista usando a função len();
len_list = len(list)
print(len_list)

# g - Altere o valor do último elemento para 6 e imprima a lista modificada.
list[len_list - 1] = 6
print(list)
