# Programa que calcula Bhaskara #

import math # Importação do módulo math para usar raiz quadrada
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
delta = (b**2) - (4*a*c)
if delta < 0:
    print("Seu delta é menor que zero. Por isso, a sua equação não tem raízes reais.")
elif delta == 0:
    x = (-b + (math.sqrt(0))) / (2*a)
    print("Seu delta é igual a zero.")
    print("Por isso, a única raiz da sua equação é " + str(x) + ".")
elif delta > 0:
    x1 = (-b + (math.sqrt(delta))) / (2*a)
    x2 = (-b - (math.sqrt(delta))) / (2*a)
    if x1 < x2:
        print("As raízes da equação são " + str(x1) + " e " + str(x2) + ".")
    else:
        print("As raízes da equação são " + str(x2) + " e " + str(x1) + ".")
