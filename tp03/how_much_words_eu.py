def show_phrases_have_eu(list_phrases):
    phrases_have = []
    for phrase in list_phrases:
        if check_if_have_word_eu(phrase):
            phrases_have.append(phrase)
    print(phrases_have)


def check_if_have_word_eu(phrase):
    return "eu" in phrase.lower()


terminou = False
phrases = []
while not terminou:
    frase = input("Insira uma palavra: ")
    if frase == 'Sair':
        terminou = True
    else:
        phrases.append(frase)
        show_phrases_have_eu(phrases)
