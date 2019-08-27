# Escreva um programa que recebe uma lista de
# números inteiros e inverta a ordem dessa lista.
# A sequência sempre termina pelo número 0.
# Note que 0 (ZERO) não deve fazer parte da sequência.

def inverte_ordem_lista():
    contador = -2
    lista = []
    n = 1
    lista_invertida = []

    while n != 0:
        n = int(input("Digite um número inteiro diferente de zero ou zero para terminar: "))
        lista.append(n)
        contador = contador + 1

    while contador >= 0:
        lista_invertida.append(lista[contador])
        contador = contador - 1

    return lista_invertida

##### INÍCIO DO PROGRAMA #####

print(inverte_ordem_lista())
