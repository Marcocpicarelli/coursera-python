# Função que exibe as letras maiúsculas de uma frase

def maiusculas(frase):
    cont = 0
    letras_maiusculas = ""

    while cont < len(frase):
        if ord(frase[cont]) >= 65 and ord(frase[cont]) <= 90:
            letras_maiusculas += frase[cont]
        cont += 1

    return letras_maiusculas
