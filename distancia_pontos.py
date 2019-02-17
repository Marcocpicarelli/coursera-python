# Programa que calcula a distância entre dois pontos em um plano

import math # Imporatação do módulo math para usar raiz quadrada

x1 = int(input("Digite o valor do eixo x do primeiro ponto: "))
y1 = int(input("Digite o valor do eixo y do primeiro ponto: "))
x2 = int(input("Digite o valor do eixo x do segundo ponto: "))
y2 = int(input("Digite o valor do eixo y do segundo ponto: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distancia >= 10:
    print("A distância " + str(distancia) + " é maior ou igual a 10.")
else:
    print("A distância " + str(distancia) + " é menor que 10.")
