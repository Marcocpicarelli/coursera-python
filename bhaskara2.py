import math # Importação do módulo math para usar raiz quadrada

def delta(a, b, c): #Função que calcula o delta
    delta = (b**2) - (4*a*c)
    return delta
    
def bhaskara(a, b, delta): #Função que calcula bhaskara
    if delta < 0:
        print("Seu delta é menor que zero.")
        print("Por isso, a sua equação não tem raízes reais.")
    elif delta == 0:
        x = (-b + (math.sqrt(0))) / (2*a)
        print("O seu delta é igual a zero.")
        print("Por isso, a única raiz da sua equação é " + str(x) + ".")
    elif delta > 0:
        x1 = (-b + (math.sqrt(delta))) / (2*a)
        x2 = (-b - (math.sqrt(delta))) / (2*a)
        print("As raízes da equação são " + str(x1) + " e " + str(x2) + ".")

###### INÍCIO DO PROGRAMA ######

x = float(input("Digite um valor para a: "))
y = float(input("Digite um valor para b: "))
z = float(input("Digite um valor para c: "))

delta = delta(x, y, z) # Chamada da função delta

resultado = bhaskara(x, y, delta) # Chamada da função bhaskara
