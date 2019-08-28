# Escreva uma função soma_hipotenusas que receba como parâmetro
# um número inteiro positivo n e devolva a soma de todos os
# inteiros entre 1 e n que são comprimento da hipotenusa de
# algum triângulo retângulo com catetos inteiros.

# Função que calcula a hipotenusa

def calcula_hipotenusa(a, b):
    hipotenusa = ((a*a) + (b*b))
    return hipotenusa
 
# Função que soma as hipotenusas

def soma_hipotenusas(n):
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

# Função que recebe a entrada do número pelo usuário

def entrada():
    x = int(input("Digite um número inteiro e positivo: "))
    while x < 1:
        print("Número inválido! Tente novamente.")
        print()
        x = int(input("Digite um número inteiro e positivo: "))
    print(soma_hipotenusas(x)) # Chamada da função que soma as hipotenusas

if __name__ == "__main__":
    entrada()
