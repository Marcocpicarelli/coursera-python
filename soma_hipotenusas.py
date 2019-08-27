###############################  ENUNCIADO  ###############################

# Escreva uma função soma_hipotenusas que receba como parâmetro
# um número inteiro positivo n e devolva a soma de todos os
# inteiros entre 1 e n que são comprimento da hipotenusa de
# algum triângulo retângulo com catetos inteiros.

################################  FUNÇÕES  ################################

def é_hipotenusa(a, b): # Função que calcula a hipotenusa
    return ((a*a) + (b*b))
 
def soma_hipotenusas(n): # Função que soma as hipotenusas
    c = 1
    soma = 0
    while (c <= n):
        c2 = (c*c)       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c2 == é_hipotenusa(a, b)): # Chamada da função que calcula hipotenusa
                    #print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
   
    return soma

def entrada(): # Função que recebe a entrada do número pelo usuário
    x = int(input("Digite um número inteiro e positivo: "))

    while x < 1:
        print("Número inválido! Tente novamente.")
        print()
        x = int(input("Digite um número inteiro e positivo: "))

    print(soma_hipotenusas(x)) # Chamada da função que soma as hipotenusas

###########################  INÍCIO DO PROGRAMA  #############################

entrada() # Chamada da função que recebe a entrada do número pelo usuário
