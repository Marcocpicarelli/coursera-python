def checar_primo(n): # Função que checa se um número é primo
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
        print("Eba! O número " + str(n) + " é primo!")
    else:
        print("Xi, o número " + str(n) + " não é primo!")
    
    # Para retornar True ou False, poderia usar o código "print(eh_primo)"

def entrada(): # Função de entrada de número pelo usuário
    n = int(input("Digite um número inteiro positivo: "))
    while n >= 0:
        checar_primo(n) # Chamada da função que checa se é primo
        n = int(input("Digite um número inteiro positivo: "))

##### INÍCIO DO PROGRAMA #####

entrada()
