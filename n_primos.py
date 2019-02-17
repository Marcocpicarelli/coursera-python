###############################  ENUNCIADO  ###############################

#   Escreva a função n_primos que recebe um número inteiro maior ou igual
#   a 2 como parâmetro e devolve a quantidade de números primos que existem
#   entre 2 e n (incluindo 2 e, se for o caso, n).

################################  FUNÇÕES  ################################

def checar_primo(x): # Função que checa se um número é primo
    divisor = 2
    eh_primo = True

    while divisor < x and eh_primo:
        resto = x % divisor
        if resto == 0:
            eh_primo = False
        else:
            eh_primo = True
        divisor = divisor + 1
        
    if x==2 or eh_primo:
        print(x)

def entrada(): # Função que recebe a entrada do número digitado pelo usuário
    n = int(input("Digite um número inteiro maior que 2: "))

    while n <= 2:
        print("Número inválido! Tente novamente!")
        print()
        n = int(input("Digite um número inteiro maior que 2: "))

    percorre_numeros(n) # Chamada da função que percorre os números até o limite digitado pelo usuário

def percorre_numeros(n): # Função que percorre os números até o limite digitado pelo usuário
    contador = 2

    while contador <= n:
        checar_primo(contador) # Chamada da função que checa se o número é primo
        contador = contador + 1

###########################  INÍCIO DO PROGRAMA  #############################

entrada () # Chamada da função recebe a entrada de um número pelo usuário



