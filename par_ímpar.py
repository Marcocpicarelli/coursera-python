# Função que verifica se um número é par ou ímpar

def verifica_par_impar(n):
    if n % 2 == 0: # Verifica se o resto da divisão dá zero
        return "Par"
    else:
        return "Ímpar"

# Função que conta os números pares e ímpares
# em uma lista terminada por 0

def conta_par_impar(lista):
    p = 0
    i = 0
    cont = 0

    while cont < len(lista) - 1:
        if lista[cont] % 2 == 0:
            p = p + 1
        else:
            i = i + 1
        cont += 1

    return p, i

# Função que exibe uma lista com a quantidade de números
# pares desejados pelo usuário a partir de zero

def mostra_pares(n):

    contador = 1
    valor = 2
    lista = []

    while contador <= n:
        lista.append(valor)    
        contador = contador + 1
        valor = valor + 2

    return lista

# Função que exibe uma lista com a quantidade de números
# ímpares desejados pelo usuário a partir de zero

def mostra_impares(n):

    contador = 1
    valor = 1
    lista = []

    while contador <= n:
        lista.append(valor)    
        contador = contador + 1
        valor = valor + 2

    return lista
