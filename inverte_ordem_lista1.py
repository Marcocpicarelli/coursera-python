# Escreva um programa que recebe uma sequência de
# números inteiros e imprima todos os valores em
# ordem inversa. A sequência sempre termina
# pelo número 0. Note que 0 (ZERO) não deve fazer
# parte da sequência.

def inverte_ordem_lista():
    contador = -2
    lista = []
    n = 1

    while n != 0:
        n = int(input("Digite um número inteiro diferente de zero ou zero para terminar: "))
        lista.append(n)
        contador = contador + 1

    while contador >= 0:
        print(lista[contador])
        contador = contador - 1

##### INÍCIO DO PROGRAMA #####

inverte_ordem_lista()




