# Função que conta as vogais ou consoantes de uma frase

def conta_letras(frase, contar = "vogais"):

    cont_vogais = 0
    cont_consoantes = 0
    indice = 0

    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    lista_consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                    "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
                    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

    contar = contar.strip()
    contar = contar.lower()

    while indice < len(frase):
        if contar == "vogais" and frase[indice] in lista_vogais:
            cont_vogais += 1
        if contar == "consoantes" and frase[indice] in lista_consoantes:
            cont_consoantes += 1
        indice += 1

    if contar == "vogais":
        return cont_vogais

    if contar == "consoantes":
        return cont_consoantes
