import math # Importação do módulo math para usar raiz quadrada

def entrada_numeros(): # Função que recebe a entrada dos números
    x = float(input("Digite um valor para a: "))
    y = float(input("Digite um valor para b: "))
    z = float(input("Digite um valor para c: "))
    print(calcula_bhaskara(x, y, z)) # Chamada da função de bhaskara

def calcula_delta(a, b, c): # Função que calcula o delta
    return (b**2) - (4*a*c)
        
def calcula_bhaskara(a, b, c): # Função que calcula bhaskara
    d = calcula_delta(a, b, c) # Chamada da função que calcula o delta
    if d < 0:
        return 0
    elif d == 0:
        x = (-b + (math.sqrt(d))) / (2*a)
        return 1, x
    elif d > 0:
        x1 = (-b + (math.sqrt(d))) / (2*a)
        x2 = (-b - (math.sqrt(d))) / (2*a)
        return 2, x1, x2

###### INÍCIO DO PROGRAMA ######

entrada_numeros() # Chamada da função que recebe a entrada dos números
