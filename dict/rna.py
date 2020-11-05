"""
Sabe-se que uma mol´ecula de RNA mensageiro ´e utilizada como base para sintetizar prote´ınas, no
processo denominado de tradu¸c˜ao. Cada trinca de bases de RNA mensageiro est´a relacionado com um
amino´acido. Combinando v´arios amino´acidos, temos uma prote´ına. Com base na tabela (simplificada)
de trincas de RNA abaixo, crie uma fun¸c˜ao que receba uma string representando uma mol´ecula de RNA
mensageiro válida, segundo essa tabela, e retorne a cadeia de amino´acidos que representam a prote´ına
correspondente:
"""


def show_aminiacidos(rna_s):
    table = {
        "UUU": "Phe",
        "CUU": "Leu",
        "UUA": "Leu",
        "AAG": "Lisina",
        "UCU": "Ser",
        "UAU": "Tyr",
        "CAA": "gln",
    }

    resultado = []
    for index in range(0, len(rna_s) // 3):
        trinca = rna_s[index*3:(index*3)+3]
        resultado.append(table[trinca])
    print('-'.join(resultado))


show_aminiacidos("UUUUUAUCU")
