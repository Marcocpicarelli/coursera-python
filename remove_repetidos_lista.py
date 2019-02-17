# Escreva a função remove_repetidos que recebe como parâmetro
# uma lista com números inteiros, verifica se tal lista possui
# elementos repetidos e os remove. A função deve devolver uma
# lista correspondente à primeira lista, sem elementos
# repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    
    lista_ordenada = []

    for n in lista:
        if n not in lista_ordenada:
            lista_ordenada.append(n)

    lista_ordenada = sorted(lista_ordenada)

    if lista_ordenada[0] == 0:
        return lista_ordenada[1:]
    else:
        return lista_ordenada

##### INÍCIO DO PROGRAMA #####

lista = []
contador = 0

quantidade = int(input("Quantos números tem a sua lista? "))
print()

while contador < quantidade:
    n = int(input("Digite o próximo número da lista: "))
    contador = contador + 1
    lista.append(n)

print(remove_repetidos(lista))
