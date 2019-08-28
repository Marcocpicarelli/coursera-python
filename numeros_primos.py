# Função que checa se um número é primo

def checa_primo(n):
    divisor = 2
    eh_primo = True

    while divisor < n and eh_primo:
        resto = n % divisor
        if resto == 0:
            eh_primo = False
        else:
            eh_primo = True
        divisor = divisor + 1

    if eh_primo:
        return n, eh_primo
    else:
        return n, False

# Função que mostra o maior número primo
# até o valor n definido pelo usuário

def maior_primo(n):
    aux = n
    while aux > 2:
        if checa_primo(aux):
            return aux
        aux = aux - 1
    return 2

# Função que percorre os números até o limite n
# definido pelo usuário e exibe os primos

def percorre_numeros(n):
    contador = 2

    while contador <= n:
        print(checa_primo(contador)) # Chamada da função que checa se o número é primo
        contador = contador + 1
