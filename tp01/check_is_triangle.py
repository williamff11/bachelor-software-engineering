def create_tuple(x, y, z):
    return (x, y, z)


def check_sides_are_valid(tuple):
    if tuple[0] < tuple[1] + tuple[2] or tuple[1] < tuple[0] + tuple[2] or tuple[2] < tuple[1] + tuple[0]:
        return True
    else:
        return False


def set_type_triangle(tuple):
    if tuple[0] == tuple[1] and tuple[0] == tuple[2]:
        return "Triângulo Equilátero"
    elif tuple[0] != tuple[1] and tuple[0] != tuple[2]:
        return "Triângulo Escaleno"
    else:
        return "Triângulo Isósceles"


side1 = input("Insira o comprimento do primeiro lado: ")
side2 = input("Insira o comprimento do segundo lado: ")
side3 = input("Insira o comprimento do terceiro lado: ")

tupla = create_tuple(side1, side2, side3)
is_triangle = check_sides_are_valid(tupla)

if is_triangle:
    print(set_type_triangle(tupla))
else:
    print("Os comprimentos passados não formam um triângulo!")