def rotate_string(str, number):
    if len(str) >= number:
        l1 = str[:number]
        l2 = str[number:]
        result = l2 + l1
        return result
    else:
        return "Número passado é maior que o número de caracteres da string"


r = rotate_string("aeiou", 3)
print(r)