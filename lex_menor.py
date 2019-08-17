# Escreva uma função que receba um array de strings como
# parâmetro e devolve o primeiro string da ordem lexicográfica,
# ignorando-se maiúsculas e minúsculas

def lex_menor(lista):

    lista_minusculas = []

    for item in lista:
        item = item.lower()
        lista_minusculas.append(item)

    lista_final = sorted(lista_minusculas)

    return lista_final[0]

minha_lista = ["caQui", "MAça", "Abacaxi", "banana", "Abacate"]

print(lex_menor(minha_lista))
