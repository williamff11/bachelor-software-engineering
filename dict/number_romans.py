def transform_numbers_in_romans(number):
    result = []
    unidades = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',
                5: ' V', 6: 'VI', 7: 'V II', 8: 'VIII', 9: 'IX'}
    dezenas = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
               5: 'L', 6: ' LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    centenas = {0: '', 1: 'C', 2: 'CC', 3: ' CCC', 4: 'CD',
                5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

    u_d_c = get_centena_dezena_unidade(number)

    result.append(centenas[u_d_c[2]])
    result.append(dezenas[u_d_c[1]])
    result.append(unidades[u_d_c[0]])

    print(''.join(result))


def get_centena_dezena_unidade(numero):
    uni = numero % 10
    numero = numero - uni
    dezena = (numero // 10) % 10
    numero = (numero - dezena) // 10
    centena = numero // 10

    return [uni, dezena, centena]


n = int(input("Digite um número: "))

transform_numbers_in_romans(n)
