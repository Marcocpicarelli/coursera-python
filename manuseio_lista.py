# Função que clona lista

def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

# Outra opção de função que clona lista

def clona_lista(lista):
    lista_clonada = lista[:]

# Função que inverte a ordem de lista

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

# Função que retorna o maior elemento da lista

def maior_elemento(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada[-1]

# Função que retorna a soma dos elementos de uma lista

def soma_elementos(lista):
    soma = 0
    contador = 0

    while contador < len(lista):
        soma = soma + lista[contador]
        contador = contador + 1

    return soma

# Função que recebe uma lista e retorna ela
# mesma ordenada e sem elementos repetidos

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
