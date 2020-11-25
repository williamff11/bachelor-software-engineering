lista = []


def show_lista():
    print(lista)


def append_el():
    new_el = input('Adicione o valor do elemento: ')
    lista.append(new_el)


def remove_el():
    el_remove = input('Adicione o valor do elemento que quer Remover: ')
    if el_remove in lista:
        lista.remove(el_remove)
        print('Valor removido da lista')
    else:
        print('Valor não encontrado na lista')


def remove_all_el():
    lista.clear()
    print('Todos os elementos da lista foram removidos')


opcao = 'a'
while opcao != 'e':
    print('''
    [a] Mostrar Lista
    [b] Incluir Elemento
    [c] Remover Elemento
    [d] Apagar Todos os Elementos da Lista
    [e] Sair
    ''')
    opcao = str(input('Selecione uma opção acima: '))

    if opcao == 'a':
        show_lista()
    elif opcao == 'b':
        append_el()
    elif opcao == 'c':
        remove_el()
    elif opcao == 'd':
        remove_all_el()
