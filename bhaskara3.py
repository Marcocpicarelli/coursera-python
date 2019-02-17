import math # Importação do módulo math para usar raiz quadrada

def entrada_numeros(): # Função que recebe a entrada dos números
    x = float(input("Digite um valor para a: "))
    y = float(input("Digite um valor para b: "))
    z = float(input("Digite um valor para c: "))
    bhaskara(x, y, z) # Chamada da função de bhaskara

def delta(a, b, c): # Função que calcula o delta
    return (b**2) - (4*a*c)
        
def bhaskara(a, b, c): # Função que calcula bhaskara
    d = delta(a, b, c) # Chamada da função que calcula o delta
    if d < 0:
        print("Seu delta é menor que zero.")
        print("Por isso, a sua equação não tem raízes reais.")
    elif d == 0:
        x = (-b + (math.sqrt(d))) / (2*a)
        print("O seu delta é igual a zero.")
        print("Por isso, a única raiz da sua equação é " + str(x) + ".")
    elif d > 0:
        x1 = (-b + (math.sqrt(d))) / (2*a)
        x2 = (-b - (math.sqrt(d))) / (2*a)
        print("As raízes da equação são " + str(x1) + " e " + str(x2) + ".")

###### INÍCIO DO PROGRAMA ######

entrada_numeros() # Chamada da função que recebe a entrada dos números
