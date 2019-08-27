########## FUNÇÃO QUE CHECA SE É PRIMO ##########

def é_primo(y):
    divisor = 2
    eh_primo = False

    while divisor < y and not eh_primo:
        resto = y % divisor
        if resto == 0:
            eh_primo = True
        divisor = divisor + 1

    if not eh_primo:
        return y

########## FUNÇÃO QUE LOCALIZA O MAIOR PRIMO ##########

def maior_primo(x):
    aux = x
    while aux > 2:
        if é_primo(aux):
            return aux
        aux = aux - 1
    return 2

########## INÍCIO DO PROGRAMA ##########

n = int(input("Digite um número inteiro maior que 2: "))

print(maior_primo(n))


