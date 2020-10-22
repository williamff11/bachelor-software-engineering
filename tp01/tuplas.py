def maybe_return_el_at_tuple(tupla: tuple, el):
    return tupla.index(el)


def return_two_tuples(tupla: tuple):
    len_tuple = int(len(tupla)/2)
    return tupla[0:len_tuple], tupla[len_tuple:int(len_tuple*2)]


def remove_el_tuple(tupla: tuple, el):
    lista = list(tupla)
    lista.remove(el)
    new_tuple = tuple(lista)
    return new_tuple


def invert_tuple(tupla: tuple):
    return tupla[::-1]


t = ("x", "y", 10, 20, "c", 11)

first = maybe_return_el_at_tuple(t, 20)
print(first)

second = return_two_tuples(t)
print(second)

third = remove_el_tuple(t, "y")
print(third)

fourth = invert_tuple(t)
print(fourth)
