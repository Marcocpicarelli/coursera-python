def fatorial(x): # Função que calcula o fatorial de um número
    fatorial = 1
    while x > 1:
        fatorial = fatorial * x
        x = x - 1
    print(fatorial)

def entrada(): # Função de entrada do número pelo usuário
    n = int(input("Digite um número inteiro que você deseja saber o fatorial: "))
    while n >= 0:
        fatorial(n) # Chamada da função que calcula o fatorial  
        n = int(input("Digite um número inteiro que você deseja saber o fatorial: "))

##### INÍCIO DO PROGRAMA #####

entrada()
