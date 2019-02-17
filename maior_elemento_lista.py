# Escreva a função maior_elemento que recebe como parâmetro
# uma lista com números inteirose devolve um número inteiro
# correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):

    lista_ordenada = sorted(lista)

    return lista_ordenada[-1]

##### INÍCIO DO PROGRAMA #####

lista = []

n = int(input("Digite o primeiro número da lista: "))
lista.append(n)

while n != 0:
    n = int(input("Digite o próximo número da lista: "))
    lista.append(n)

print(maior_elemento(lista))
